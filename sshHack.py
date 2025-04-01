import os
import pyfiglet

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    PURPLE = '\033[95m'

banenr = pyfiglet.figlet_format('SSH HACKER')

print(bcolors.GREEN + banenr + bcolors.RESET)

def installer():
    user = input(bcolors.RED + 'Do you want to install the packages? [y/n]: ' + bcolors.RESET)

    if user == 'y':
        try: 
            os.system('sudo apt install netcat')
            os.system('sudo apt install netcat-openbsd')
        except Exception as e:
            print(bcolors.RED + f'Error: {e}')

    if user == 'n':
        main()

def main():
    user2 = input(bcolors.GREEN + 'Enter IP adress: ' + bcolors.RESET)
    user3 = input(bcolors.GREEN + 'Enter username: ' + bcolors.RESET)

    try:
        print(bcolors.YELLOW + 'Scanning for ssh ports...' + bcolors.RESET)

        for port in range(1, 65535):
            os.system(f'nc {user2} {port}')
    except Exception as e2:
        print(bcolors.RED + f'Error: {e2}' + bcolors.RESET)

    try:
        print(bcolors.GREEN + 'Trying to connect...' + bcolors.RESET)
        os.system(f'ssh {user3}@{user2}')
    except Exception as e3:
        print(bcolors.RED + f'Error: {e3}' + bcolors.RESET)
    
installer()