#Player


class Player():
    def __init__(self, health, defense, attack, speed, evasion, luck, mana, items):
        self.health = health
        self.defense = defense
        self.attack = attack
        self.speed = speed
        self.evasion = evasion
        self.luck = luck 
        self.mana = mana
        self.items = items 
    
    def printStats(self):
        print(self.health)
        print(self.defense)
        print(self.attack)
        print(self.speed)
        print(self.evasion)
        print(self.luck)
        print(self.mana)
        print(self.items)
        