import os
import importlib
import subprocess
import time
import pyfiglet

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

def check_packages(packages):
    for package in packages:
        try:
            importlib.import_module(package)
            print(bcolors.GREEN + f"Found '{package}' :D" + bcolors.RESET)
        except ImportError:
            print(bcolors.RED + f"Package '{package}' is NOT installed :c" + bcolors.RESET)

packages_to_check = ["mcpi", "time", "os", "importlib", "subprocess", "socket", "tkinter", "pyfiglet"]

check_packages(packages_to_check)
time.sleep(0.1)

print(bcolors.RED + ' ██ ▄█▀ ██▓▄▄▄█████▓▄▄▄█████▓▓██   ██▓ ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀' + bcolors.RESET)
time.sleep(0.3)
print(bcolors.RED + '▓███▄░ ▒██▒▒ ▓██░ ▒░▒ ▓██░ ▒░  ▒██ ██░▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ' + bcolors.RESET)
time.sleep(0.3)
print(bcolors.RED + '▓██ █▄ ░██░░ ▓██▓ ░ ░ ▓██▓ ░   ░ ▐██▓░░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ' + bcolors.RESET)
time.sleep(0.3)
print(bcolors.RED + '▒██▒ █▄░██░  ▒██▒ ░   ▒██▒ ░   ░ ██▒▓░░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄' + bcolors.RESET)
time.sleep(0.3)
print(bcolors.RED + '▒ ▒▒ ▓▒░▓    ▒ ░░     ▒ ░░      ██▒▒▒  ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒' + bcolors.RESET)
time.sleep(0.3)
print(bcolors.RED + '░ ░▒ ▒░ ▒ ░    ░        ░     ▓██ ░▒░  ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░' + bcolors.RESET)
time.sleep(0.3)
print(bcolors.RED + '░ ░░ ░  ▒ ░  ░        ░       ▒ ▒ ░░   ░  ░░ ░  ░   ▒   ░        ░ ░░ ░ ' + bcolors.RESET)
time.sleep(0.3)
print(bcolors.RED + '░  ░    ░                     ░ ░      ░  ░  ░      ░  ░░ ░      ░  ░   ' + bcolors.RESET)
time.sleep(0.3)
print(bcolors.RED + '                              ░ ░                       ░               ' + bcolors.RESET)
time.sleep(0.3)
print(bcolors.GREEN + 'Made by Kittyy :3' + bcolors.RESET)
time.sleep(0.1)
print(bcolors.GREEN + 'v.1.6' + bcolors.RESET)
time.sleep(0.1)
print('')
print('')

print(bcolors.RED + '____________________________________________________________')

print(bcolors.RED + 'catportscan[01]' + '      Client to join welldream probe[05]' + bcolors.RESET)
print(bcolors.RED + 'EmailBomber[02]' + '      Minecraft port scanner        [06]' + bcolors.RESET)
print(bcolors.RED + 'J.A.R.V.I.S[03]' + '      DDOS Server attack            [07]' + bcolors.RESET)
print(bcolors.RED + 'Exit       [04]' + '      Info                          [08]' + bcolors.RESET)
print(bcolors.RED + '____________________________________________________________')
print('')
user_input = input(bcolors.RED + 'Please select tool: ' + bcolors.RESET)

# Pfad basierend auf aktuellem Arbeitsverzeichnis
current_path = os.path.dirname(os.path.abspath(__file__))
multitool_path = os.path.join(current_path, 'MultikIttyy')

if user_input == '01':
    os.chdir(multitool_path)
    subprocess.run(['python3', 'catportscan.py'])

if user_input == '02':
    os.chdir(multitool_path)
    subprocess.run(['python3', 'EmailBomber.py'])

if user_input == '03':
    os.chdir(multitool_path)
    subprocess.run(['python3', 'JARVIS.py'])

if user_input == '04':
    print(bcolors.GREEN + 'Exit in:')
    print(bcolors.GREEN + '1')
    time.sleep(1)
    print(bcolors.GREEN + '2')
    time.sleep(1)
    print(bcolors.GREEN + '3')
    time.sleep(1)
    print(bcolors.GREEN + '4')
    print(bcolors.RESET + 'Goodbye')
    exit()

if user_input == '05':
    os.chdir(multitool_path)
    subprocess.run(['python3', 'Client.py'])

if user_input == '06':
    os.chdir(multitool_path)
    subprocess.run(['python3', 'MinecraftFindIP.py'])

if user_input == '07':
    os.chdir(multitool_path)
    subprocess.run(['python3', 'attackServer(DDOS).py'])
