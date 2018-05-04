

def handle_client(client):
    name = client.recv(1024)
    welcome = "welcome %s! if you want to quit type {quit} to exit. " %name

    client.send(welcome)
    msg = "%s has joind the chat" % name
    broadcast(msg)
    clients[c] = name
    while True:
        msg = client.recv(1024)
        break
        # if msg != ({quit}):
        #
        # )
