# Import socket module
import socket
from threading import Thread


def receive():
    while True:
            msg = client_socket.recv(1024)
            break

def send(event=None):
    msg = my_msg.get()
    client_socket.send(msg)
    client_socket.close()


client_socket = socket.socket()
port = 12345
client_socket.connect(('127.0.0.1', port))

receive_thread = Thread(target=receive)
receive_thread.start()

# client_socket.close()
