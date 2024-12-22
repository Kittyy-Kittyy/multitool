import os

print('+[+[update y/n]+]+')
user_input = input()
if user_input == 'y':
    os.system('rm -rf multitool')
    os.system('git clone https://github.com/Kittyy-Kittyy/multitool.git')
    
if user_input == 'n':
    exit