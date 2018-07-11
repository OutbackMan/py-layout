import ctypes
import sys
import numpy

_current_platform: str = sys.platform()

if _current_platform == "win32":
    lib = ctypes.cdll.LoadLibrary("win-lib.dll")  
    # call like lib.func()
elif  



screenshot()
key_down(), key_up(), key_press()
enter_text()

mouse_init(relx, rely)
mouse_move()
mouse_up(), mouse_down(), mouse_click()
mouse_drag()
