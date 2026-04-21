#!/usr/bin/env python3
"""
Weed Detection Vision Node for ROS 2 - Optimized for YOLO with Homography
"""

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import Header
from cv_bridge import CvBridge
from weedbot_interfaces.msg import WeedDetection, WeedArray

import cv2
import numpy as np
import time
import yaml
import os
from pathlib import Path
from ament_index_python.packages import get_package_share_directory


class VisionNode(Node):
    """
    Main vision node for weed detection using YOLO instance segmentation
    """
    
    def __init__(self):
        super().__init__('weedbot_vision_node')
        
        # Declare parameters
        self.declare_parameter('camera_topic', '/camera/image_raw')
        self.declare_parameter('model_path', '')
        self.declare_parameter('confidence_threshold', 0.5)
        self.declare_parameter('iou_threshold', 0.4)
        self.declare_parameter('input_size', 640)
        self.declare_parameter('device', 'cuda')
        self.declare_parameter('publish_viz', True)
        self.declare_parameter('viz_topic', '/weedbot/visualization')
        self.declare_parameter('max_det', 300)
        self.declare_parameter('use_homography', True)
        self.declare_parameter('verbose_inference', True)  # NEW: Control YOLO verbosity
        
        # Get parameters
        self.camera_topic = self.get_parameter('camera_topic').value
        self.model_path = self.get_parameter('model_path').value
        self.conf_threshold = self.get_parameter('confidence_threshold').value
        self.iou_threshold = self.get_parameter('iou_threshold').value
        self.input_size = self.get_parameter('input_size').value
        self.device = self.get_parameter('device').value
        self.publish_viz = self.get_parameter('publish_viz').value
        self.viz_topic = self.get_parameter('viz_topic').value
        self.max_det = self.get_parameter('max_det').value
        self.use_homography_param = self.get_parameter('use_homography').value
        self.verbose_inference = self.get_parameter('verbose_inference').value
        
        # Initialize CV Bridge
        self.bridge = CvBridge()
        
        # NEW: Store class names from model
        self.class_names = {}
        
        # Load homography matrix
        self.homography_matrix = None
        self.use_homography = False
        if self.use_homography_param:
            self.load_homography()
        
        # Load model
        self.model = None
        self.model_loaded = False
        if self.model_path:
            self.load_model()
        else:
            self.get_logger().error('No model path specified!')
            return
        
        # Subscriber
        self.image_sub = self.create_subscription(
            Image,
            self.camera_topic,
            self.image_callback,
            10
        )
        
        # Publishers
        self.detection_pub = self.create_publisher(
            WeedArray,
            '/weedbot/detections',
            10
        )
        
        if self.publish_viz:
            self.viz_pub = self.create_publisher(
                Image,
                self.viz_topic,
                10
            )
        
        # Statistics
        self.frame_count = 0
        self.total_inference_time = 0.0
        self.total_detections = 0
        
        # Timer for statistics (every 30 frames)
        self.stats_counter = 0
        
        self.get_logger().info('Vision Node initialized')
        self.get_logger().info(f'Listening to: {self.camera_topic}')
        self.get_logger().info(f'Device: {self.device}')
        self.get_logger().info(f'Model: {self.model_path}')
        self.get_logger().info(f'Homography: {"ENABLED" if self.use_homography else "DISABLED"}')
        self.get_logger().info(f'Class names: {list(self.class_names.values())}')
    
    def load_homography(self):
        """Load homography matrix from YAML file"""
        try:
            # Try to get package share directory
            try:
                package_path = get_package_share_directory('weedbot_vision')
            except:
                # Fallback to source directory
                package_path = os.path.expanduser('~/ros2_ws/src/weedbot_vision')
            
            yaml_path = os.path.join(package_path, 'config', 'homography_matrix.yaml')
            
            if not os.path.exists(yaml_path):
                self.get_logger().warn(f"Homography file not found: {yaml_path}")
                self.get_logger().warn("Run camera_calibration.py first to generate it")
                self.get_logger().warn("Continuing without homography - only pixel coordinates will be available")
                return
            
            with open(yaml_path, 'r') as f:
                data = yaml.safe_load(f)
            
            self.homography_matrix = np.array(data['homography_matrix'], dtype=np.float32)
            self.use_homography = True
            
            self.get_logger().info(f"✓ Homography matrix loaded from: {yaml_path}")
            self.get_logger().info("✓ Real-world coordinate transformation enabled")
            
        except Exception as e:
            self.get_logger().error(f"Failed to load homography: {e}")
            self.use_homography = False
    
    def pixel_to_real_world(self, pixel_x, pixel_y):
        """
        Transform pixel coordinates to real-world meters using homography
        
        Args:
            pixel_x: X coordinate in pixels
            pixel_y: Y coordinate in pixels
        
        Returns:
            (x_meters, y_meters): Real-world coordinates in meters
        """
        if not self.use_homography:
            return 0.0, 0.0
        
        try:
            # Prepare point for transformation
            pixel_point = np.array([[[pixel_x, pixel_y]]], dtype=np.float32)
            
            # Apply homography transformation
            real_point = cv2.perspectiveTransform(pixel_point, self.homography_matrix)
            
            x_meters = float(real_point[0][0][0])
            y_meters = float(real_point[0][0][1])
            
            return x_meters, y_meters
            
        except Exception as e:
            self.get_logger().error(f"Homography transformation error: {e}")
            return 0.0, 0.0
    
    def load_model(self):
        """Load the YOLO model"""
        try:
            model_path = Path(self.model_path)
            
            if not model_path.exists():
                self.get_logger().error(f'Model file not found: {self.model_path}')
                return
            
            self.get_logger().info(f'Loading YOLO model from: {self.model_path}')
            
            try:
                from ultralytics import YOLO
                self.model = YOLO(str(model_path))
                
                # Extract class names from model
                if hasattr(self.model, 'names'):
                    self.class_names = self.model.names
                    self.get_logger().info(f'Loaded {len(self.class_names)} class(es) from model: {list(self.class_names.values())}')
                    if len(self.class_names) == 1:
                        self.get_logger().info('Single-class mode: Weeds only')
                else:
                    self.get_logger().warn('Could not extract class names from model')
                    self.class_names = {0: 'Weed'}
                
                # Check device availability
                import torch
                if self.device == 'cuda' and not torch.cuda.is_available():
                    self.get_logger().warn('CUDA not available, using CPU')
                    self.device = 'cpu'
                
                self.get_logger().info(f'Model loaded successfully on {self.device}')
                self.model_loaded = True
                
                # Run a dummy inference to warm up
                dummy_img = np.zeros((640, 640, 3), dtype=np.uint8)
                self.model(dummy_img, verbose=False)
                self.get_logger().info('Model warmed up')
                
            except ImportError:
                self.get_logger().error('ultralytics not installed. Install with: pip3 install ultralytics')
                return
            
        except Exception as e:
            self.get_logger().error(f'Failed to load model: {str(e)}')
            self.model_loaded = False
    
    def image_callback(self, msg):
        """Callback for camera images"""
        if not self.model_loaded:
            return
        
        try:
            # Convert ROS Image to OpenCV
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            
            # Run detection
            start_time = time.time()
            detections = self.run_inference(cv_image)
            inference_time = (time.time() - start_time) * 1000  # ms
            
            # Create and publish detection message
            weed_array = self.create_detection_message(detections, msg.header, inference_time)
            self.detection_pub.publish(weed_array)
            
            # Publish visualization
            if self.publish_viz:
                viz_image = self.visualize_detections(cv_image, detections)
                viz_msg = self.bridge.cv2_to_imgmsg(viz_image, encoding='bgr8')
                viz_msg.header = msg.header
                self.viz_pub.publish(viz_msg)
            
            # Update statistics
            self.frame_count += 1
            self.total_inference_time += inference_time
            self.total_detections += len(detections)
            self.stats_counter += 1
            
            # Log stats every 30 frames
            if self.stats_counter >= 30:
                avg_fps = 30.0 / (inference_time / 1000.0 * 30)
                avg_inference = self.total_inference_time / self.frame_count
                avg_detections = self.total_detections / self.frame_count
                
                self.get_logger().info(
                    f'Stats - FPS: {avg_fps:.1f}, '
                    f'Inference: {avg_inference:.1f}ms, '
                    f'Avg Weeds: {avg_detections:.1f}'
                )
                self.stats_counter = 0
            
        except Exception as e:
            self.get_logger().error(f'Image callback error: {str(e)}')
    
    def run_inference(self, image):
        """Run YOLO inference"""
        try:
            # Run prediction
            results = self.model.predict(
                image,
                conf=self.conf_threshold,
                iou=self.iou_threshold,
                imgsz=self.input_size,
                device=self.device,
                verbose=self.verbose_inference,  # FIXED: Now respects parameter
                max_det=self.max_det
            )
            
            detections = []
            h, w = image.shape[:2]
            
            # Process results
            for result in results:
                boxes = result.boxes
                
                if boxes is not None and len(boxes) > 0:
                    for i in range(len(boxes)):
                        # Get box coordinates
                        box = boxes.xyxy[i].cpu().numpy()
                        x1, y1, x2, y2 = box
                        
                        # Get confidence and class
                        conf = float(boxes.conf[i].cpu().numpy())
                        cls = int(boxes.cls[i].cpu().numpy())

                        # Only process Weed detections (class 0)
                        if cls != 0:
                            continue

                        class_name = self.class_names.get(cls, 'Weed')
                        
                        # Calculate center in pixels
                        center_x_pixel = int((x1 + x2) / 2)
                        center_y_pixel = int((y1 + y2) / 2)
                        
                        # Transform to real-world coordinates
                        real_x, real_y = self.pixel_to_real_world(center_x_pixel, center_y_pixel)
                        
                        # Normalize coordinates (0-1)
                        detection = {
                            'bbox': [x1/w, y1/h, (x2-x1)/w, (y2-y1)/h],
                            'confidence': conf,
                            'class_id': cls,
                            'class_name': class_name,  # NEW
                            'center_x': ((x1 + x2) / 2) / w,
                            'center_y': ((y1 + y2) / 2) / h,
                            'pixel_x': center_x_pixel,
                            'pixel_y': center_y_pixel,
                            'real_world_x': real_x,
                            'real_world_y': real_y,
                            'real_world_z': 0.0
                        }
                        detections.append(detection)
            
            return detections
            
        except Exception as e:
            self.get_logger().error(f'Inference error: {str(e)}')
            return []
    
    def create_detection_message(self, detections, header, inference_time):
        """Create WeedArray message from detections"""
        weed_array = WeedArray()
        weed_array.header = header
        weed_array.total_weeds = len(detections)
        weed_array.inference_time_ms = inference_time
        
        for det in detections:
            weed_det = WeedDetection()
            weed_det.header = header
            weed_det.bbox_x = [det['bbox'][0]]
            weed_det.bbox_y = [det['bbox'][1]]
            weed_det.bbox_w = [det['bbox'][2]]
            weed_det.bbox_h = [det['bbox'][3]]
            weed_det.confidences = [det['confidence']]
            weed_det.class_ids = [det['class_id']]
            
            # Add real-world coordinates
            weed_det.real_world_x = det['real_world_x']
            weed_det.real_world_y = det['real_world_y']
            weed_det.real_world_z = det['real_world_z']
            
            weed_array.detections.append(weed_det)
        
        return weed_array
    
    def visualize_detections(self, image, detections):
        """Draw bounding boxes and labels on image"""
        viz_image = image.copy()
        h, w = image.shape[:2]
        
        for det in detections:
            x, y, w_box, h_box = det['bbox']
            conf = det['confidence']
            cls = det['class_id']
            class_name = det['class_name']  # NEW
            
            # Convert normalized to pixel coordinates
            x1 = int(x * w)
            y1 = int(y * h)
            x2 = int((x + w_box) * w)
            y2 = int((y + h_box) * h)
            
            # Color based on confidence (green for high, yellow for medium, red for low)
            if conf > 0.7:
                color = (0, 255, 0)  # Green
            elif conf > 0.5:
                color = (0, 255, 255)  # Yellow
            else:
                color = (0, 165, 255)  # Orange
            
            # Draw bounding box
            cv2.rectangle(viz_image, (x1, y1), (x2, y2), color, 2)
            
            # Draw center point
            center_x = det['pixel_x']
            center_y = det['pixel_y']
            cv2.circle(viz_image, (center_x, center_y), 5, (0, 0, 255), -1)
            
            # Label with coordinates and confidence
            if self.use_homography:
                real_x = det['real_world_x']
                real_y = det['real_world_y']
                label = f'Weed ({real_x:.2f}, {real_y:.2f})m {conf:.2f}'
            else:
                label = f'Weed {conf:.2f}'
            
            label_size, _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)
            
            # Draw background for text
            cv2.rectangle(viz_image, 
                         (x1, y1 - label_size[1] - 10),
                         (x1 + label_size[0], y1),
                         color, -1)
            
            # Draw text
            cv2.putText(viz_image, label, (x1, y1 - 5),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        
        # Draw stats on image
        stats_text = f'Weeds: {len(detections)}'
        cv2.putText(viz_image, stats_text, (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Add homography status indicator
        if self.use_homography:
            cv2.putText(viz_image, 'Real-World Coords: ON', (10, 60),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        
        return viz_image


def main(args=None):
    rclpy.init(args=args)
    node = VisionNode()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()