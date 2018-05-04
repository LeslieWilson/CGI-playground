
import socket
from threading import Thread
# from functionTest import *

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
# Close the connection with the client

def accept_incoming_connections():
    while True:
       c, addr = s.accept()
       print 'Got connection from', addr
       c.send("greetings!" + "type your name and press enter")
       addresses[c] = addr
       Thread(target=handle_client, args=(c,)).start()

def broadcast(msg):
    for sock in clients:
        sock.send(msg)

def handle_client(c):
    name = c.recv(1024)
    msg = "%s has joing the chat" % name
    broadcast(msg)
    clients[c] = name
    while True:
        msg = c.recv(1024)
        break

clients = {}
addresses = {}

s = socket.socket()
print "Socket successfully created"
port = 12345
s.bind(('', port))
print "socket binded to %s" %(port)

if __name__ == "__main__":
    s.listen(5)
    print "waiting for connection..."
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    s.close()

# can you like help me set it up to be more simple im kind of confusing myself
