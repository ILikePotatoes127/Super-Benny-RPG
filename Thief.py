#Thief

from Player import *
class Thief():
    player_class = "Thief"
    skills = ["Fireball"]
    #Skills ["Steal", "Shank", "Back stab (Bleed)", "Lacerate (Slow)", "Smoke Bomb (Increased evasion)", "Blunder Bust"]

    def __init__(self, stats):
        self.stats = stats
    
    def printStats(self):
        print("Class: "+Thief.player_class)
        print("Skills: "+" ".join(Thief.skills))
        self.stats.printStats()