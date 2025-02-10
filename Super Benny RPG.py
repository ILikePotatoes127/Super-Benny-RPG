from Mage import *
from Thief import *
from Warrior import *
from Darklord import *

from Bat_Benny import *

import math

#Dictionary for enemy_select() function
#Arrays are filleed with character stats and their corresponding constructor
enemy_stats = {
    "Bat Benny":[],
    "Green Benny": [],
    "Red Benny": [],
    "Blue Benny": [],
    "Gold Benny": [],
    "Turbo Benny": [],
    "Paper Benny": [],
    "Evil Benny": [],
    "Karaoke Benny": []
}

#Dictionary for class_select() function
#Arrays are filled with character stats and their corresponding constructor
class_stats = {
    "Mage":[50,5,15,20,15,5,100,0, Mage],
    "Thief":[75, 15, 20, 35, 30, 25, 65, 0, Thief],
    "Warrior":[100, 25, 35, 15, 5, 5, 35, 0, Warrior],
    "Darklord":[80, 20, 25, 20, 5, 5, 70, 0, Darklord]
}

#Returns a player under a specific class depending on their input.
def class_select():
    #Dictionary that holds all item variants
    basic_items = {
        "Health Potion": 0,
        "Reinforcement Potion": 0,
        "Speed Potion": 0,
        "Strength Potion": 0
    }

    print("Choose your class (Type in one of the following to choose): ")
    print("Mage, Thief, Warrior, Darklord")
    rpg_class = input()

    if rpg_class in class_stats:
        c = class_stats[rpg_class]
        stats = Player(c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7], basic_items)
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
    print("(Attack, Skill, Item)")
    move = True
    while move:
        choice = input()

        if choice=="Attack":
            attack()
        if choice=="Skill":
            skill()
        if choice=="Item":
            item()


def attack():
    pass

def skill():
    pass

def item():
    pass

def enemy_turn():
    pass

def skeleton_minion():
    pass

#Contains Core Game Loop
def main():

    enemy_stat = Enemy(10,10,10,10,10,10,10)
    bat = Bat_Benny(enemy_stat)





    intro()

    player = class_select()
    print()

    player.printStats()

    #While The Player is not Dead
    #enemy = enemy_select()
    #start the battle between player and enemy
    player.attack_enemy(bat)

    print(bat.stats.health)

#This is just gonna be a bunch of prints to tell players how the game works
def intro():
    print("Welcome to Super Benny RPG!!")
    print()


#Checks if smth smth (I act don't know, I just see people do this all the time)
if __name__ == "__main__":
    main()