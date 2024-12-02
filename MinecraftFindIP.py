import os
import time

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'


print(bcolors.GREEN + ' ███▄ ▄███▓ ██▓ ███▄    █ ▓█████  ▄████▄   ██▀███   ▄▄▄         █████▒▄▄▄█████▓  █████▒██▓ ███▄    █ ▓█████▄  ██▓ ██▓███ ')
time.sleep(0.1) 
print(bcolors.GREEN + '▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▓█   ▀ ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▓██   ▒ ▓  ██▒ ▓▒▓██   ▒▓██▒ ██ ▀█   █ ▒██▀ ██▌▓██▒▓██░  ██▒')
time.sleep(0.1)
print(bcolors.GREEN + '▓██    ▓██░▒██▒▓██  ▀█ ██▒▒███   ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▒████ ░ ▒ ▓██░ ▒░▒████ ░▒██▒▓██  ▀█ ██▒░██   █▌▒██▒▓██░ ██▓▒')
time.sleep(0.1)
print(bcolors.GREEN + '▒██    ▒██ ░██░▓██▒  ▐▌██▒▒▓█  ▄ ▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ░▓█▒  ░ ░ ▓██▓ ░ ░▓█▒  ░░██░▓██▒  ▐▌██▒░▓█▄   ▌░██░▒██▄█▓▒ ▒')
time.sleep(0.1)
print(bcolors.GREEN + '▒██▒   ░██▒░██░▒██░   ▓██░░▒████▒▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒░▒█░      ▒██▒ ░ ░▒█░   ░██░▒██░   ▓██░░▒████▓ ░██░▒██▒ ░  ░')
time.sleep(0.1)
print(bcolors.GREEN + '░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░      ▒ ░░    ▒ ░   ░▓  ░ ▒░   ▒ ▒  ▒▒▓  ▒ ░▓  ▒▓▒░ ░  ░')
time.sleep(0.1)
print(bcolors.GREEN + '░  ░      ░ ▒ ░░ ░░   ░ ▒░ ░ ░  ░  ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░ ░          ░     ░      ▒ ░░ ░░   ░ ▒░ ░ ▒  ▒  ▒ ░░▒ ░     ')
time.sleep(0.1)
print(bcolors.GREEN + '░      ░    ▒ ░   ░   ░ ░    ░   ░          ░░   ░   ░   ▒    ░ ░      ░       ░ ░    ▒ ░   ░   ░ ░  ░ ░  ░  ▒ ░░░       ')
time.sleep(0.1)
print(bcolors.GREEN + '       ░    ░           ░    ░  ░░ ░         ░           ░  ░                         ░           ░    ░     ░           ')
time.sleep(0.1)
print(bcolors.GREEN + '                                 ░                                                                   ░                   ')


time.sleep(0.5)
print(bcolors.GREEN + 'Enter server adress:')
user_input = input()
os.system('nslookup mc' + user_input)
time.sleep(0.5)

if exit:
    print(bcolors.RESET + 'Goodbye')

