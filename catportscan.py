import pyfiglet 
import sys
import socket
from datetime import datetime
import importlib


def check_packages(packages):
    for package in packages:
        try:
            importlib.import_module(package)
            print(f"Found '{package}' :D")
        except ImportError:
            print(f"Package '{package}' is NOT installed :c")

packages_to_check = ["colorama", "time", "os", "pyfiglet"]

check_packages(packages_to_check)

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

banner = pyfiglet.figlet_format("CAT PORT SCAN")
print(bcolors.GREEN + banner)  
print(bcolors.GREEN + "Made by Cat :3")  

target = input(bcolors.GREEN + "Target IP: ")

print(bcolors.GREEN + "_" * 50)  
print(bcolors.GREEN + "Scanning target: " + target)  
print(bcolors.GREEN + "Scanning started at: " + str(datetime.now()))  
print(bcolors.GREEN + "_" * 50)  

try:
    for port in range(1, 65536):  
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        # Print open port
        result = s.connect_ex((target, port))
        if result == 0:
            print(bcolors.GREEN + "[*] Port {} is open".format(port))  
        s.close()

except KeyboardInterrupt:
    print(bcolors.RESET + "\nExiting :(")  
    sys.exit()

except socket.error:
    print(bcolors.RED + "Host not responding :O")  
    sys.exit()

if exit:
    print(bcolors.RESET + 'Goodbye')
