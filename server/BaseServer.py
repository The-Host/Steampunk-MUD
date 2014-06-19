from libs.miniboa import TelnetServer


class BaseServer(object):
    """Base class for a telnet server."""

    def __init__(self, address='', port=7777, idle_timeout=300):
        """Initializer for `BaseServer`.

        :param address: bytes Host address. For a local-only server
        use 127.0.0.1 and for an externally visible server use ''
        or your outgoing IP address (ex. 192.168.1.3).

        :param port: int Port on which to listen for incoming
        connections.

        :param idle_timeout: int How long to wait before kicking idle
        clients (in minutes).

        """
        self.clients = []
        self.running = False

        self.address = address
        self.port = port
        self.idle_timeout = idle_timeout
        self.timeout = 0.05

    def broadcast(self, msg):
        """Sends a message, `msg`, to all clients connected to the
        server.

        :param msg: The message to send.

        """
        for client in self.clients:
            client.send(msg)

    def on_connect(self, client):
        """Called when a new client connects to the server.

        :param client: The client connecting to the server.

        """
        print("++ Opened connection to {}".format(client.addrport()))
        self.clients.append(client)

    def on_disconnect(self, client):
        """Called when a client disconnects from the server.

        :param client: The client disconnecting from the server.

        """
        print("-- Lost connection to {}".format(client.addrport()))
        self.clients.remove(client)

    def kick_idle(self):
        """Kicks all clients that have been idle longer than
        `idle_timeout` minutes.

        """
        for client in self.clients:
            if client.idle() > self.idle_timeout:
                print(
                    '-- Kicking idle client from {}'.format(client.addrport())
                )
                client.active = False

    def process_clients(self):
        """Iterates through all currently connected clients and
        calls `process_client` once for each connected client.

        """
        for client in self.clients:
            if client.active and client.cmd_ready:
                self.process_client(client)

    def process_client(self, client):
        """Not implemented here. Should be overridden in subclasses.

        :param client: The client to be processed.

        """
        pass

    def start(self):
        """Starts the server."""

        server = TelnetServer(
            port=self.port,
            address=self.address,
            on_connect=self.on_connect,
            on_disconnect=self.on_disconnect,
            timeout=self.timeout
        )

        print(">> Listening for connections on port {}.".format(self.port))

        self.running = True

        while self.running:
            server.poll()
            self.kick_idle()
            self.process_clients()

        print(">> Server shutdown.")


if __name__ == '__main__':
    game_server = BaseServer()
    game_server.start()
