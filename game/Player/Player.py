class Player:
    def __init__(self, player_health, player_mana):
        self.__health = player_health
        self.__mana = player_mana

    @property
    def health(self):
        """Returns current player health"""
        return self.__health

    @property
    def mana(self):
        """Returns current player mana"""
        return self.__health

    @health.setter
    def health(self, value):
        """Sets new player health"""
        self.__health = value

    @mana.setter
    def mana(self, value):
        """Sets new player mana"""
        self.__mana = value
