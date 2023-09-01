import socket

# get host IPv4 address
HOST = 'localhost'

# Ports numbers < 1024 are 'well-known ports' (standard services associated with them)
# 1024 > and < 65,535 are 'unregistered' or 'dynamic'
PORT = 9999

# address family designates type of addresses socket can communicate with
# AF_INET for IPv4 addresses, using TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind((HOST, PORT))

# 5 unaccepted connections allowed before rejecting new connections
server.listen(5)


while True:
    # server socket accepts connections
    # communication socket allows communication between client and server
    communication_socket, address = server.accept()
    print(f"Connected to {address}")

    # receive message from client
    message = communication_socket.recv(1024).decode('utf-8') # 1024 byte message, decode byte stream
    print(f"MESSAGE: {message}")
    # send message back to client
    communication_socket.send(f"Message received".encode('utf-8'))
    communication_socket.close()

    print(f"Connection with {address} ended")