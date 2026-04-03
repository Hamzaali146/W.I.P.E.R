# weedbot_vision/bridge.py
import rclpy
from rclpy.node import Node
from weedbot_interfaces.msg import WeedArray, WeedDetection
import zmq
import json

class BridgeNode(Node):
    def __init__(self):
        super().__init__('vision_bridge')

        #ROS publisher
        self.publisher = self.create_publisher(
            WeedArray,
            '/weedbot/detections',
            10
        )

        #ZMQ setup: this RECEIVES coordinates from vision_service.py
        context = zmq.Context()
        self.socket = context.socket(zmq.PULL)
        self.socket.bind("tcp://*:5555")  # vision_service.py connects here

        #Check for new messages every 100ms (non-blocking)
        self.create_timer(0.1, self.check_zmq)

        self.get_logger().info("Bridge ready, waiting for detections...")

    def check_zmq(self):
        """Called every 100ms by ROS timer — checks if vision sent anything"""
        try:
            raw = self.socket.recv_string(flags=zmq.NOBLOCK)
            data = json.loads(raw)
            self.publish_to_ros(data)
        except zmq.Again:
            pass  # nothing received yet, that's fine

    def publish_to_ros(self, data):
        """Takes coordinates and publishes them as ROS message"""
        msg = WeedArray()
        msg.total_weeds = len(data["detections"])

        for det in data["detections"]:
            weed = WeedDetection()
            weed.bbox_x       = [det["bbox"][0]]
            weed.bbox_y       = [det["bbox"][1]]
            weed.bbox_w       = [det["bbox"][2]]
            weed.bbox_h       = [det["bbox"][3]]
            weed.confidences  = [det["confidence"]]
            weed.class_ids    = [det["class_id"]]
            weed.real_world_x = det["real_world_x"]
            weed.real_world_y = det["real_world_y"]
            weed.real_world_z = 0.0
            msg.detections.append(weed)

        self.get_logger().info(f"Published {msg.total_weeds} weeds to /weedbot/detections")
        self.publisher.publish(msg)


def main():
    rclpy.init()
    node = BridgeNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()