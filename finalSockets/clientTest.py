# Import socket module
import socket
from threading import Thread
from functionTest import *

# call = accept_incoming_connections()
# client_socket.send(call)

# print client_socket.recv(1024)

def receive():
    while True:
        try:
            msg = client_socket.recv(1024)
            print msg
        except OSError:
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

client_socket.close()
