#!/usr/bin/env python

#Run the program using python3
#Use --help to see all the parsing options for ease of use

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Defines the interface to change its MAC address.")
    parser.add_option("-m", "--mac", dest="new_mac", help="Defines the new MAC address that is going to be changed on respective interface")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("Please specify a new MAC, use --help for more info.")
    return options

def change_mac(interface, new_mac):
    print("Changing the MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface,"up"])


options = get_arguments()
change_mac(options.interface, options.new_mac)
