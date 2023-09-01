import threading
import socket

HOST = 'localhost'
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

# connected clients and associated user names
clients = []
nicknames = []


def broadcast(message):
    # send message to all client
    for client in clients:
        client.send((message.encode('ascii')))


def handle(client):
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            broadcast(message)
        except Exception as e:
            print(e)

            # if client disconnects, remove from list, end connection and break loop
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} has left the chat") # encoded in ascii char set
            nicknames.remove(nickname)
            break


def receive():
    while True:
        # accepts client attempting to connect
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        # send code 'NICK' to client, upon receiving will send nickname back
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Client nickname: {nickname}")
        broadcast(f"{nickname} has joined the chat")
        client.send("Connected to server".encode('ascii'))

        # handles clients with thraeds to process actions roughly at the same time
        thread = threading.Thread(target = handle, args=(client,)) # extra comma?
        thread.start() 


print("Server is listening...")
receive()