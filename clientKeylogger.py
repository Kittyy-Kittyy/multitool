import socket

# Server-IP abfragen
SERVER_IP = input("Bitte Server-IP eingeben: ")
PORT = 12345

def receive_keys(client_socket):
    """Empfängt gedrückte Tasten und zeigt sie an"""
    while True:
        try:
            key_data = client_socket.recv(1024).decode()
            if not key_data:
                break
            print(f"Taste empfangen: {key_data}")
        except:
            break

def start_client():
    """Startet den Client und verbindet sich mit dem Server"""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, PORT))

    receive_keys(client_socket)  # Wartet auf Tastendrücke vom Server

    client_socket.close()

if __name__ == "__main__":
    start_client()
