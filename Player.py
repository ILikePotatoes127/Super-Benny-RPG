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
        print("Health: "+str(self.health))
        print("Defense: "+str(self.defense))
        print("Attack: "+str(self.attack))
        print("Speed: "+str(self.speed))
        print("Evasion: "+str(self.evasion))
        print("Luck: "+str(self.luck))
        print("Mana: "+str(self.mana))
        for item in self.items:
            print(f"{item}: {self.items[item]}")
        