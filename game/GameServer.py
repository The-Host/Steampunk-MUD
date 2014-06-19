import server


class GameServer(server.BaseServer):
    def __init__(self, address='', port=7777, idle_timeout=300):
        super().__init__(address, port, idle_timeout)

    def on_connect(self, client):
        super().on_connect(client)
        client.send('Welcome to the MUD, {}.\n'.format(client.addrport()))

    def on_disconnect(self, client):
        super().on_disconnect(client)
        self.broadcast('{} left\n.'.format(client.addrport()))

    def process_client(self, client):
        pass


if __name__ == '__main__':
    mud = GameServer()
    mud.start()
