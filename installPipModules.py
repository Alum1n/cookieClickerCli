import os, sys, json, time, threading, platform
if sys.platform.startswith("linux"):
    distro = platform.freedesktop_os_release()
    if distro["NAME"] == "Arch Linux":
        os.system("sudo pacman -S python-pip")
        os.system("pip install colorama pynput --break-system-packages")
    elif distro["NAME"] == "Debian":
        os.system("apt install python3-pip")
        os.system("pip install colorama pynput --break-system-packages")
    else:
        print("This only supports Arch Linux and Debian")
        print("The pip modules needed are: colorama, pynput")
else:
    print("This only supports Arch Linux and Debian")
    print("The pip modules needed are: colorama, pynput")
