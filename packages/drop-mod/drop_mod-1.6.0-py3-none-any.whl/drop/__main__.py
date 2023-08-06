"""
The basic drop-mod launcher. Usually launches a GUI.
"""

# the user wants to run drop directly
import os
from sys import exit as sys_exit

RUN_GUI = True

# check if it'll be possible to run drop-gui
if (os.getenv("DISPLAY") is None) and (os.name == 'posix'):
    RUN_GUI = "Cannot run drop-gui due to no DISPLAY variable: this likely means that this " \
              "session is running without graphics interface, such as in a tty terminal."
# i have no idea how this will work for Windows. can you even not run have a UI on Windows?
# is that even possible?

# if type(RUN_GUI) is not str:
# What the actual fuck was I thinking when writing this?
if RUN_GUI:
    import drop.gui
    try:
        drop.gui.start_gui()
    except ImportError:
        sys_exit("Dear PyGui not installed: cannot run the GUI without the core GUI library.")
else:
    sys_exit(RUN_GUI)
