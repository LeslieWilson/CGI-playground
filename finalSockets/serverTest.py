
'''
Leslie Wilson
serverTest.py
May 5, 2018
'''
# imports socket module
import socket
# imports threading module
from threading import Thread
# imports functiontest2 from my files
from functiontest2 import *


def comboInitiate():
    '''
    Function sets server socket, binds it to ip address, accepts 2 clients into
    an array. Starts a new Thread that initiaties chat between two accepted
    clients.

    '''

    port=12342
    server_socket = socket.socket()
    server_socket.bind(('', port))
    print "socket binded to %s" %(port)
    while True:
        clients = []
        server_socket.listen(2)
        print "waiting for connection..."
        # double set, clientsocket and address. .accept method takes a connect and extrats the clientsocket id(portnumber?) and address
        (clientsocket, addr) = server_socket.accept()
        clients.append(clientsocket)
        (clientsocket, addr) = server_socket.accept()
        # taking port number and appending to array clients, you'll have multiple users
        clients.append(clientsocket)
        # sending arguments (from clients array) to target, which is the testchat function in this case.
        START_CHAT = Thread(target=testchat, args = (clients,))
        START_CHAT.start()


comboInitiate()


# ~~~~~~~~~~~~~HERE ARE SOME THINGS I TRIED THAT DID NOT WORK, OR ALMOST WORKED~~~~~~~

# # name of function
#    chat = newfunction[]
#    # send reversed fortune back to client
#    c.send(chat)
#    msg = "%s has joind the chat!" % name
#    clients[c] = name
#         while True:
#             msg = c.recv(1024)
#             if msg != "quit":
#                 return(msg, name=": ")

# ************************************************************************
# def accept_incoming_connections():
#     while True:
#        c, addr = s.accept()
#        print 'Got connection from', addr
#        c.send("greetings!" + "type your name and press enter")
#        addresses[c] = addr
#        Thread(target=handle_client, args=(c,)).start()
#
# def broadcast(msg):
#     for sock in clients:
#         sock.send(msg)
#
# def handle_client(c):
#     name = c.recv(1024)
#     msg = "%s has joing the chat" % name
#     broadcast(msg)
#     clients[c] = name
#     while True:
#         msg = c.recv(1024)
#         break
#
# clients = {}
# addresses = {}
#
# s = socket.socket()
# print "Socket successfully created"
# port = 12345
# s.bind(('', port))
# print "socket binded to %s" %(port)
#
# if __name__ == "__main__":
#     s.listen(5)
#     print "waiting for connection..."
#     ACCEPT_THREAD = Thread(target=accept_incoming_connections)
#     ACCEPT_THREAD.start()
#     ACCEPT_THREAD.join()
#     s.close()
