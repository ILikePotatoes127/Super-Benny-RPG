from Mage import *
from Thief import *
from Warrior import *
from Darklord import *

from Bat_Benny import *

import math


#initiation for py game so that we can call any library stuff
import pygame
import sys
import random
pygame.init()

#Canvas for the window size in pygame, can be readjusted later, they're constants for now
#We put this in MAIN for it to work
#We also define black to draw the background black
WIDTH = 800
HEIGHT = 500

#Colors for background and textbox
BLACK = (0, 0, 0)
WHITE = (255,255,255)
#COLORS = (R,G,B)





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


def wait_for_user_input():
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Yo")
                pygame.display.flip()
                return 
            pass
        pass
    pass
#Text on screen because I am stupid, we can hopefully copy and paste this stuff
class text_box():
    def __init__(self, text):
        self.text = text
    def draw_text_box(screen):
        pygame.draw.rect(screen,WHITE,(25,300,750,150),2)
    def draw_text(screen,text):
        font = pygame.font.Font(None, 36)
        text = font.render(str(text), True, WHITE)
        screen.blit(text,(40,325))
    pass

#Screen.blit for what we're drawing on top of text box and text is a string and where we're putting it
def battle_pass_through_text(screen,text,x,y):
    font = pygame.font.Font(None, 36)
    text = font.render(str(text), True, WHITE)
    screen.blit(text,(x,y))

#Contains Core Game Loop
#Sorry Daniel I have to change a bit of this to show some stuff properly cause pygame needs to run within this :)

def main():
    #Showing the game window itself
    screen = pygame.display.set_mode((WIDTH,HEIGHT))

    #Title being visible for the game 
    pygame.display.set_caption("Super Benny RPG")

    enemy_stat = Enemy(10,10,10,10,10,10,10)
    bat = Bat_Benny(enemy_stat)


    #Clock object in order to set the frame rate
    clock = pygame.time.Clock()
    #Loop for the game to work
    
    #Intro
    intro(screen,clock)
    
    while True:
        
        screen.fill(BLACK)
        text_box.draw_text_box(screen)
        
        for event in pygame.event.get():
            #This is basically going to handle any player input, right now it only checks for the X at the windows bar is pressed to exit
            #out the game
            if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("Is this thing on?")
                    text_box.draw_text(screen, "Hi!")
                if event.key == pygame.K_RIGHT:
                    battle_pass_through_text(screen,"It's my time to shine!", WIDTH/2, HEIGHT/2)
        #It's like godot with delta, 
        delta_time = clock.get_rawtime()
        #Updates display
        pygame.display.flip()
        #60ms per frame
        clock.tick(60)
        wait_for_user_input()
        print("It went too far")
                    


    intro()

    player = class_select()
    print()

    player.printStats()

    #While The Player is not Dead
    #enemy = enemy_select()
    #start the battle between player and enemy
    player.attack_enemy(bat)

    print(bat.stats.health)
    clock.tick(60)


#This is just gonna be a bunch of prints to tell players how the game works
#This is just getting text to display, it's a little weird but I'm working on it still
def intro(surface,timer):
    text_box.draw_text_box(surface)
    text_box.draw_text(surface,"Welcome to SUPER BENNY RPG!")
    timer.tick(60)
    pygame.display.flip()
    wait_for_user_input()
    

    surface.fill(BLACK)
    text_box.draw_text_box(surface)
    text_box.draw_text(surface,"Hi!")
    
    timer.tick(60)
    pygame.display.flip()
    wait_for_user_input()


#Checks if smth smth (I act don't know, I just see people do this all the time)
if __name__ == "__main__":
    main()