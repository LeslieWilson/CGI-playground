# Import socket module
import socket

client_socket = socket.socket()
port = 12348
client_socket.connect(('127.0.0.1', port))

greeting = client_socket.recv(1024)
print greeting
while True:
    chat = raw_input("what would you like to say?")
    client_socket.send(chat)
    response = client_socket.recv(1024)
    print response






# ~~~~~~~~~~~~~HERE ARE SOME THINGS I TRIED THAT DID NOT WORK, OR ALMOST WORKED~~~~~~~

# from threading import Thread
# from functionTest import *

# call = accept_incoming_connections()
# client_socket.send(call)

# print client_socket.recv(1024)

# def receive():
#     msg = client_socket.recv(1024)
#     print msg
#     name = raw_input()
#     client_socket.send(name)
#     new_person = client_socket.recv(1024)
#     print new_person
#
# def send(event=None):
#     msg = my_msg.get()
#     client_socket.send(msg)
#     client_socket.close()
#
# client_socket = socket.socket()
# port = 12349
# client_socket.connect(('127.0.0.1', port))
#
# receive_thread = Thread(target=receive)
# receive_thread.start()
#
# client_socket.close()
