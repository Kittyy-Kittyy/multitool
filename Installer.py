import os
import subprocess


class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'






banner = '''
,--.                ,--.          ,--.,--.               
|  |,--,--,  ,---.,-'  '-. ,--,--.|  ||  | ,---. ,--.--. 
|  ||      \(  .-''-.  .-'' ,-.  ||  ||  || .-. :|  .--' 
|  ||  ||  |.-'  `) |  |  \ '-'  ||  ||  |\   --.|  |    
`--'`--''--'`----'  `--'   `--`--'`--'`--' `----'`--'   '''

print(bcolors.YELLOW + banner)
user_input = input('Do you want install all packages? y/n: ')

if user_input == 'y':
    os.system('sudo apt install nmap')
    os.system('sudo apt install aircrack-ng')
    os.system('sudo apt install python3-pip')

if user_input == 'n':
    print(bcolors.GREEN + 'exiting...' + bcolors.RESET)
    os.chdir(os.path.join(os.path.expanduser('~'), 'multitool'))
    subprocess.run(['python3', 'Setup.py'])
