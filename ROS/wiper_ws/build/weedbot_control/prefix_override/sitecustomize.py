import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/sanya/fyp/W.I.P.E.R/ROS/wiper_ws/install/weedbot_control'
