import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ubantuu/robot_arm_ws/install/robot_ctrl_py'
