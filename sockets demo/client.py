import socket

# IP of server, same as host because server run on same computer
# if connecting through internet, use public IP address
HOST = 'localhost'
PORT = 9999

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send("Hello server".encode('utf-8'))

# print message received from server
print(socket.recv(1024).decode('utf-8'))