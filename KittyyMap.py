import os
import time


class bcolors:
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  RESET = '\033[0m'
  MAGENTA = '\033[95m'



banner = '''
 __________________________________________________________________________
|  ___  ____    _   _     _                  ____    ____                  |
| |_  ||_  _|  (_) / |_  / |_               |_   \  /   _|                 |
|   | |_/ /    __ `| |-'`| |-' _   __  _   __ |   \/   |   ,--.  _ .--.    |
|   |  __'.   [  | | |   | |  [ \ [  ][ \ [  ]| |\  /| |  `'_\ :[ '/'`\ \  |
|  _| |  \ \_  | | | |,  | |,  \ '/ /  \ '/ /_| |_\/_| |_ // | |,| \__/ |  |
| |____||____|[___]\__/  \__/[\_:  / [\_:  /|_____||_____|\'-;__/| ;.__/    |
|                             \__.'   \__.'                     [__|       |
|__________________________________________________________________________| '''


print(bcolors.MAGENTA + banner + bcolors.RESET)
print('')
print(bcolors.GREEN + '                    Please select a option:                         ' + bcolors.RESET)
print(bcolors.GREEN + 'Port scan        [01]' + bcolors.RESET)
print(bcolors.GREEN + 'Nmap help        [02]' + bcolors.RESET)
print(bcolors.GREEN + 'Exit             [03]' + bcolors.RESET)
print(bcolors.GREEN + 'URL-Scan         [04]' + bcolors.RESET)
print(bcolors.GREEN + 'intense-scan Plus[05]' + bcolors.RESET)
print(bcolors.GREEN + 'Regular-scan     [06]' + bcolors.RESET)
print(bcolors.GREEN + 'Ping-scan        [07]' + bcolors.RESET)



user_input = input()

if user_input == '01':
  user_input2 = input(bcolors.GREEN + 'Please enter ip-adress: ' + bcolors.RESET)
  try:
    os.system('nmap -v -sn ' + user_input2)
  except ModuleNotFoundError:
    print(bcolors.RED + f'Please use the installer before you run this code' + bcolors.RESET)


if user_input == '1':
  user_input2 = input(bcolors.GREEN + 'Please enter ip-adress: ' + bcolors.RESET)
  try:
    os.system('nmap -v -sn ' + user_input2)
  except ModuleNotFoundError:
    print(bcolors.RED + f'Please use the installer before you run this code' + bcolors.RESET)


if user_input == '02':
  try:
    os.system('nmap --help')
  except ModuleNotFoundError:
    print(bcolors.RED + f'Please use the installer before you run this code' + bcolors.RESET)


if user_input == '2':
  try:
    os.system('nmap --help')
  except ModuleNotFoundError:
    print(bcolors.RED + f'Please use the installer before you run this code' + bcolors.RESET)


if user_input == '03':
  os.system('sudo python3 run.py')


if user_input == '3':
  os.system('sudo python3 run.py')


if user_input == '04':
  user_input3 = input(bcolors.GREEN + 'Please enter URL: ' + bcolors.RESET)
  try:
    os.system('nmap -v -A ' + user_input3)
    os.system('sudo python3 KittyyMap.py')
  except ModuleNotFoundError:
    print(bcolors.RED + f'Please use the Installer before you run this code.' + bcolors.RESET)


if user_input == '4':
  user_input3 = input(bcolors.GREEN + 'Please enter URL: ' + bcolors.RESET)
  try:
    os.system('nmap -v -A ' + user_input3)
    os.system('sudo python3 KittyyMap.py')
  except ModuleNotFoundError:
    print('Please use the Installer before you run this code.')



if user_input == '05':
  user_input4 = input(bcolors.GREEN + 'Please enter the IP-adress to be scanned: ' + bcolors.RESET)
  try:
    os.system('namp -sS -sU -T4 -A -v ' + user_input4)
    print(bcolors.GREEN + '+[+[+FINISHED]+]+' + bcolors.RESET)
    os.system('sudo python3 run.py')
  except ModuleNotFoundError:
    print(bcolors.RED + f'Please use the Installer before yourun this code.' + bcolors.RESET)


if user_input == '5':
  user_input4 = input(bcolors.GREEN + 'Please enter the IP-adress to be scanned: ' + bcolors.RESET)
  try:
    os.system('namp -sS -sU -T4 -A -v ' + user_input4)
    print(bcolors.GREEN + '+[+[+FINISHED]+]+' + bcolors.RESET)
    os.system('sudo python3 run.py')
  except ModuleNotFoundError:
    print(bcolors.RED + f'Please use the Installer before yourun this code.' + bcolors.RESET)




if user_input == '06':
  try:
    user_input5 = input(bcolors.GREEN + 'Please enter IP-adress to be scanned: ' + bcolors.RESET)
    os.system('nmap ' + user_input5)
  except ModuleNotFoundError:
    print(bcolors.RED + f'Please use the Installer before you run this code.' + bcolors.RESET)




if user_input == '6':
  try:
    user_input5 = input(bcolors.GREEN + 'Please enter IP-adress to be scanned: ' + bcolors.RESET)
    os.system('nmap ' + user_input5)
  except ModuleNotFoundError:
    print(bcolors.RED + f'Please use the Installer before you run this code.' + bcolors.RESET)


if user_input == '07':
  try:
    print(bcolors.GREEN + '+[+[+Ping-scan+]+]+')
    user_input6 = input(bcolors.GREEN + 'Please enter IP-adress to be scanned: ' + bcolors.RESET)
    os.system('nmap -sn ' + user_input6)
  except ModuleNotFoundError:
    print(bcolors.RED + f'Please use the installer before you run this code.' + bcolors.RESET)


if user_input == '7':
  try:
    print(bcolors.GREEN + '+[+[+Ping-scan+]+]+')
    user_input6 = input(bcolors.GREEN + 'Please enter IP-adress to be scanned: ' + bcolors.RESET)
    os.system('nmap -sn ' + user_input6)
  except ModuleNotFoundError:
    print(bcolors.RED + f'Please use the installer before you run this code.' + bcolors.RESET)
