#Darklord Benny

from Player import *
class Darklord():
    player_class = "Darklord"
    skills = ["Fireball"]
    #Skills ["Skeleton Minion", "Skull Blast", "Lifesteal", "Curse", "Meteor"]

    def __init__(self, stats):
        self.stats = stats
    
    def printStats(self):
        print(Darklord.player_class)
        self.stats.printStats()
        print(Darklord.skills)