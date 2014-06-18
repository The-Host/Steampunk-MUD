#First run server, then client.
#When client is ran, server gets a message from it
#and sends a message back.
#After client gets the server message, the client closes.

import socket

data = "Hello from the client!" #DAta to be sent to server

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket object

sock.connect(('127.0.0.1', 4343)) #must be the address and port of server
sock.send(bytes(data, 'UTF-8')) #sending data in form of bytes

result = sock.recv(1024).decode('UTF-8') #data that the server sent to client
print(result)

sock.close() #end socket object
