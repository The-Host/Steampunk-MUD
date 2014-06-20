#! /usr/local/bin/env python3

"""File used to start server."""

import game


if __name__ == '__main__':
    game_server = game.GameServer()
    game_server.start()
