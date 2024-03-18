#create a tcp server with ssl encryption 
import socket
import ssl

def create_tcp_server(host, port):
    #create a tcp socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #bind the socket to the host and port
    sock.bind((host, port))
    #listen for incoming connections
    sock.listen(5)
    #create a context for SSL
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    #load the certificate and key
    context.load_cert_chain('server.crt', 'server.key')
    #wrap the socket with SSL
    ssl_sock = context.wrap_socket(sock, server_side=True)
    return ssl_sock
