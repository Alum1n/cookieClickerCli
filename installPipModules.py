import os, sys, json, time, threading, platform
if sys.platform.startswith("linux"):
    distro = platform.freedesktop_os_release()
    if distro["NAME"] == "Arch Linux":
        os.system("sudo pacman -S python-pip")
        os.system("pip install colorama pynput --break-system-packages")
    else:
        print("imagine not using arch")