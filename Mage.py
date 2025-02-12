#Mage
from Player import *
class Mage():
    player_class = "Mage"
    skills = ["Fireball"]
    #Skills ["Fireball", "Lightning Bolt", "Heal", "Magic Defense", "Magice Missile", "Cone of Frost", "Water Elemental"]

    def __init__(self, stats):
        self.stats = stats
        
    def printStats(self):
        print("Class: "+Mage.player_class)
        print("Skills: "+" ".join(Mage.skills))
        self.stats.printStats()
    
    def attack_enemy(self, enemy:Enemy):
        print("You attack " + enemy.name)
        self.stats.attack_enemy(enemy.stats)
    
    #The one in player doesn't work - Miguel
    def get_health(self):
        return str(self.stats.health)
