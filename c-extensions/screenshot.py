import ctypes
import sys
import numpy

_current_platform: str = sys.platform()

if _current_platform == "win32":
    screenshot = ctypes.cdll.LoadLibrary("win-lib.dll")  
    # call like lib.func()
elif  

