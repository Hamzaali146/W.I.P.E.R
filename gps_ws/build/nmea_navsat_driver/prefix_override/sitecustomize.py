import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/fatima/W.I.P.E.R/gps_ws/install/nmea_navsat_driver'
