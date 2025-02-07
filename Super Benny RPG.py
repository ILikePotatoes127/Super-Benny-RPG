from Mage import *
from Thief import *
from Warrior import *
from Darklord import *


import math


class_stats = {
    "Mage":[50,5,5,20,15,5,100,[],Mage],
    "Thief":[75, 15, 20, 35, 30, 25, 65, [],Thief],
    "Warrior":[100, 25, 35, 15, 5, 5, 35, [],Warrior],
    "Darklord":[80, 20, 25, 20, 5, 5, 70, [],Darklord]
}

def main():
    print("Welcome to Super Benny RPG!!")

    player = class_select()

    player.printStats()

def class_select():
    print("Choose your class (Type in one of the following to choose): ")
    print("Mage, Thief, Warrior, Darklord")
    rpg_class = input()

    if rpg_class in class_stats:
        c = class_stats[rpg_class]
        stats = Player(c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7])
        class_constructor = c[8]
        player = class_constructor(stats)
        return player
    else:
        return class_select()



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

if __name__ == "__main__":
    main()
    #stats = Player(10,20,10,10,10,10,10,10)
    #player = Mage(stats)
    #player.printStats()