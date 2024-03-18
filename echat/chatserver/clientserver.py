import socket
import ssl
import threading

def create_ssl_server(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(1)
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain('server.crt', 'server.key')
    ssl_sock = context.wrap_socket(sock, server_side=True)
    return ssl_sock

def create_ssl_client(server_host, server_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_verify_locations('server.crt')
    ssl_sock = context.wrap_socket(sock, server_hostname=server_host)
    ssl_sock.connect((server_host, server_port))
    return ssl_sock

def handle_client(conn):
    while True:
        msg = conn.recv(1024).decode('utf-8')
        if not msg:
            break
        print("Received:", msg)

def start_server(host, port):
    server = create_ssl_server(host, port)
    print("Server started, waiting for connection...")
    while True:
        conn, addr = server.accept()
        print("Client connected:", addr)
        threading.Thread(target=handle_client, args=(conn,)).start()


def start_client(host, port):
    client = create_ssl_client(host, port)
    print("Connected to server.")
    while True:
        msg = input("Enter message: ")
        client.send(msg.encode('utf-8'))

if __name__ == "__main__":
    choice = input("Start server or client? (s/c): ")
    if choice.lower() == 's':
        start_server('localhost', 12345)
    elif choice.lower() == 'c':
        start_client('localhost', 12345)
