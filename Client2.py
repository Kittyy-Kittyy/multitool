import socket

class ChatClient:
    def __init__(self):
        self.password = "kittyycat1"  # You can change this
        self.locked = True
        self.server_ip = None
        self.client_socket = None

    def lock_chat(self):
        # Ask for password
        user_password = input("Enter password to access chat: ")
        if user_password == self.password:
            self.locked = False
            self.connect_to_server()
        else:
            print("Access Denied: Incorrect Password")
            exit()

    def connect_to_server(self):
        if not self.locked:
            self.server_ip = input("Enter the IP address of the server: ")
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                self.client_socket.connect((self.server_ip, 12345))
                print("Connected to server.")
            except Exception as e:
                print(f"Connection Error: Failed to connect to server: {e}")
                exit()

    def send_message(self):
        if not self.locked:
            while True:
                message = input("You: ")
                if message:
                    self.client_socket.send(message.encode())  # Send message to the server

                    # Receive reply from server
                    try:
                        reply = self.client_socket.recv(1024).decode()
                        if reply:
                            print(f"Server: {reply}")
                        else:
                            print("Disconnected from server.")
                            self.client_socket.close()
                            break
                    except:
                        print("Error receiving reply.")
                        break

# Main function to start the chat client
if __name__ == "__main__":
    app = ChatClient()
    app.lock_chat()
    app.send_message()
