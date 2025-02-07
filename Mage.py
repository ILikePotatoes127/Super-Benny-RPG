#Mage
from Player import *
class Mage():
    player_class = "Mage"
    skills = ["Fireball"]

    def __init__(self, stats):
        self.stats = stats
        
    def printStats(self):
        print(1)
        print(self.stats.health)
        print(self.stats.defense)
        print(Mage.player_class)
