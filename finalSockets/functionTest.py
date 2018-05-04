

# client functions
def receive():
    while True:
            msg = client_socket.recv(1024)
            break

def send(event=None):
    msg = my_msg.get()
    client_socket.send(msg)
    client_socket.close()

# server functions

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


    # can you help me pull it down- i don't want to make anymore mistakes. i don't think i can do this. im spinning my wheels- can we pull down the origional and go through it together. 
