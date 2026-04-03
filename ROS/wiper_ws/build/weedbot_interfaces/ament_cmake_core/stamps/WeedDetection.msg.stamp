std_msgs/Header header

# Pixel coordinates (normalized 0-1)
float32[] bbox_x  # Bounding box x coordinates
float32[] bbox_y  # Bounding box y coordinates
float32[] bbox_w  # Bounding box widths
float32[] bbox_h  # Bounding box heights
float32[] confidences  # Detection confidences
int32[] class_ids  # Class IDs (if multiple weed types)

# NEW: Real-world coordinates (meters, relative to camera center on ground)
float32 real_world_x  # X position in meters (+ = right, - = left)
float32 real_world_y  # Y position in meters (+ = forward, - = backward)
float32 real_world_z  # Z position in meters (0 = ground plane)

# Optional segmentation mask
sensor_msgs/Image mask