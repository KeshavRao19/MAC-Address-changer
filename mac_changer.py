#!/usr/bin/env python

#Run the program using python3
#Use --help to see all the parsing options for ease of use

import subprocess
import argparse
import re

def get_arguments():
    parser = argparse.ArgumentParser(description="This will change MAC address of any network interface.")
    parser.add_argument("-i", "--interface", required=True, help="Defines the interface to change its MAC address.")
    parser.add_argument("-m", "--mac", required=True, help="Defines the new MAC address to assign to the specified interface.")
    args = parser.parse_args()
    return args

def change_mac(interface, new_mac):
    print(f"Changing MAC address for {interface} to {new_mac}")
    try:
        subprocess.call(["sudo", "ifconfig", interface, "down"])
        subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
        subprocess.call(["sudo", "ifconfig", interface, "up"])
        print(f"MAC address changed successfully to {new_mac}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to change MAC address: {e}")

def get_current_mac(interface):
    try:
        ifconfig_result = subprocess.check_output(["ifconfig", interface], encoding='utf-8')
        search_result = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", ifconfig_result)
        if search_result:
            return search_result.group(0)
        else:
            print("Unable to fetch MAC address from the interface.")
            return None
    except subprocess.CalledProcessError as e:
        print(f"Failed to get MAC address: {e}")
        return None

if __name__ == "__main__":
    options = get_arguments()

    current_mac = get_current_mac(options.interface)
    if current_mac:
        print(f"Current MAC = {current_mac}")
        change_mac(options.interface, options.mac)
        new_mac = get_current_mac(options.interface)
        if new_mac == options.mac:
            print(f"MAC address of {options.interface} was successfully changed to {new_mac}")
        else:
            print("MAC address change has failed...")
