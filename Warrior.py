#Warrior

from Player import *
class Warrior():
    player_class = "Warrior"
    skills = ["Fireball"]
    #Skills ["Great Slash", "Shield Bash", "Armor Up (Defense increase)", "Warrior Cry"]

    def __init__(self, stats):
        self.stats = stats
    
    def printStats(self):
        print(Warrior.player_class)
        self.stats.printStats()
        print(Warrior.skills)