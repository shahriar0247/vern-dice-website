import socket
import time
server = socket.socket()        
print ("Socket successfully created")

port = 80
host_ip = '192.168.1.246'
server.connect((host_ip, port))
print ("Connected to the socket successfully ")

for i in range (6):
    print ((server.recv(500).decode()))

time.sleep(30)
