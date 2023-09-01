import socket
import threading

HOST = 'localhost'
PORT = 9999

nickname = input("Choose a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


def receive():
    while True:
        try:
            # receive message from server
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                # send chosen nickname to server
                client.send(nickname.encode('ascii'))
            else:
                # print message received from server
                print(message)

        except Exception as e:
            print(e)
            print("An error ocurred")
            client.close()
            break


def write():
    while True:
        # client always prompted to write new message
        message = (f"{nickname}: {input('')}")
        client.send(message.encode('ascii'))


# allow writing and receiving to be processed at roughly the same time
receive_thread = threading.Thread(target=receive)
write_thread = threading.Thread(target=write)

receive_thread.start()
write_thread.start()