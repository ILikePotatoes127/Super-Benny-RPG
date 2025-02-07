from Mage import *
from Thief import *
from Warrior import *
from Darklord import *


enemy_data = {
    "type":"Goblin",
    "health": 10,
    "defense":10,
    "attack":10,
    "speed":10,
    "evasion":10,
    "luck":10,
    "mana":10,
    "items":10,
    "skills":["Stab"],
}
'''
skills = {
    "stab":stab,
    "stab":stab,
    "stab":stab,
    "stab":stab,
    "stab":stab,
    "stab":stab,
    "stab":stab,
    "stab":stab,
    "stab":stab,
    "stab":stab,
    "stab":stab,
    "stab":stab
}

def start():
    print("Welcome to Super Benny RPG!!")
    
    class_select()

def class_select():
    global player_data
    print("Choose your class (Type in one of the following to choose): ")
    print("Mage, Thief, Warrior, Darklord")
    
    rpg_class = input()

    if rpg_class == "Mage":
        player_data["class"] = "Mage"
        player_data["health"] = 10
        player_data["defense"] = 10
        player_data["attack"] = 10
        player_data["speed"] = 10
        player_data["evasion"] = 10
        player_data["luck"] = 10
        player_data["mana"] = 10
        player_data["items"] = 10
        player_data["skills"] = ["Fireball"]
        #Skills ["Fireball", "Lightning Bolt", "Heal", "Magic Defense", "Magice Missile", "Cone of Frost", "Water Elemental"]
        
    elif rpg_class == "Thief":
        player_data["class"] = "Thief"
        player_data["health"] = 10
        player_data["defense"] = 10
        player_data["attack"] = 10
        player_data["speed"] = 10
        player_data["evasion"] = 10
        player_data["luck"] = 10
        player_data["mana"] = 10
        player_data["items"] = 10
        player_data["skills"] = ["Steal"]
        #Skills ["Steal", "Shank", "Back stab (Bleed)", "Lacerate (Slow)", "Smoke Bomb (Increased evasion)", "Blunder Bust"]

    elif rpg_class == "Warrior":
        player_data["class"] = "Warrior"
        player_data["health"] = 10
        player_data["defense"] = 10
        player_data["attack"] = 10
        player_data["speed"] = 10
        player_data["evasion"] = 10
        player_data["luck"] = 10
        player_data["mana"] = 10
        player_data["items"] = 10
        player_data["skills"] = ["Great Slash"]
        #Skills ["Great Slash", "Shield Bash", "Armor Up (Defense increase)", "Warrior Cry"]

    elif rpg_class == "Darklord":
        player_data["class"] = "Darklord"
        player_data["health"] = 10
        player_data["defense"] = 10
        player_data["attack"] = 10
        player_data["speed"] = 10
        player_data["evasion"] = 10
        player_data["luck"] = 10
        player_data["mana"] = 10
        player_data["items"] = 10
        player_data["skills"] = ["Skeleton Minion"]
        #Skills ["Skeleton Minion", "Skull Blast", "Lifesteal", "Curse", "Meteor"]

    else:
        class_select()


def check_stats():
    print("Player Stats:")
    print("Class: " + player_data["class"])
    print("Health: " + player_data["health"])
    print("Defense: " + player_data["defense"])
    print("Attack: " + player_data["attack"])
    print("Speed: " + player_data["speed"])
    print("Evasion: " + player_data["evasion"])
    print("Luck: " + player_data["luck"])
    print("Mana: " + player_data["mana"])
    print("Skills: " + player_data["skills"])


def battle():
    enemy = "Goblin" #This will be random with random stats at some point
    print("You encounter a "+enemy+"! What do you do?")
    player_turn()
    enemy_turn()

def player_turn():
    print("(Attack, Skill, Item, Run)")
    move = True
    while move:
        choice = input()

        if choice=="Attack":
            attack()
        if choice=="Skill":
            skill()
        if choice=="Item":
            item()
        if choice=="Run":
            run()


def attack():
    enemy_data["health"]-=player_data["health"]

def skill():
    print("Choose a skill:")
    print(player_data["skills"])
    choice = input()
    if choice in player_data["skills"]:
        pass
    else:
        skill()

def item():
    pass

def run():
    pass

def enemy_turn():
    pass

def skeleton_minion():
    pass

#start()
'''

#if __name__ == "__main__":
stats = Player(10,20,10,10,10,10,10,10)
player = Mage(stats)
player.printStats()
player.stats.health = 50
player.printStats()