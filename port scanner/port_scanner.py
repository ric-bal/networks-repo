import socket
import threading
from queue import Queue

TARGET = 'localhost'
queue = Queue()
open_ports = []


def portscan(port):
    try:
        # IPv4 addresses, using TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((TARGET, port))
        return True
    except:
        return False


def fill_queue(port_list):
    for port in port_list:
        queue.put(port)


# worker function threads will be using
def worker():
    while not queue.empty():
        # get port from queue (FIFO)
        port = queue.get()
        if portscan(port):
            print(f"Port {port} is open")
            open_ports.append(port)


# check standardised ports (0 - 1023)
port_list = range(1, 1024)
fill_queue(port_list)

thread_list = []
# 500 threads
for t in range(500):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

# start each thread
for thread in thread_list:
    thread.start()

# wait until all threads are done
for thread in thread_list:
    thread.join()

print(f"Open Ports: {open_ports}")

