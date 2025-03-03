import math, random, pygame, sys
from pygame.locals import * 
#Window init
WIDTH = 800
HEIGHT  = 500

#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE_SKY = (98,122,157)
RED = (175, 54, 60)
BLUE = (56,61,150)
GREEN = (70,148,73)
#COLOR = (R,G,B) Add more if you want idk

FPS = 30

#Keyboard controls I guess?
LEFT = "left"
RIGHT = "right"

#Get any enemy stats here, I guess we'll see though, or we'll just manually
#define them as well as items and just make them random
def main():
    #Any globals here I guess
    global clock, screen, font, delta, transitionScreen, playerStats, wallet, battleUIFont, enemyStats, enemySprite
    playerStats = []
    enemyStats = []
    pygame.init()
    font = pygame.font.Font("Fonts/BennyFont.ttf", 24)
    battleUIFont = pygame.font.Font("Fonts/BennyFont.ttf", 16)
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    transitionScreen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Super Benny RPG!")
    delta = clock.tick(FPS)/100
    introGame()
    chooseYourBenny()
    while True:
        battleScene.battleUI(playerStats,enemyStats)
        
def checkKey():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()
    keyEvents = pygame.event.get(KEYUP)
    if len(keyEvents) == 0:
        return None
    if keyEvents[0].key == K_ESCAPE:
        terminate()
    return keyEvents[0].key


def terminate():
    pygame.quit()
    sys.exit()


def introGame():
    while True:
        time = pygame.time.get_ticks()/1000
        sizeOne = math.sin(time) * 50 + 200
        sizeTwo = math.cos(time) * 50 + 200
        sizeThree= math.sin(time) *10 + 20
        sizeOne = int(sizeOne)
        sizeTwo = int(sizeTwo)
        sizeThree = int(sizeThree)
        screen.fill(BLACK)
        pygame.draw.circle(screen, RED, (10,10), 100 + sizeOne, sizeTwo)
        pygame.draw.circle(screen, BLUE, (810,10), 100 + sizeOne, sizeTwo)
        pygame.draw.circle(screen, BLUE_SKY, (10,410), 100 + sizeOne, sizeTwo)
        pygame.draw.circle(screen, GREEN, (810,410), 100 + sizeOne, sizeTwo)
        titleFont = pygame.font.Font("Fonts/BennyFont.ttf", 24)
        titleScreen = "Super Benny RPG"
        space = 30
        for i in range(len(titleScreen)):
            titleOneText = titleFont.render(titleScreen[i], True, GREEN)
            screen.blit(titleOneText,(200+i*space,105+1*sizeThree))
        for i in range(len(titleScreen)):
            titleOneText = titleFont.render(titleScreen[i], True, WHITE)
            screen.blit(titleOneText,(200+i*space,100+1*sizeThree))
        
        if checkKey():
            pygame.event.get()
            screenTransition()
            return
    
        pygame.display.update()
        clock.tick(FPS)
    
def chooseYourBenny():
    headerFont = pygame.font.Font("Fonts/BennyFont.ttf", 24)
    textHeader = "Choose your Benny"
    addPos = 20
    newPos = 0
    for i in range(50):
        pygame.draw.line(screen, WHITE, (0,70),(0+ i * addPos,70))
        pygame.display.update()
        clock.tick(60)
    for j in range(25):
        newPos += addPos
        screen.fill(BLACK)
        pygame.draw.line(screen, WHITE, (-300,70),(800,70))
        headerText = headerFont.render(textHeader, False, WHITE)
        screen.blit(headerText,(-300+newPos,20))
        pygame.display.update()
        clock.tick(60)

    currentChoice = "MAGE"
    while True:
        screen.fill(BLACK)
        #Make the arrows move to make the selection obvious
        time = pygame.time.get_ticks()/1000
        sizeOne = math.sin(time) * 5
        sizeOne = int(sizeOne)
        #Header needs to be in front of the screenfill LOL
        headerText = headerFont.render(textHeader, False, WHITE)
        screen.blit(headerText,(-300+newPos,20+sizeOne))
        #Draws the triangle selection
        pygame.draw.polygon(screen,WHITE,[(20+sizeOne,400),(20+sizeOne,450),(60+sizeOne,425)])
        pygame.draw.line(screen, WHITE, (-300,70),(800,70))
        choiceText = headerFont.render(currentChoice, False, WHITE)
        screen.blit(choiceText,(80+sizeOne,415))
        
        #LOL
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_RIGHT) and currentChoice == "MAGE":
                    currentChoice = "WARRIOR"
                elif (event.key == K_RIGHT) and currentChoice == "WARRIOR":
                    currentChoice = "THIEF"
                elif (event.key == K_RIGHT) and currentChoice == "THIEF":
                    currentChoice = "DARKLORD"
                elif (event.key == K_RIGHT) and currentChoice == "DARKLORD":
                    currentChoice = "MAGE"
                elif (event.key == K_LEFT) and currentChoice == "MAGE":
                    currentChoice = "DARKLORD"
                elif (event.key == K_LEFT) and currentChoice == "WARRIOR":
                    currentChoice = "MAGE"
                elif (event.key == K_LEFT) and currentChoice == "THIEF":
                    currentChoice = "WARRIOR"
                elif (event.key == K_LEFT) and currentChoice == "DARKLORD":
                    currentChoice = "THIEF"
                elif (event.key == K_SPACE):
                    setPlayerStats(currentChoice)
                    setEnemyStats()
                    screenTransition()
                    return
                elif event.key == K_ESCAPE:
                    terminate()
    
        pygame.display.update()
        clock.tick(60)

def setPlayerStats(playerClass):
    global playerStats
    #Sored as HP, MP, ATK, DEF, SPD
    if playerClass == "MAGE":
        playerStats = [50, 100, 10, 10, 20]
    elif playerClass == "WARRIOR":
        playerStats = [100, 20, 30, 20, 30]
    elif playerClass == "THIEF":
        playerStats = [75, 40, 15, 15, 50]
    elif playerClass == "DARKLORD":
        playerStats = [80, 70, 20, 15, 30]

def setEnemyStats():
    #we can probably set the enemy sprite here too
    #Just use rand int bro it's not that hard 
    enemyStats = [20,10,5,5,1]

class battleScene():
    def battleUI(pStat,eStat):
        #Print player stats
        screen.fill(BLACK)
        #HP
        toPrint = str(pStat[0])
        headerText = battleUIFont.render(toPrint, False, WHITE)
        screen.blit(headerText,(20,20))
        #MP
        toPrint = str(pStat[1])
        headerText = battleUIFont.render(toPrint, False, WHITE)
        screen.blit(headerText,(50,20))
        pygame.display.update()
        clock.tick(60)
    
    
#Scuffed
def screenTransition():
    currSize = 25
    for k in range(50):
        currSize += 25
        pygame.draw.circle(screen, BLACK, (400,200),currSize,0)
        pygame.display.update()
        clock.tick(60)
        
if __name__ == '__main__':
    main()
