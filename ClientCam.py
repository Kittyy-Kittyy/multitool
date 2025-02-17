import cv2
import socket
import struct
import pickle
from tkinter import ttk  # Es sollte "ttk" anstatt "tkk" sein
import tkinter as tk

# Client Start with Button and Labels

root = tk.Tk()

def Button_Sonde():
    start_client()

B1 = tk.Button(root, text='Connect to Server.', command=Button_Sonde)
B1.pack()  

L1 = tk.Label(root, text='You are connect to Server.')
L1.pack()  

def start_client():
    # Initialisiere den Socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('IP-DER-SONDE', 12345))

    data = b""
    payload_size = struct.calcsize("L")

    while True:
        # Empfang von Nachrichten vom Server
        while len(data) < payload_size:
            packet = client_socket.recv(4096)
            if not packet:
                break
            data += packet

        if len(data) < payload_size:
            break

        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("L", packed_msg_size)[0]

        while len(data) < msg_size:
            data += client_socket.recv(4096)

        frame_data = data[:msg_size]
        data = data[msg_size:]

        # Deserialisiere das Frame
        frame = pickle.loads(frame_data)

        # Zeige das Frame an
        cv2.imshow('Frame vom Server', frame)
        if cv2.waitKey(1) == 27:
            break

    client_socket.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    root.mainloop()