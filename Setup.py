import os
import importlib
import subprocess
import time


class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'


def pip_installer():
    try:
        os.system('sudo aot install python3-pip')
        subprocess.run(['python3'])
        os.system('sudo pip install tkinter')

    except ImportError:
        print(bcolors.RED + f"tkinter can not installed")



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
    print(bcolors.RED + 'WIFIBruteforce[09]                                   Back[b]' + bcolors.RESET)
    print(bcolors.RED + 'Update        [10]                                          ' + bcolors.RESET)
    print(bcolors.RED + '------------------------------------------------------------' + bcolors.RESET)



    user_input2 = input(bcolors.RED + 'Please select Tool: ' + bcolors.RESET)
    if user_input2 == 'b':
        os.chdir(os.path.join(os.path.expanduser('~'), 'multitool'))
        subprocess.run(['python3', 'Setup.py'])




    if user_input2 == '10':
        os.chdir(os.path.join(os.path.expanduser('~'), 'multitool'))
        subprocess.run(['python3', 'Update.py'])

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
print(bcolors.GREEN + 'v.2.0' + bcolors.RESET)
time.sleep(0.1)
print('')
print('')

print(bcolors.RED + '------------------------------------------------------------' + bcolors.RESET)
print(bcolors.RED + 'catportscan[01]' + '      Next                          [n ]' + bcolors.RESET)
print(bcolors.RED + 'EmailBomber[02]' + '      Minecraft IP scanner          [06]' + bcolors.RESET)
print(bcolors.RED + 'BruteForce [03]' + '      DDOS Server attack            [07]' + bcolors.RESET)
print(bcolors.RED + 'Exit       [04]' + '      VirusBuilder                  [08]' + bcolors.RESET)
print(bcolors.RED + '------------------------------------------------------------' + bcolors.RESET)
print('')
user_input = input(bcolors.RED + 'Please select tool: ' + bcolors.RESET)

if user_input == '01':
    os.chdir(os.path.join(os.path.expanduser('~'), 'multitool'))
    subprocess.run(['python3', 'catportscan.py'])

if user_input == '02':
    os.chdir(os.path.join(os.path.expanduser('~'), 'multitool'))
    subprocess.run(['python3', 'EmailBomber.py'])

if user_input == '03':
    os.chdir(os.path.join(os.path.expanduser('~'), 'multitool'))
    subprocess.run(['python3', 'BruteForce.py'])

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
    os.chdir(os.path.join(os.path.expanduser('~'), 'multitool'))
    subprocess.run(['python3', 'Client.py'])

if user_input == '06':
    os.chdir(os.path.join(os.path.expanduser('~'), 'multitool'))
    subprocess.run(['python3', 'MinecraftFindIP.py'])

if user_input == '07':
    os.chdir(os.path.join(os.path.expanduser('~'), 'multitool'))
    subprocess.run(['python3', 'attackServer(DDOS).py'])

if user_input == '08':
    os.chdir(os.path.join(os.path.expanduser('~'), 'multitool'))
    subprocess.run(['python3', 'VirusBuilder.py'])

if user_input == 'n':
    page_two()