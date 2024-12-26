import os


class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'



print(bcolors.GREEN + '+[+[update y/n]+]+' + bcolors.RESET)
user_input = input()
if user_input == 'y':
    os.system('rm -rf multitool')
    os.system('git clone https://github.com/Kittyy-Kittyy/multitool.git')
    
if user_input == 'n':
    print(bcolors.GREEN + 'exiting...' + bcolors.RESET)
    exit