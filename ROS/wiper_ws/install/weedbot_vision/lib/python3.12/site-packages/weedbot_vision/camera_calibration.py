#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from ament_index_python.packages import get_package_share_directory
import cv2
import numpy as np
import yaml
import os
import threading


class CameraCalibration(Node):
    def __init__(self):
        super().__init__('camera_calibration')
        self.bridge = CvBridge()
        self.current_frame = None
        self.frame_lock = threading.Lock()
        self.subscription = self.create_subscription(
            Image, '/camera/camera/color/image_raw', self.image_callback, 10)
        self.get_logger().info("Camera Calibration started — waiting for /camera/camera/color/image_raw ...")

    def image_callback(self, msg):
        with self.frame_lock:
            self.current_frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

    def get_frame(self):
        with self.frame_lock:
            return self.current_frame.copy() if self.current_frame is not None else None

    # ------------------------------------------------------------------ #
    #  On-screen text input — no terminal / stdin needed                  #
    # ------------------------------------------------------------------ #
    def _opencv_text_input(self, base_frame, active_idx, pixel_points, real_points_so_far):
        """
        Shows the frozen frame with:

          - all confirmed points in GREEN
          - the ACTIVE point pulsing in RED + a large label
          - a text input bar at the bottom
        Returns (x, y) float tuple once the user presses Enter.
        """
        typed = ""
        tick = 0

        while True:
            display = base_frame.copy()
            h, w = display.shape[:2]

            # Draw all points
            for i, p in enumerate(pixel_points):
                if i == active_idx:
                    # Pulse red (radius oscillates)
                    radius = 12 + int(6 * abs(np.sin(tick * 0.1)))
                    cv2.circle(display, p, radius, (0, 0, 255), 3)
                    cv2.circle(display, p, 5, (0, 0, 255), -1)
                    cv2.putText(display, f"P{i+1} <- HERE",
                                (p[0] + 14, p[1] - 14),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
                else:
                    color = (0, 200, 0) if i < active_idx else (100, 100, 100)
                    cv2.circle(display, p, 8, color, -1)
                    label = f"P{i+1}"
                    if i < len(real_points_so_far):
                        rx, ry = real_points_so_far[i]
                        label += f" ({rx:.2f},{ry:.2f})"
                    cv2.putText(display, label, (p[0] + 10, p[1] - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.65, color, 2)

            # Top banner
            banner = f"ENTER REAL-WORLD COORDS FOR POINT {active_idx+1}  (red dot)"
            cv2.rectangle(display, (0, 0), (w, 50), (0, 0, 120), -1)
            cv2.putText(display, banner, (10, 34),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.85, (0, 180, 255), 2)

            # Bottom input bar
            cv2.rectangle(display, (0, h - 90), (w, h), (20, 20, 20), -1)
            cv2.putText(display,
                        f"Type X Y in meters  e.g.  0.50 -0.30  or  0.50,-0.30",
                        (10, h - 58), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (180, 180, 180), 1)
            cv2.putText(display, f"> {typed}_",
                        (10, h - 22), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)
            cv2.putText(display, "Enter=confirm   Backspace=delete",
                        (w - 420, h - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (120, 120, 120), 1)

            cv2.imshow("Homography Calibration", display)
            key = cv2.waitKey(30) & 0xFF
            tick += 1

            if key == 13:  # Enter
                parts = typed.replace(',', ' ').split()
                if len(parts) >= 2:
                    try:
                        return float(parts[0]), float(parts[1])
                    except ValueError:
                        pass
                # flash red on bad input
                typed = ""
            elif key in (8, 127):  # Backspace
                typed = typed[:-1]
            elif key != 255:
                ch = chr(key)
                if ch in '0123456789.-_, ':
                    typed += ch

            rclpy.spin_once(self, timeout_sec=0.01)

    # ------------------------------------------------------------------ #
    #  Main calibration flow                                              #
    # ------------------------------------------------------------------ #
    def run_calibration(self):
        # Wait for first frame
        while rclpy.ok():
            frame = self.get_frame()
            if frame is not None:
                break
            rclpy.spin_once(self, timeout_sec=0.1)

        pixel_points = []
        display_frame = frame.copy()
        WIN = "Homography Calibration"

        def mouse_cb(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN and len(pixel_points) < 4:
                pixel_points.append((x, y))
                self.get_logger().info(f"Point {len(pixel_points)} pixel: ({x}, {y})")

        cv2.namedWindow(WIN)
        cv2.setMouseCallback(WIN, mouse_cb)

        # ---- Phase 0: show live feed until user freezes it ---- #
        self.get_logger().info("PHASE 0: Preview live feed. Press SPACE to freeze, then click 4 points.")
        frozen_frame = None
        while rclpy.ok():
            live = self.get_frame()
            if live is not None:
                display_frame = live.copy()

            h, w = display_frame.shape[:2]
            cv2.rectangle(display_frame, (0, 0), (w, 50), (0, 0, 0), -1)
            cv2.putText(display_frame, "LIVE PREVIEW  —  press SPACE to freeze frame  |  q=quit",
                        (10, 34), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 200, 255), 2)
            cv2.imshow(WIN, display_frame)
            key = cv2.waitKey(30) & 0xFF
            if key == ord('q'):
                cv2.destroyAllWindows(); return
            if key == ord(' '):
                frozen_frame = display_frame.copy()
                break
            rclpy.spin_once(self, timeout_sec=0.01)

        display_frame = frozen_frame.copy()

        # ---- Phase 1: click 4 pixel points on frozen frame ---- #
        self.get_logger().info("PHASE 1: Click 4 ground-plane points in the image.")
        self.get_logger().info("Tip: click them in a consistent order, e.g. top-left → top-right → bottom-right → bottom-left")

        while rclpy.ok():
            # Use frozen frame — do NOT update from live feed
            display_frame = frozen_frame.copy()

            h, w = display_frame.shape[:2]
            for i, p in enumerate(pixel_points):
                cv2.circle(display_frame, p, 8, (0, 255, 0), -1)
                cv2.putText(display_frame, f"P{i+1}", (p[0]+10, p[1]-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

            remaining = 4 - len(pixel_points)
            banner = (f"FROZEN — Click point {len(pixel_points)+1}/4"
                      if remaining > 0 else "4 points selected!")
            cv2.rectangle(display_frame, (0, 0), (w, 50), (0, 0, 0), -1)
            cv2.putText(display_frame, banner + "   r=reset  q=quit",
                        (10, 34), cv2.FONT_HERSHEY_SIMPLEX, 0.85, (0, 200, 255), 2)

            cv2.imshow(WIN, display_frame)
            key = cv2.waitKey(30) & 0xFF
            if key == ord('q'):
                cv2.destroyAllWindows(); return
            if key == ord('r'):
                pixel_points.clear()

            if len(pixel_points) == 4:
                break
            rclpy.spin_once(self, timeout_sec=0.01)

        # Freeze the frame with all 4 points drawn for Phase 2
        frozen = display_frame.copy()

        # ---- Phase 2: enter real-world coords per point ---- #
        self.get_logger().info("PHASE 2: Enter real-world (X,Y) in meters for each RED point.")
        self.get_logger().info("Origin = camera center projected on ground. +X = right, +Y = forward.")

        real_points = []
        for i in range(4):
            x, y = self._opencv_text_input(frozen, i, pixel_points, real_points)
            real_points.append((x, y))
            self.get_logger().info(f"Point {i+1} real-world: ({x:.4f}, {y:.4f}) m")

        # ---- Compute homography ---- #
        src = np.array(pixel_points, dtype=np.float32)
        dst = np.array(real_points, dtype=np.float32)
        H, _ = cv2.findHomography(src, dst)

        if H is None:
            self.get_logger().error("Homography computation failed — check your points.")
            cv2.destroyAllWindows(); return

        # Reprojection error
        errors = []
        for (px, py), (rx, ry) in zip(pixel_points, real_points):
            pt = np.array([[[px, py]]], dtype=np.float32)
            mapped = cv2.perspectiveTransform(pt, H)[0][0]
            err = np.sqrt((mapped[0]-rx)**2 + (mapped[1]-ry)**2)
            errors.append(err)
        mean_err = np.mean(errors)
        self.get_logger().info(f"Reprojection errors (m): {[f'{e:.4f}' for e in errors]}")
        self.get_logger().info(f"Mean reprojection error: {mean_err:.4f} m")
        if mean_err > 0.05:
            self.get_logger().warn("Mean error > 5 cm — consider re-calibrating with more accurate point clicks.")

        # ---- Phase 3: test mode ---- #
        test_click = [None]

        def test_mouse(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                pt = np.array([[[x, y]]], dtype=np.float32)
                rw = cv2.perspectiveTransform(pt, H)[0][0]
                rx, ry = float(rw[0]), float(rw[1])
                self.get_logger().info(f"TEST  pixel ({x},{y}) → ({rx:.3f} m, {ry:.3f} m)")
                test_click[0] = (x, y, rx, ry)

        cv2.setMouseCallback(WIN, test_mouse)
        self.get_logger().info("TEST MODE: click to verify coords. s=save  q=quit without saving.")

        while rclpy.ok():
            live = self.get_frame()
            test_frame = live.copy() if live is not None else frozen.copy()
            h, w = test_frame.shape[:2]

            # Draw calibration points for reference
            for i, p in enumerate(pixel_points):
                rx, ry = real_points[i]
                cv2.circle(test_frame, p, 6, (0, 255, 0), -1)
                cv2.putText(test_frame, f"P{i+1}({rx:.2f},{ry:.2f})",
                            (p[0]+8, p[1]-8), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 1)

            if test_click[0]:
                tx, ty, rx, ry = test_click[0]
                cv2.circle(test_frame, (tx, ty), 8, (0, 0, 255), -1)
                cv2.putText(test_frame, f"({rx:.3f},{ry:.3f})m",
                            (tx+10, ty-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            err_txt = f"Reproj err: {mean_err*100:.1f} cm mean"
            cv2.rectangle(test_frame, (0, 0), (w, 50), (0, 0, 0), -1)
            cv2.putText(test_frame,
                        f"TEST — click to verify  |  s=save  q=quit  |  {err_txt}",
                        (10, 34), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
            cv2.imshow(WIN, test_frame)

            key = cv2.waitKey(30) & 0xFF
            if key == ord('s'):
                break
            if key == ord('q'):
                self.get_logger().info("Quit without saving.")
                cv2.destroyAllWindows(); return

            rclpy.spin_once(self, timeout_sec=0.01)

        cv2.destroyAllWindows()
        self._save(H)

    def _save(self, H):
        try:
            pkg_share = get_package_share_directory('weedbot_vision')
        except Exception:
            pkg_share = os.path.expanduser(
                '~/wiper_ws/install/weedbot_vision/share/weedbot_vision')

        path = os.path.join(pkg_share, 'config', 'homography_matrix.yaml')
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            yaml.dump({'homography_matrix': H.tolist()}, f)
        self.get_logger().info(f"Saved: {path}")


def main(args=None):
    rclpy.init(args=args)
    node = CameraCalibration()
    try:
        node.run_calibration()
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
