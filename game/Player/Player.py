class Player():

    def __init__(self, playerHealth, playerMana):
        self.playerHealth = playerHealth
        self.playerMana = playerMana

    def getHealth(self):
    	"""Returns current player health"""
        return self.playerHealth

    def getMana(self):
    	"""Returns current player mana"""
        return self.playerMana

    def setHealth(self, value):
    	"""Sets new player health"""
        self.playerHealth = value

    def setMana(self, value):
    	"""Sets new player mana"""
        self.playerMana = value
