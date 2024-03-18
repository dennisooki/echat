import socket
import ssl
import threading

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = {}  # dictionary to store client connections and usernames

    def create_ssl_server(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.listen(1)
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain('server.crt', 'server.key')
        self.ssl_sock = context.wrap_socket(sock, server_side=True)

    def broadcast(self, message):
        for conn in self.clients:
            conn.send(message.encode('utf-8'))

    def handle_client(self, conn, addr):
        username = conn.recv(1024).decode('utf-8')  # receive the username from the client
        self.clients[conn] = username
        print(f"Client connected: {addr}, Username: {username}")
        while True:
            msg = conn.recv(1024).decode('utf-8')
            if not msg:
                break
            print(f"Received from {username}:", msg)
            self.broadcast(msg)  # broadcast the message to all clients
        del self.clients[conn]  # remove the client from the list when they disconnect
        self.broadcast(f"SERVER: {username} has left")  # notify all clients that the user has left

    def start(self):
        self.create_ssl_server()
        print("Server started, waiting for connection...")
        while True:
            conn, addr = self.ssl_sock.accept()
            threading.Thread(target=self.handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    server = Server('localhost', 12345)
    server.start()







