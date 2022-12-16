import os
import platform

if __name__=="__main__":
    if platform.system().lower() == 'linux':
        # build c_cal.so file
        com_str = "gcc c_cal.c c_cal.h -fPIC -shared -o c_cal.so"
        os.system(com_str)
    elif platform.system().lower() == 'windows':
        pass