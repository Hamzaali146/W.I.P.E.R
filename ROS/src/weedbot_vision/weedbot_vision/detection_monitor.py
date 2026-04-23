#!/usr/bin/env python3
"""
Detection Monitor Node
Subscribes to weed detections and provides logging/statistics
"""

import rclpy
from rclpy.node import Node
from weedbot_interfaces.msg import WeedArray
import time


class DetectionMonitor(Node):
    """
    Monitors and logs weed detection statistics
    """
    
    def __init__(self):
        super().__init__('detection_monitor')
        
        # Declare parameters
        self.declare_parameter('detection_topic', '/weedbot/detections')
        self.declare_parameter('log_interval', 5.0)  # seconds
        self.declare_parameter('verbose', True)
        
        # Get parameters
        self.detection_topic = self.get_parameter('detection_topic').value
        self.log_interval = self.get_parameter('log_interval').value
        self.verbose = self.get_parameter('verbose').value
        
        # Subscribe to detections
        self.detection_sub = self.create_subscription(
            WeedArray,
            self.detection_topic,
            self.detection_callback,
            10
        )
        
        # Statistics
        self.total_detections = 0
        self.total_frames = 0
        self.total_inference_time = 0.0
        self.detection_confidences = []
        self.last_log_time = time.time()
        self.detections_per_frame = []
        
        # Timer for periodic logging
        self.log_timer = self.create_timer(
            self.log_interval,
            self.log_statistics
        )
        
        self.get_logger().info('Detection Monitor initialized')
        self.get_logger().info(f'Monitoring: {self.detection_topic}')
    
    def detection_callback(self, msg):
        """Process detection message"""
        self.total_frames += 1
        self.total_detections += msg.total_weeds
        self.total_inference_time += msg.inference_time_ms
        self.detections_per_frame.append(msg.total_weeds)
        
        # Collect confidence scores
        for detection in msg.detections:
            if detection.confidences:
                self.detection_confidences.extend(detection.confidences)
        
        # Verbose logging
        if self.verbose and msg.total_weeds > 0:
            self.get_logger().info(
                f'Frame {self.total_frames}: {msg.total_weeds} weeds detected, '
                f'inference: {msg.inference_time_ms:.2f}ms'
            )
            
            # Log individual detections
            for i, detection in enumerate(msg.detections):
                if detection.confidences:
                    conf = detection.confidences[0]
                    x = detection.bbox_x[0]
                    y = detection.bbox_y[0]
                    self.get_logger().info(
                        f'  Weed {i+1}: conf={conf:.3f}, pos=({x:.3f}, {y:.3f})'
                    )
    
    def log_statistics(self):
        """Log accumulated statistics"""
        if self.total_frames == 0:
            self.get_logger().info('No detections received yet')
            return
        
        # Calculate statistics
        avg_detections = self.total_detections / self.total_frames
        avg_inference = self.total_inference_time / self.total_frames
        
        avg_confidence = 0.0
        if self.detection_confidences:
            avg_confidence = sum(self.detection_confidences) / len(self.detection_confidences)
        
        # Calculate detection rate (frames with at least one detection)
        frames_with_detections = sum(1 for x in self.detections_per_frame if x > 0)
        detection_rate = (frames_with_detections / self.total_frames) * 100
        
        self.get_logger().info('═' * 60)
        self.get_logger().info('DETECTION STATISTICS')
        self.get_logger().info('─' * 60)
        self.get_logger().info(f'Total Frames:          {self.total_frames}')
        self.get_logger().info(f'Total Detections:      {self.total_detections}')
        self.get_logger().info(f'Avg Detections/Frame:  {avg_detections:.2f}')
        self.get_logger().info(f'Detection Rate:        {detection_rate:.1f}%')
        self.get_logger().info(f'Avg Confidence:        {avg_confidence:.3f}')
        self.get_logger().info(f'Avg Inference Time:    {avg_inference:.2f}ms')
        self.get_logger().info('═' * 60)
        
        # Reset periodic statistics
        self.detection_confidences = []
        self.detections_per_frame = []


def main(args=None):
    rclpy.init(args=args)
    node = DetectionMonitor()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()