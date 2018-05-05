
'''
Leslie Wilson
functiontest.py
May 5, 2018
'''


class Chat(object):
    '''
    This object initiates chat between two clients
    '''

    def __init__(self, clients):
        # initiaties clients from clients array
        self.clients = clients
        # sends the message(can be input, automated message whatever)
    def broadcast(self, msg):
        for client in self.clients:
            client.send(msg)
        # initiates chat, sets
    def two_person_chat(self):
        greeting = "hello, welcome to chat, at any point type quit if you would like to end convo. please type your name"
        self.broadcast(greeting)
        # sets as empty so it can receive and save the raw inputs
        client0msg = ""
        client1msg = ""
        client0name = self.clients[0].recv(1028)
        client1name = self.clients[1].recv(1028)
        self.broadcast("hello {}, and {}, let's begin chat!".format(client0name, client1name))
        while True:
            if client0msg == "quit" or client1msg == "quit":
                self.broadcast("the chat is ending, goodbye!")
                break
            # makes connection between when chat program receives message
            # from first and second user in clients array
            client0msg = self.clients[0].recv(1028)
            client1msg = self.clients[1].recv(1028)

            self.broadcast("{}: ".format(client0name) + client0msg + "\n{}: ".format(client1name) + client1msg)

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
