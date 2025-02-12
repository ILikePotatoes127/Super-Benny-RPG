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
#Edited this to display in pygame, commented out code that might make the game hang
def class_select():
    #Dictionary that holds all item variants
    basic_items = {
        "Health Potion": 0,
        "Reinforcement Potion": 0,
        "Speed Potion": 0,
        "Strength Potion": 0
    }
    
    #print("Choose your class (Type in one of the following to choose): ")
    #print("Mage, Thief, Warrior, Darklord")
    #rpg_class = input()
    rpg_class = None
    #Horrifying loop
    while rpg_class == None:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #So scuffed, press S for mage, d for Thief, h for Warrior and j for Darklord, we can fix this later
            if event.key == pygame.K_s:
                rpg_class = "Mage"
                break
            if event.key == pygame.K_d:
                break
            if event.key == pygame.K_h:
                break
            if event.key == pygame.K_j:
                break
            pass
        pass

    if rpg_class in class_stats:
        c = class_stats[rpg_class]
        stats = Player(c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7], basic_items)
        class_constructor = c[8]
        player = class_constructor(stats)
        return player
    else:
        return class_select()


#Alternate class_select for visuals in pygame, it's a little stupid


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

#Delay because it pygame is so good at being pygame it can potentially skip over text
def wait_for_user_input():
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Yo")
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
    def draw_text(screen,text,timer):
        #Read this as put text box in, and then draw the text
        #Advance the frames, and update the display and then wait for user to press space again
        #Also fill surface because if you don't it ends up not getting rid of the previous text
        #text_box.draw_text_box(surface)
        screen.fill(BLACK)
        text_box.draw_text_box(screen)
        font = pygame.font.Font(None, 36)
        text = font.render(str(text), True, WHITE)
        screen.blit(text,(40,325))
        timer.tick(60)
        pygame.display.flip()
        wait_for_user_input()
    def class_text(screen, text,x,y):
        font= pygame.font.Font(None, 36)
        text = font.render(str(text), True, WHITE)
        screen.blit(text,(x,y))
        pass
    def print_player_stats(screen,stat,x,y):
        font = pygame.font.Font(None, 36)
        text = font.render(f"{stat} health",True, WHITE)
        screen.blit(text,(x,y))
        pygame.display.flip()

    pass

#Edit, we're probably not using this anymore

#Screen.blit for what we're drawing on top of text box and text is a string and where we're putting it
#def battle_pass_through_text(screen,text,x,y):
#    font = pygame.font.Font(None, 36)
#    text = font.render(str(text), True, WHITE)
#    screen.blit(text,(x,y))

#Contains Core Game Loop
#Sorry Daniel I have to change a bit of this to show some stuff properly cause pygame needs to run within this :)

def main():
    #Showing the game window itself
    screen = pygame.display.set_mode((WIDTH,HEIGHT))

    #Title being visible for the game 
    pygame.display.set_caption("Super Benny RPG - The game for you and me!")

    enemy_stat = Enemy(10,10,10,10,10,10,10)
    bat = Bat_Benny(enemy_stat)


    #Clock object in order to set the frame rate
    clock = pygame.time.Clock()
    #Loop for the game to work
    
    #Intro
    intro(screen,clock)
    screen.fill(BLACK)
    #Asks you to choose a class, can optimize this later
    text_box.class_text(screen, "Mage Benny", 10,350)
    text_box.class_text(screen, "S", 10,400)
    text_box.class_text(screen, "Thief Benny", 180,350)
    text_box.class_text(screen, "D", 180,400)
    text_box.class_text(screen, "Warrior Benny", 360,350)
    text_box.class_text(screen, "H", 360,400)
    text_box.class_text(screen, "Darklord Benny", 590,350)
    text_box.class_text(screen, "J", 590,400)
    pygame.display.flip()
    player = class_select()
    #Battle sequence
    screen.fill(BLACK)
    text_box.print_player_stats(screen, str(player.stats.health),0,0)
    wait_for_user_input()
    print(player.stats.health)

    while True:
        
        pygame.quit()
        sys.exit()
        pass
    '''
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
                    pass
                    #battle_pass_through_text(screen,"It's my time to shine!", WIDTH/2, HEIGHT/2)
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
    '''

#This is just gonna be a bunch of prints to tell players how the game works
#This is just getting text to display, it's a little weird but I'm working on it still
def intro(surface,timer):
    text_box.draw_text(surface,"Welcome to SUPER BENNY RPG!",timer)
    text_box.draw_text(surface,"Choose your class!",timer)
    


#Checks if smth smth (I act don't know, I just see people do this all the time)
if __name__ == "__main__":
    main()