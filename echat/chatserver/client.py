
import socket
import ssl
from tkinter import *


class Client:
    def __init__(self, username, host, port):
        self.username = username
        self.host = host
        self.port = port
        

    def create_ssl_client(self, server_host, server_port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        context.load_verify_locations('echat/chatserver/server.crt')
        ssl_sock = context.wrap_socket(sock, server_hostname=server_host)
        ssl_sock.connect((server_host, server_port))
        return ssl_sock

    def connect(self):
        print(f"Attempting to connect to {self.host}:{self.port}")
        try:
            self.client = self.create_ssl_client(self.host, self.port)
            self.client.send(self.username.encode('utf-8'))  # send the username
            print("Connected to server.")
            
        except Exception as e:
            print(f"Error: {e}")
            print("Please check if the server is running and the host and port are correct.")

    def disconnect(self):
        self.client.send("SERVER: {} has left".format(self.username).encode('utf-8'))
        self.client.close()

    def receive_messages(self, chat_box):
        while True:
            msg = self.client.recv(1024).decode('utf-8')
            if not msg:
                break
            chat_box['state'] = 'normal'  # Enable the text box
            chat_box.insert(END, f"{msg}\n")
            chat_box['state'] = 'disabled'  # Disable the text box again

    def send_message(self, message):
        msg_with_username = f"{self.username}: {message}"
        self.client.send(msg_with_username.encode('utf-8'))
   
if __name__ == "__main__":
    username = input("Enter your username: ")
    client = Client(username, 'localhost', 12345)
    client.connect()
