import os
import subprocess

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'



print(bcolors.GREEN + '+[+[update y/n]+]+' + bcolors.RESET)
user_input = input()
if user_input == 'y':
    os.system('cd')
    os.system('rm -rf multitool')
    os.system('git clone https://github.com/Kittyy-Kittyy/multitool.git')
    
if user_input == 'n':
    print(bcolors.GREEN + 'exiting...' + bcolors.RESET)
    os.chdir(os.path.join(os.path.expanduser('~'), 'multitool'))
    subprocess.run(['python3', 'Setup.py'])
