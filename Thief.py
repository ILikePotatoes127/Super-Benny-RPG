#Thief

from Player import *
class Thief():
    player_class = "Thief"
    skills = ["Fireball"]
    #Skills ["Steal", "Shank", "Back stab (Bleed)", "Lacerate (Slow)", "Smoke Bomb (Increased evasion)", "Blunder Bust"]

    def __init__(self, stats):
        self.stats = stats