# Import socket module
import socket

# setting client socket
client_socket = socket.socket()
# sets port
port = 12346
# connects client to ip address and port
client_socket.connect(('127.0.0.1', port))
# sets whatever is received by client socket to variable called greeting
greeting = client_socket.recv(1024)
print greeting
# loops until it fails
while True:
    # user needs to put in name and message
    name = raw_input ("Please enter your name")
    chat = raw_input("Begin Chat!")
    # socket sends name and chat inputs
    client_socket.send(name)
    client_socket.send(chat)
    # sets whatever socket receives as "response" variable
    response = client_socket.recv(1024)
    # prints response variable on client side
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
