#Darklord Benny

from Player import *
class Darklord():
    player_class = "Darklord"
    skills = ["Fireball"]
    #Skills ["Skeleton Minion", "Skull Blast", "Lifesteal", "Curse", "Meteor"]

    def __init__(self, stats):
        self.stats = stats
    
    def printStats(self):
        print("Class: "+Darklord.player_class)
        print("Skills: "+" ".join(Darklord.skills))
        self.stats.printStats()