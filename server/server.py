#First run server, then client.
#When client is ran, server gets a message from it
#and sends a message back.
#After client gets the server message, the client closes.

import socketserver

class TcpServer(socketserver.ThreadingTCPServer):
    '''Activate server'''
    allow_reuse_address = True

class TcpServerHandler(socketserver.BaseRequestHandler):
    '''Server handler. Useless without TcpServer class'''
    def handle(self):
        '''Handles input and output'''
        try:
            data = self.request.recv(1024).decode('UTF-8')
            print(data)
            self.request.sendall(bytes("An hello from the server!", 'UTF-8'))
        except Exception as e:
            print(e)

#execute code
server = TcpServer(('127.0.0.1', 4343), TcpServerHandler)
server.serve_forever()
