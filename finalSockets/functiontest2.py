

class Chat(object):
    def __init__(self, clients):
        self.clients = clients

    def broadcast(self, msg):
        for client in self.clients:
            client.send(msg)

    def two_person_chat(self):
        msg = "hello, welcome to chat, at any point type quit if you would like to end convo"
        self.broadcast(msg)
        client0msg = ""
        client1msg = ""
        while client0msg != "quit" and client1msg != "quit":
            client0msg = self.clients[0].recv(1028)
            client1msg = self.clients[1].recv(1028)
            self.broadcast("{name}: " + client0msg + "{name}: " + client1msg)

def testchat(clients):
    chat = Chat(clients)
    chat.two_person_chat()





# ~~~~~~~~~~~~~HERE ARE SOME THINGS I TRIED THAT DID NOT WORK, OR ALMOST WORKED~~~~~~~
# # client functions
# def receive():
#     while True:
#             msg = client_socket.recv(1024)
#             break
#
# def send(event=None):
#     msg = my_msg.get()
#     client_socket.send(msg)
#     client_socket.close()
#
# # server functions
#
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
