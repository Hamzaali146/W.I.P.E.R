import cv2
import numpy as np
from skimage.filters import sobel, gabor, gaussian
from skimage.feature import canny

# Load images
rgb = cv2.imread('test_images/rgb.png', 0)
ir = cv2.imread('test_images/nir.png', 0)

if rgb is None or ir is None:
    print("Error: Put rgb.png and ir.png in folder!")
    exit()


# Resize NIR to match RGB exactly
if ir.shape != rgb.shape:
    nir_resized = cv2.resize(ir, (rgb.shape[1], rgb.shape[0]), interpolation=cv2.INTER_CUBIC)
    print(f"Resized NIR: {ir.shape} → {rgb.shape}")
else:
    nir_resized = ir.copy()
    print("Same size already")

ir_aligned = nir_resized

# Features 
rgb_edges = sobel(rgb)
rgb_gabor = np.mean([gabor(rgb, frequency=f)[0] for f in [0.1, 0.3]], axis=0)
rgb_salient = canny(rgb / 255.0) * 255
ir_grad = sobel(ir_aligned)  
ir_gaussian = gaussian(ir_aligned, sigma=2) 
rgb_features = np.stack([rgb, rgb_edges, rgb_gabor, rgb_salient], axis=-1)
ir_features = np.stack([ir_aligned, ir_grad, ir_gaussian], axis=-1)

# Decision maps 
def activity_measure(feature_map):
    return cv2.Laplacian(np.abs(feature_map), cv2.CV_64F)
rgb_decisions = np.array([activity_measure(f[:,:,0]) for f in np.split(rgb_features, 4, axis=-1)])  
ir_decisions = np.array([activity_measure(f[:,:,0]) for f in np.split(ir_features, 3, axis=-1)])  
rgb_decisions = (rgb_decisions - rgb_decisions.min()) / (rgb_decisions.max() - rgb_decisions.min() + 1e-6)
ir_decisions = (ir_decisions - ir_decisions.min()) / (ir_decisions.max() - ir_decisions.min() + 1e-6)

# Fusion 
def fuse_pixels(rgb_feat, ir_feat, rgb_dec, ir_dec):
    weight_rgb = rgb_dec / (rgb_dec + ir_dec + 1e-6)
    weight_ir = ir_dec / (rgb_dec + ir_dec + 1e-6)
    return weight_rgb * rgb_feat + weight_ir * ir_feat

fused = fuse_pixels(rgb.astype(np.float32), ir_aligned.astype(np.float32), 
                    np.mean(rgb_decisions, axis=0), np.mean(ir_decisions, axis=0))
fused = np.clip(fused, 0, 255).astype(np.uint8)

cv2.imwrite('fused_result.png', fused)
cv2.imwrite('ir_aligned.png', ir_aligned)
print("Done! Check fused_result.png")
