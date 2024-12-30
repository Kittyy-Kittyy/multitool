import os



class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'


def pip_installer():
    try:
        Liste = ['tkinter', 'importlib']
        os.system('sudo apt install python3-pip')
        os.system('sudo pip install tkinter --break-system-packages')
        os.system('sudo pip install importlib --break-system-packages')
    
    except ImportError:
        print(bcolors.RED + f"{Liste} can not installed" + bcolors.RESET)
from tkinter import *
import importlib
import time




def check_packages(packages):
    for package in packages:
        try:
            importlib.import_module(package)
            print(bcolors.GREEN + f"Found '{package}' :D" + bcolors.RESET)
        except ImportError:
            print(bcolors.RED + f"Package '{package}' is NOT installed :c" + bcolors.RESET)

packages_to_check = ["time", "os", "importlib", "subprocess", "socket", "tkinter", "pyfiglet"]



def page_two():
    print(bcolors.RED + '------------------------------------------------------------' + bcolors.RESET)
    print(bcolors.RED + 'Installer            [09]                   Back        [b ]' + bcolors.RESET)
    print(bcolors.RED + 'Update               [10]                   KittyyMap   [12]' + bcolors.RESET)
    print(bcolors.RED + 'ClientForVirusBuilder[11]                                   ' + bcolors.RESET)
    print(bcolors.RED + '------------------------------------------------------------' + bcolors.RESET)



    user_input2 = input(bcolors.RED + 'Please select Tool: ' + bcolors.RESET)
    if user_input2 == 'b':
        os.system('sudo python3 Setup.py')




    if user_input2 == '10':
        os.system('sudo python3 Update.py')


    if user_input2 == '11':
        os.system('sudo python3 Client2.py')


    if user_input2 == '12':
        os.system('sudo python3 KittyyMap.py')


    if user_input2 == '09':
        os.system('sudo python3 Installer.py')

    if user_input2 == '9':
        os.system('sudo python3 Installer.py')



    

check_packages(packages_to_check)
time.sleep(0.1)

print(bcolors.RED + ' ██ ▄█▀ ██▓▄▄▄█████▓▄▄▄█████▓▓██   ██▓ ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀' + bcolors.RESET)
time.sleep(0.05)
print(bcolors.RED + '▓███▄░ ▒██▒▒ ▓██░ ▒░▒ ▓██░ ▒░  ▒██ ██░▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ' + bcolors.RESET)
time.sleep(0.05)
print(bcolors.RED + '▓██ █▄ ░██░░ ▓██▓ ░ ░ ▓██▓ ░   ░ ▐██▓░░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ' + bcolors.RESET)
time.sleep(0.05)
print(bcolors.RED + '▒██▒ █▄░██░  ▒██▒ ░   ▒██▒ ░   ░ ██▒▓░░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄' + bcolors.RESET)
time.sleep(0.05)
print(bcolors.RED + '▒ ▒▒ ▓▒░▓    ▒ ░░     ▒ ░░      ██▒▒▒  ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒' + bcolors.RESET)
time.sleep(0.05)
print(bcolors.RED + '░ ░▒ ▒░ ▒ ░    ░        ░     ▓██ ░▒░  ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░' + bcolors.RESET)
time.sleep(0.05)
print(bcolors.RED + '░ ░░ ░  ▒ ░  ░        ░       ▒ ▒ ░░   ░  ░░ ░  ░   ▒   ░        ░ ░░ ░ ' + bcolors.RESET)
time.sleep(0.05)
print(bcolors.RED + '░  ░    ░                     ░ ░      ░  ░  ░      ░  ░░ ░      ░  ░   ' + bcolors.RESET)
time.sleep(0.05)
print(bcolors.RED + '                              ░ ░                       ░               ' + bcolors.RESET)
time.sleep(0.05)
print(bcolors.GREEN + 'Made by Kittyy :3' + bcolors.RESET)
time.sleep(0.05)
print(bcolors.GREEN + 'v.2.0' + bcolors.RESET)
time.sleep(0.05)
print('')
print('')

print(bcolors.RED + '------------------------------------------------------------' + bcolors.RESET)
print(bcolors.RED + 'catportscan[01]' + '      Next                          [n ]' + bcolors.RESET)
print(bcolors.RED + 'EmailBomber[02]' + '      Minecraft IP scanner          [05]' + bcolors.RESET)
print(bcolors.RED + 'BruteForce [03]' + '      DDOS Server attack            [06]' + bcolors.RESET)
print(bcolors.RED + 'Exit       [04]' + '      VirusBuilder                  [07]' + bcolors.RESET)
print(bcolors.RED + '------------------------------------------------------------' + bcolors.RESET)
print('')
user_input = input(bcolors.RED + 'Please select tool: ' + bcolors.RESET)

if user_input == '01':
    os.system('sudo python3 catportscan.py')

if user_input == '1':
    os.system('sudo python3 catportscan.py')

if user_input == '02':
    os.system('sudo python3 EmalBomber.py')

if user_input == '2':
    os.system('sudo python3 EmailBomber.py')

if user_input == '03':
    os.system('sudo python3 BruteForce.py')

if user_input== '3':
    os.system('sudo python3 BruteForce.py')

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

if user_input == '4':
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
    os.system('sudo python3 MinecraftFindIP.py')

if user_input == '5':
    os.system('sudo python3 MinecraftFindIP.py')

if user_input == '06':
    os.system('sudo pyhon3 attackServer(DDOS).py')

if user_input == '6':
    os.system('sudo python3 attackServer(DDOS).py')

if user_input == '07':
    os.system('sudo python3 VirusBuilder.py')

if user_input == '7':
    os.system('sudo python3 VirusBuilder.py')

if user_input == 'n':
    page_two()