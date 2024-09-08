#!/usr/bin/env python

import subprocess

subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether 00:11:22:33:44:55", shell=True)
subprocess.call("ifconfig eth0 up", shell=True)


#if you want to change the wired lan settings then you can use this - 

# subprocess.call("ifconfig wlan0 down", shell=True)
# subprocess.call("ifconfig wlan0 hw ether 00:11:22:33:44:55", shell=True)
# subprocess.call("ifconfig wlan0 up", shell=True)

