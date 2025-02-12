#Player
from Enemy import *
class Player():
    def __init__(self, health, defense, attack, speed, evasion, luck, mana, gold, items):
        self.health = health
        self.defense = defense
        self.attack = attack
        self.speed = speed
        self.evasion = evasion
        self.luck = luck 
        self.mana = mana
        self.gold = gold
        self.items = items 
    
    def printStats(self):
        print("Health: "+str(self.health))
        print("Defense: "+str(self.defense))
        print("Attack: "+str(self.attack))
        print("Speed: "+str(self.speed))
        print("Evasion: "+str(self.evasion))
        print("Luck: "+str(self.luck))
        print("Mana: "+str(self.mana))
        print("Gold: "+str(self.gold))
        for item in self.items:
            print(f"{item}: {self.items[item]}")
    
    def attack_enemy(self, enemy:Enemy):
        enemy.health -= max(0,self.attack - enemy.defense)
    
    def get_health(self):
        return self.health