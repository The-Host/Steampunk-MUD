# First run server, then client. When client is ran, server gets a
# message from it and sends a message back.After client gets the
# server message, the client closes.

import socket


if __name__ == '__main__':
    # Data to be sent to server
    data = "Hello from the client!"

    # create socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # must be the address and port of server
    sock.connect(('127.0.0.1', 4343))

    # sending data in form of bytes
    sock.send(bytes(data, 'UTF-8'))

    # data that the server sent to client
    result = sock.recv(1024).decode('UTF-8')
    print(result)

    # end socket object
    sock.close()
