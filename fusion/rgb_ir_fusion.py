import os
import re
import cv2
import numpy as np
from skimage.filters import sobel, gabor, gaussian
from skimage.feature import canny

RGB_DIR = "rgb"
NIR_DIR = "nir"
OUT_DIR = "fused_output"

os.makedirs(OUT_DIR, exist_ok=True)

def extract_id(filename: str):
    """
    Extract the numeric id from names like:
      rgb_00000.png, nir_00000.jpg, etc.
    Returns: "00000" or None if not found.
    """
    m = re.search(r"_(\d+)", filename)
    return m.group(1) if m else None

def activity_measure(feature_map):
    return cv2.Laplacian(np.abs(feature_map), cv2.CV_64F)

def fuse_pixels(rgb_img, nir_img):
    # Resize NIR to match RGB
    if nir_img.shape != rgb_img.shape:
        nir_img = cv2.resize(nir_img, (rgb_img.shape[1], rgb_img.shape[0]), interpolation=cv2.INTER_CUBIC)

    # Features
    rgb_edges = sobel(rgb_img)
    rgb_gabor = np.mean([gabor(rgb_img, frequency=f)[0] for f in [0.1, 0.3]], axis=0)
    rgb_salient = canny(rgb_img / 255.0) * 255

    ir_grad = sobel(nir_img)
    ir_gaussian = gaussian(nir_img, sigma=2)

    rgb_features = np.stack([rgb_img, rgb_edges, rgb_gabor, rgb_salient], axis=-1)
    ir_features = np.stack([nir_img, ir_grad, ir_gaussian], axis=-1)

    # Decision maps
    rgb_decisions = np.array([activity_measure(f[:, :, 0]) for f in np.split(rgb_features, 4, axis=-1)])
    ir_decisions = np.array([activity_measure(f[:, :, 0]) for f in np.split(ir_features, 3, axis=-1)])

    rgb_decisions = (rgb_decisions - rgb_decisions.min()) / (rgb_decisions.max() - rgb_decisions.min() + 1e-6)
    ir_decisions = (ir_decisions - ir_decisions.min()) / (ir_decisions.max() - ir_decisions.min() + 1e-6)

    rgb_dec = np.mean(rgb_decisions, axis=0)
    ir_dec = np.mean(ir_decisions, axis=0)

    # Fusion weights
    weight_rgb = rgb_dec / (rgb_dec + ir_dec + 1e-6)
    weight_ir = ir_dec / (rgb_dec + ir_dec + 1e-6)

    fused = (weight_rgb * rgb_img.astype(np.float32)) + (weight_ir * nir_img.astype(np.float32))
    fused = np.clip(fused, 0, 255).astype(np.uint8)

    return fused

rgb_files = [f for f in os.listdir(RGB_DIR) if os.path.isfile(os.path.join(RGB_DIR, f))]
nir_files = [f for f in os.listdir(NIR_DIR) if os.path.isfile(os.path.join(NIR_DIR, f))]

rgb_map = {}
nir_map = {}

for f in rgb_files:
    fid = extract_id(f)
    if fid is not None:
        rgb_map[fid] = f

for f in nir_files:
    fid = extract_id(f)
    if fid is not None:
        nir_map[fid] = f

common_ids = sorted(set(rgb_map.keys()) & set(nir_map.keys()))

if not common_ids:
    print("No matching rgb_xxxxx and nir_xxxxx pairs found.")
    exit()

print(f"Found {len(common_ids)} matching pairs.")

for fid in common_ids:
    rgb_path = os.path.join(RGB_DIR, rgb_map[fid])
    nir_path = os.path.join(NIR_DIR, nir_map[fid])

    rgb = cv2.imread(rgb_path, 0)
    nir = cv2.imread(nir_path, 0)

    if rgb is None or nir is None:
        print(f"[SKIP] Could not read: {rgb_path} or {nir_path}")
        continue

    fused = fuse_pixels(rgb, nir)

    out_name = f"fused_{fid}.png"
    out_path = os.path.join(OUT_DIR, out_name)
    cv2.imwrite(out_path, fused)

    print(f"[OK] {rgb_map[fid]} + {nir_map[fid]} -> {out_name}")

print(f"Done! Check output folder: {OUT_DIR}")