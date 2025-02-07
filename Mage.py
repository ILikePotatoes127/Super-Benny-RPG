#Mage
from Player import *
class Mage():
    player_class = "Mage"
    skills = ["Fireball"]
    #Skills ["Fireball", "Lightning Bolt", "Heal", "Magic Defense", "Magice Missile", "Cone of Frost", "Water Elemental"]

    def __init__(self, stats):
        self.stats = stats
        
    def printStats(self):
        print(Mage.player_class)
        self.stats.printStats()
        print(Mage.skills)
