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
BATTLEBG = (0,77,64)
#COLOR = (R,G,B) Add more if you want idk

FPS = 30

#Keyboard controls I guess?
LEFT = "left"
RIGHT = "right"

#Get any enemy stats here, I guess we'll see though, or we'll just manually
#define them as well as items and just make them random


#I am going to cry

def main():
    #Any globals here I guess
    global clock, screen, font, delta, transitionScreen, playerStats, wallet, battleUIFont, enemyStats, enemySprite, enemyName, playerItem, playerClass, battleCount, enemyPayout, gameOver, enemyDeath, playerAnim
    enemyDeath = []
    playerItem = "NONE"
    wallet = 0
    playerClass = "MAGE"
    playerStats = []
    enemyStats = []
    pygame.init()
    font = pygame.font.Font("Fonts/BennyFont.ttf", 24)
    battleUIFont = pygame.font.Font("Fonts/BennyFont.ttf", 16)
    gameOver= pygame.font.Font("Fonts/BennyFont.ttf", 64)
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    transitionScreen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Super Benny RPG!")
    delta = clock.tick(FPS)/100
    #Sprites
    introGame()
    chooseYourBenny()
    while True:
        battleScene.battleLogic()

        
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

def setPlayerStats(playerSelect):
    global playerStats
    global playerClass
    #Sored as HP, MP, ATK, DEF, SPD
    #Mage speed is crazy turn it back after testing
    if playerSelect == "MAGE":
        playerStats = [50, 100, 10, 10, 100]
    elif playerSelect == "WARRIOR":
        playerStats = [100, 20, 30, 20, 30]
    elif playerSelect == "THIEF":
        playerStats = [75, 40, 15, 15, 50]
    elif playerSelect == "DARKLORD":
        playerStats = [80, 70, 20, 15, 30]
    playerClass = playerSelect

def setEnemyStats():
    global enemySprite
    global enemyName
    global enemyStats
    global enemyPayout
    global enemyDeath
    bennyChosen = random.randint(1,8)
    enemyDeath = []
    #sprBennyShop = pygame.image.load("Art Files/BennyRPG ShopWindow.png")
    #Sored as HP, MP, ATK, DEF, SPD
    match bennyChosen:
        case 1:
            enemySprite = pygame.image.load("Art Files/BennyRPG Blue Benny.png").convert_alpha()
            enemyName = "BLUE BENNY"
            deathAnim1 = pygame.image.load("Art Files/Animations/Blue Benny Death (100ms)/BennyRPG Blue Benny Death Animation1.png").convert_alpha()
            deathAnim2 = pygame.image.load("Art Files/Animations/Blue Benny Death (100ms)/BennyRPG Blue Benny Death Animation2.png").convert_alpha()
            deathAnim3 = pygame.image.load("Art Files/Animations/Blue Benny Death (100ms)/BennyRPG Blue Benny Death Animation3.png").convert_alpha()
            deathAnim4 = pygame.image.load("Art Files/Animations/Blue Benny Death (100ms)/BennyRPG Blue Benny Death Animation4.png").convert_alpha()
            deathAnim5 = pygame.image.load("Art Files/Animations/Blue Benny Death (100ms)/BennyRPG Blue Benny Death Animation5.png").convert_alpha()
            deathAnim6 = pygame.image.load("Art Files/Animations/Blue Benny Death (100ms)/BennyRPG Blue Benny Death Animation6.png").convert_alpha()
            deathAnim7 = pygame.image.load("Art Files/Animations/Blue Benny Death (100ms)/BennyRPG Blue Benny Death Animation7.png").convert_alpha()
            deathAnim8 = pygame.image.load("Art Files/Animations/Blue Benny Death (100ms)/BennyRPG Blue Benny Death Animation8.png").convert_alpha()
            deathAnim9 = pygame.image.load("Art Files/Animations/Blue Benny Death (100ms)/BennyRPG Blue Benny Death Animation9.png").convert_alpha()
            enemyStats = [35,5,10,6,5]
            enemyDeath = [deathAnim1, deathAnim2, deathAnim3, deathAnim4, deathAnim5, deathAnim6, deathAnim7, deathAnim8, deathAnim9]
            enemyPayout = 15
        case 2:
            enemyName = "RED BENNY"
            enemySprite = pygame.image.load("Art Files/BennyRPG Red Benny.png").convert_alpha()
            enemyDeath.append(pygame.image.load("Art Files/Animations/Red Benny Death (100ms)/BennyRPG Red Benny Death Animation1.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Red Benny Death (100ms)/BennyRPG Red Benny Death Animation2.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Red Benny Death (100ms)/BennyRPG Red Benny Death Animation3.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Red Benny Death (100ms)/BennyRPG Red Benny Death Animation4.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Red Benny Death (100ms)/BennyRPG Red Benny Death Animation5.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Red Benny Death (100ms)/BennyRPG Red Benny Death Animation6.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Red Benny Death (100ms)/BennyRPG Red Benny Death Animation7.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Red Benny Death (100ms)/BennyRPG Red Benny Death Animation8.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Red Benny Death (100ms)/BennyRPG Red Benny Death Animation9.png").convert_alpha())
            enemyStats = [40,5,15,7,2]
            enemyPayout = 15
        case 3:
            enemyName = "GREEN BENNY"
            enemySprite = pygame.image.load("Art Files/BennyRPG Grean Beany.png").convert_alpha()
            enemyDeath.append(pygame.image.load("Art Files/Animations/Green Benny Death (100ms)/BennyRPG Green Beany Death Animation1.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Green Benny Death (100ms)/BennyRPG Green Beany Death Animation2.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Green Benny Death (100ms)/BennyRPG Green Beany Death Animation3.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Green Benny Death (100ms)/BennyRPG Green Beany Death Animation4.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Green Benny Death (100ms)/BennyRPG Green Beany Death Animation5.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Green Benny Death (100ms)/BennyRPG Green Beany Death Animation6.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Green Benny Death (100ms)/BennyRPG Green Beany Death Animation7.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Green Benny Death (100ms)/BennyRPG Green Beany Death Animation8.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Green Benny Death (100ms)/BennyRPG Green Beany Death Animation9.png").convert_alpha())
            enemyStats = [35,5,5,8,50]
            enemyPayout = 15
        case 4:
            enemyName = "PAPER BENNY"
            enemySprite = pygame.image.load("Art Files/BennyRPG Paper Benny.png").convert_alpha()
            enemyDeath.append(pygame.image.load("Art Files/Animations/Paper Benny Death (100ms)/BennyRPG Paper Benny Death Animation1.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Paper Benny Death (100ms)/BennyRPG Paper Benny Death Animation2.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Paper Benny Death (100ms)/BennyRPG Paper Benny Death Animation3.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Paper Benny Death (100ms)/BennyRPG Paper Benny Death Animation4.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Paper Benny Death (100ms)/BennyRPG Paper Benny Death Animation5.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Paper Benny Death (100ms)/BennyRPG Paper Benny Death Animation6.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Paper Benny Death (100ms)/BennyRPG Paper Benny Death Animation7.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Paper Benny Death (100ms)/BennyRPG Paper Benny Death Animation8.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Paper Benny Death (100ms)/BennyRPG Paper Benny Death Animation9.png").convert_alpha())
            enemyStats = [35,5,10,6,5]
            enemyPayout = 15
        case 5:
            enemyName = "GOLD BENNY"
            enemySprite = pygame.image.load("Art Files/BennyRPG Gold Benny.png").convert_alpha()
            enemyDeath.append(pygame.image.load("Art Files/Animations/Gold Benny Death (100ms)/BennyRPG Gold Benny Death Animation1.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Gold Benny Death (100ms)/BennyRPG Gold Benny Death Animation2.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Gold Benny Death (100ms)/BennyRPG Gold Benny Death Animation3.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Gold Benny Death (100ms)/BennyRPG Gold Benny Death Animation4.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Gold Benny Death (100ms)/BennyRPG Gold Benny Death Animation5.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Gold Benny Death (100ms)/BennyRPG Gold Benny Death Animation6.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Gold Benny Death (100ms)/BennyRPG Gold Benny Death Animation7.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Gold Benny Death (100ms)/BennyRPG Gold Benny Death Animation8.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Gold Benny Death (100ms)/BennyRPG Gold Benny Death Animation9.png").convert_alpha())
            enemyStats = [100,5,10,6,5]
            enemyPayout = 15
        case 6:
            enemyName = "TURBO BENNY"
            enemySprite = pygame.image.load("Art Files/BennyRPG Turbo Benny.png").convert_alpha()
            enemyDeath.append(pygame.image.load("Art Files/Animations/Turbo Benny Death (100ms)/BennyRPG Turbo Benny Death Animation1.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Turbo Benny Death (100ms)/BennyRPG Turbo Benny Death Animation2.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Turbo Benny Death (100ms)/BennyRPG Turbo Benny Death Animation3.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Turbo Benny Death (100ms)/BennyRPG Turbo Benny Death Animation4.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Turbo Benny Death (100ms)/BennyRPG Turbo Benny Death Animation5.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Turbo Benny Death (100ms)/BennyRPG Turbo Benny Death Animation6.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Turbo Benny Death (100ms)/BennyRPG Turbo Benny Death Animation7.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Turbo Benny Death (100ms)/BennyRPG Turbo Benny Death Animation8.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Turbo Benny Death (100ms)/BennyRPG Turbo Benny Death Animation9.png").convert_alpha())
            enemyStats = [25,5,10,6,1000]
            enemyPayout = 15
        case 7:
            enemyName = "BAT BENNY"
            enemySprite = pygame.image.load("Art Files/Bat Benny.png").convert_alpha()
            enemyDeath.append(pygame.image.load("Art Files/Animations/Bat Benny Death (100ms)/BennyRPG Bat Benny Death Animation1.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Bat Benny Death (100ms)/BennyRPG Bat Benny Death Animation2.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Bat Benny Death (100ms)/BennyRPG Bat Benny Death Animation3.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Bat Benny Death (100ms)/BennyRPG Bat Benny Death Animation4.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Bat Benny Death (100ms)/BennyRPG Bat Benny Death Animation5.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Bat Benny Death (100ms)/BennyRPG Bat Benny Death Animation6.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Bat Benny Death (100ms)/BennyRPG Bat Benny Death Animation7.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Bat Benny Death (100ms)/BennyRPG Bat Benny Death Animation8.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Bat Benny Death (100ms)/BennyRPG Bat Benny Death Animation9.png").convert_alpha())
            enemyStats = [45,5,15,10,100]
            enemyPayout = 15
        case 8:
            enemyName = "EVIL BENNY"
            enemySprite = pygame.image.load("Art Files/Evil Benny.png").convert_alpha()
            enemyDeath.append(pygame.image.load("Art Files/Animations/Evil Benny Death (100ms)/BennyRPG Evil Benny Death Animation1.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Evil Benny Death (100ms)/BennyRPG Evil Benny Death Animation2.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Evil Benny Death (100ms)/BennyRPG Evil Benny Death Animation3.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Evil Benny Death (100ms)/BennyRPG Evil Benny Death Animation4.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Evil Benny Death (100ms)/BennyRPG Evil Benny Death Animation5.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Evil Benny Death (100ms)/BennyRPG Evil Benny Death Animation6.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Evil Benny Death (100ms)/BennyRPG Evil Benny Death Animation7.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Evil Benny Death (100ms)/BennyRPG Evil Benny Death Animation8.png").convert_alpha())
            enemyDeath.append(pygame.image.load("Art Files/Animations/Evil Benny Death (100ms)/BennyRPG Evil Benny Death Animation9.png").convert_alpha())
            enemyStats = [500,5,20,8,5]
            enemyPayout = 15

class battleScene():
    def battleUI(pStat,eStat):
        #Print player stats
        #HP
        uiHealth = pygame.image.load("Art Files/BennyRPG Health UI.png").convert_alpha()
        uiMana = pygame.image.load("Art Files/BennyRPG Mana.png").convert_alpha()
        #uiHealth = pygame.transform.scale(uiHealth,(64,64))
        #uiMana = pygame.transform.scale(uiMana,(64,64))
        toPrint = str(pStat[0])
        headerText = battleUIFont.render("HP " + toPrint, False, WHITE)
        screen.blit(uiHealth,(270,420))
        screen.blit(headerText,(300,420))
        #MP
        toPrint = str(pStat[1])
        headerText = battleUIFont.render("MP " +toPrint, False, WHITE)
        screen.blit(uiMana,(270,440))
        screen.blit(headerText,(300,440))
        #pygame.display.update()
        #clock.tick(60)
        
    def battleBGIntro():
        battleBg = pygame.image.load("Art Files/BennyRPG Fighting Grounds.png")
        targetHeight = 270
        targetWidth = 780
        newHeight = 60
        newWidth = 10
        
        while newHeight != targetHeight:
            screen.blit(battleBg,(30,60))
            newHeight += 10
            pygame.draw.rect(screen, BLACK, [(newWidth,newHeight),(780,270)])
            pygame.display.update()
            clock.tick(60)
        while newWidth != targetWidth:
            screen.blit(battleBg,(30,60))
            newWidth += 10
            pygame.draw.rect(screen, BLACK, [(newWidth,newHeight),(780,270)])
            pygame.display.update()
            clock.tick(60)
            
    def battleBG():
        
        battleBg = pygame.image.load("Art Files/BennyRPG Fighting Grounds.png")
        screen.blit(battleBg,(30,60))
        
    def playerAnimation(toplay):
        global playerAnim
        global playerClass
        playerAnim = []
        if toplay == "ATTACK":
            slash1 = pygame.image.load("Art Files/Animations/Basic Attack (100ms)/BennyRPG Basic Atk1.png").convert_alpha()
            slash1 = pygame.transform.scale(slash1,(128,128))
            slash2 = pygame.image.load("Art Files/Animations/Basic Attack (100ms)/BennyRPG Basic Atk2.png").convert_alpha()
            slash2 = pygame.transform.scale(slash2,(128,128))
            slash3 = pygame.image.load("Art Files/Animations/Basic Attack (100ms)/BennyRPG Basic Atk3.png").convert_alpha()
            slash3 = pygame.transform.scale(slash3,(128,128))
            slash4 = pygame.image.load("Art Files/Animations/Basic Attack (100ms)/BennyRPG Basic Atk4.png").convert_alpha()
            slash4 = pygame.transform.scale(slash4,(128,128))
            slash5 = pygame.image.load("Art Files/Animations/Basic Attack (100ms)/BennyRPG Basic Atk5.png").convert_alpha()
            slash5 = pygame.transform.scale(slash5,(128,128))
            slash6 = pygame.image.load("Art Files/Animations/Basic Attack (100ms)/BennyRPG Basic Atk6.png").convert_alpha()
            slash6 = pygame.transform.scale(slash6,(128,128))
            slash7 = pygame.image.load("Art Files/Animations/Basic Attack (100ms)/BennyRPG Basic Atk7.png").convert_alpha()
            slash7 = pygame.transform.scale(slash7,(128,128))
            slash8 = pygame.image.load("Art Files/Animations/Basic Attack (100ms)/BennyRPG attackEnd.png").convert_alpha()
            playerAnim = [slash1, slash2, slash3, slash4, slash5, slash6, slash7, slash8]
            for i, anim in enumerate(playerAnim):
                battleScene.battleBG()
                battleScene.drawEnemy()
                screen.blit(anim,(325,150))
                pygame.display.update()
                clock.tick(30)
            battleScene.enemyDamaged()
        elif toplay == "SKILL":
            match playerClass:
                case "MAGE":
                    playerAnim.append(pygame.image.load("Art Files/Animations/Ice Attack (100ms)/BennyRPG Ice Attack1.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Ice Attack (100ms)/BennyRPG Ice Attack2.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Ice Attack (100ms)/BennyRPG Ice Attack3.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Ice Attack (100ms)/BennyRPG Ice Attack4.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Ice Attack (100ms)/BennyRPG Ice Attack5.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Ice Attack (100ms)/BennyRPG Ice Attack6.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Ice Attack (100ms)/BennyRPG Ice Attack7.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Ice Attack (100ms)/BennyRPG Ice Attack8.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Ice Attack (100ms)/BennyRPG Ice Attack9.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Ice Attack (100ms)/BennyRPG Ice Attack10.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Ice Attack (100ms)/BennyRPG Ice Attack11.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Ice Attack (100ms)/BennyRPG Ice Attack12.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Ice Attack (100ms)/BennyRPG Ice Attack13.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Ice Attack (100ms)/BennyRPG Ice Attack14.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Ice Attack (100ms)/BennyRPG Ice Attack15.png").convert_alpha())
                    
                case "WARRIOR":
                    playerAnim.append(pygame.image.load("Art Files/Animations/Cross Slash (100ms)/BennyRPG Cross Slash1.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Cross Slash (100ms)/BennyRPG Cross Slash2.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Cross Slash (100ms)/BennyRPG Cross Slash3.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Cross Slash (100ms)/BennyRPG Cross Slash4.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Cross Slash (100ms)/BennyRPG Cross Slash5.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Ice Attack (100ms)/BennyRPG Ice Attack15.png").convert_alpha())
                    
                case "DARKLORD":
                    shadowballExplosion = []
                    playerAnim.append(pygame.image.load("Art Files/Animations/Shadow Ball Idle (100ms)/BennyRPG Shadow Ball1.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Shadow Ball Idle (100ms)/BennyRPG Shadow Ball2.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Shadow Ball Idle (100ms)/BennyRPG Shadow Ball3.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Shadow Ball Idle (100ms)/BennyRPG Shadow Ball4.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Shadow Ball Idle (100ms)/BennyRPG Shadow Ball5.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Shadow Ball Idle (100ms)/BennyRPG Shadow Ball6.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Shadow Ball Idle (100ms)/BennyRPG Shadow Ball7.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Shadow Ball Idle (100ms)/BennyRPG Shadow Ball8.png").convert_alpha())
                    shadowballExplosion.append(pygame.image.load("Art Files/Animations/Shadow Ball Explosion (50ms)/BennyRPG Shadow Ball9.png").convert_alpha())
                    shadowballExplosion.append(pygame.image.load("Art Files/Animations/Shadow Ball Explosion (50ms)/BennyRPG Shadow Ball10.png").convert_alpha())
                    shadowballExplosion.append(pygame.image.load("Art Files/Animations/Shadow Ball Explosion (50ms)/BennyRPG Shadow Ball11.png").convert_alpha())
                    shadowballExplosion.append(pygame.image.load("Art Files/Animations/Shadow Ball Explosion (50ms)/BennyRPG Shadow Ball12.png").convert_alpha())
                    shadowballExplosion.append(pygame.image.load("Art Files/Animations/Shadow Ball Explosion (50ms)/BennyRPG Shadow Ball13.png").convert_alpha())
                    shadowballExplosion.append(pygame.image.load("Art Files/Animations/Shadow Ball Explosion (50ms)/BennyRPG Shadow Ball14.png").convert_alpha())
                    shadowballExplosion.append(pygame.image.load("Art Files/Animations/Shadow Ball Explosion (50ms)/BennyRPG Shadow Ball15.png").convert_alpha())
                    shadowballExplosion.append(pygame.image.load("Art Files/Animations/Shadow Ball Explosion (50ms)/BennyRPG Shadow Ball16.png").convert_alpha())
                    shadowballExplosion.append(pygame.image.load("Art Files/Animations/Shadow Ball Explosion (50ms)/BennyRPG Shadow Ball17.png").convert_alpha())
                    shadowballExplosion.append(pygame.image.load("Art Files/Animations/Shadow Ball Explosion (50ms)/BennyRPG Shadow Ball18.png").convert_alpha())
                    shadowballExplosion.append(pygame.image.load("Art Files/Animations/Shadow Ball Explosion (50ms)/BennyRPG Shadow Ball19.png").convert_alpha())
                    shadowballExplosion.append(pygame.image.load("Art Files/Animations/Shadow Ball Explosion (50ms)/BennyRPG Shadow Ball20.png").convert_alpha())
                    shadowballExplosion.append(pygame.image.load("Art Files/Animations/Shadow Ball Explosion (50ms)/BennyRPG Shadow Ball21.png").convert_alpha())
                    shadowballExplosion.append(pygame.image.load("Art Files/Animations/Shadow Ball Explosion (50ms)/BennyRPG Shadow Ball22.png").convert_alpha())
                    shadowballExplosion.append(pygame.image.load("Art Files/Animations/Shadow Ball Explosion (50ms)/BennyRPG Shadow Ball23.png").convert_alpha())
                    shadowballExplosion.append(pygame.image.load("Art Files/Animations/Shadow Ball Explosion (50ms)/BennyRPG Shadow Ball24.png").convert_alpha())
                    shadowballExplosion.append(pygame.image.load("Art Files/Animations/Shadow Ball Explosion (50ms)/BennyRPG Shadow Ball25.png").convert_alpha())
                    shadowballExplosion.append(pygame.image.load("Art Files/Animations/Shadow Ball Explosion (50ms)/BennyRPG Shadow Ball26.png").convert_alpha())
                    shadowballExplosion.append(pygame.image.load("Art Files/Animations/Shadow Ball Explosion (50ms)/BennyRPG Shadow Ball27.png").convert_alpha())
                    pass
                case "THIEF":
                    playerAnim.append(pygame.image.load("Art Files/Animations/Spinning Knife (50ms)/BennyRPG Spinning Dagger1.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Spinning Knife (50ms)/BennyRPG Spinning Dagger2.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Spinning Knife (50ms)/BennyRPG Spinning Dagger3.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Spinning Knife (50ms)/BennyRPG Spinning Dagger4.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Spinning Knife (50ms)/BennyRPG Spinning Dagger5.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Spinning Knife (50ms)/BennyRPG Spinning Dagger6.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Spinning Knife (50ms)/BennyRPG Spinning Dagger7.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Spinning Knife (50ms)/BennyRPG Spinning Dagger8.png").convert_alpha())
                    playerAnim.append(pygame.image.load("Art Files/Animations/Ice Attack (100ms)/BennyRPG Ice Attack15.png").convert_alpha())
            if playerClass == "DARKLORD":
                for i, anim in enumerate(playerAnim):
                    #7
                    battleScene.battleBG()
                    anim = pygame.transform.scale(anim,(128,128))
                    oneShadow = anim
                    twoShadow = anim
                    threeShadow = anim
                    battleScene.drawEnemy()
                    screen.blit(oneShadow,(500-i*25,150))
                    screen.blit(twoShadow,(175+i*25,150))
                    screen.blit(threeShadow,(325,80+i*10))
                    pygame.display.update()
                    clock.tick(40)
                for j, anim in enumerate(shadowballExplosion):
                    battleScene.battleBG()
                    anim = pygame.transform.scale(anim,(128,128))
                    battleScene.drawEnemy()
                    screen.blit(anim,(325,150))
                    pygame.display.update()
                    clock.tick(30)
            elif playerClass == "THIEF":
                for j, anim in enumerate(playerAnim):
                    battleScene.battleBG()
                    anim = pygame.transform.scale(anim,(128,128))
                    battleScene.drawEnemy()
                    screen.blit(anim,(325,60+j*10))
                    pygame.display.update()
                    clock.tick(30)
            else:
                for i, anim in enumerate(playerAnim):
                    battleScene.battleBG()
                    anim = pygame.transform.scale(anim,(128,128))
                    battleScene.drawEnemy()
                    screen.blit(anim,(325,150))
                    pygame.display.update()
                    clock.tick(15)
            battleScene.enemyDamaged()

        

    def drawEnemy():
        global enemySprite
        enemySprite = pygame.transform.scale(enemySprite,(128,128))
        screen.blit(enemySprite,(325,150))
        
    def enemyDamaged():
        global enemySprite
        enemySprite = pygame.transform.scale(enemySprite,(128,128))
        fakeFrame = pygame.image.load("Art Files/Animations/Basic Attack (100ms)/BennyRPG attackEnd.png").convert_alpha()
        for i in range(10):
            battleScene.battleBG()
            if i // 2 == 1:
                screen.blit(enemySprite,(325,150))
            elif i //2 == 0:
                screen.blit(fakeFrame,(325,150))
            pygame.display.update()
            clock.tick(20)
        screen.blit(enemySprite,(325,150))
        pygame.display.update()
        clock.tick(20)

    def playerAttack():
        #Sored as HP, MP, ATK, DEF, SPD as a reminder
        global enemyStats
        global playerStats
        playerDamage = playerStats[2]
        enemyDefense = enemyStats[3]
        damage = playerDamage - random.randint(enemyDefense-3,enemyDefense)
        #Attack anim function here depending on the player global class
        #class attack anim()
        Textbox = "You did " + str(damage) + " damage"
        pygame.draw.rect(screen, BLACK, [(20,360),(780,460)])
        pygame.draw.rect(screen, WHITE, [(20,360),(750,130)],3)
        pygame.display.update()
        clock.tick(30)
        enemyStats[0] -= damage
        textDraw = ""        
        for i in range(len(Textbox)):
            textDraw += Textbox[i]
            uiUpdate = battleUIFont.render(textDraw, True, WHITE)
            screen.blit(uiUpdate, (30,390))
            pygame.display.update()
            clock.tick(60) 
        while True:
             for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                elif event.type == KEYDOWN:
                    return
                
    def playerSkill():
        #Sored as HP, MP, ATK, DEF, SPD as a reminder
        global enemyStats
        global playerStats
        global playerClass
        cost = 5
        playerDamage = playerStats[2]
        enemyDefense = enemyStats[3]
        damage = (playerDamage * 3) - random.randint(enemyDefense-3,enemyDefense)
        #skill anim function here depending on the player global class
        #class skill attack anim()
        Textbox = "Used " + str(playerClass) + " skill to do " + str(damage) + " damage"
        pygame.draw.rect(screen, BLACK, [(20,360),(780,460)])
        pygame.draw.rect(screen, WHITE, [(20,360),(750,130)],3)
        pygame.display.update()
        clock.tick(30)
        textDraw = ""
        playerStats[1] -= 5
        enemyStats[0] -= damage
        for i in range(len(Textbox)):
            textDraw += Textbox[i]
            uiUpdate = battleUIFont.render(textDraw, True, WHITE)
            screen.blit(uiUpdate, (30,390))
            pygame.display.update()
            clock.tick(60) 
        while True:
             for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                elif event.type == KEYDOWN:
                    return

    def enemyChatter():
        global enemyName
        Textbox = str(enemyName) + " lunges forward"
        pygame.draw.rect(screen, BLACK, [(20,360),(780,460)])
        pygame.draw.rect(screen, WHITE, [(20,360),(750,130)],3)
        pygame.display.update()
        clock.tick(30)
        textDraw = ""
        for i in range(len(Textbox)):
            textDraw += Textbox[i]
            uiUpdate = battleUIFont.render(textDraw, True, WHITE)
            screen.blit(uiUpdate, (30,390))
            pygame.display.update()
            clock.tick(60)
        while True:
             for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                elif event.type == KEYDOWN:
                    return
    
    def enemyAttack():
        #Sored as HP, MP, ATK, DEF, SPD as a reminder
        global enemyStats
        global playerStats
        global enemyName
        enemyDamage = enemyStats[2] + 5
        playerDefense = playerStats[3]
        damage = (enemyDamage) - random.randint(playerDefense-3,playerDefense)
        #idk maybe camera shake
        damage = abs(damage)
        Textbox = str(enemyName) + " does " + str(damage) + " damage"
        pygame.draw.rect(screen, BLACK, [(20,360),(780,460)])
        pygame.draw.rect(screen, WHITE, [(20,360),(750,130)],3)
        pygame.display.update()
        clock.tick(30)
        textDraw = ""
        playerStats[0] -= damage
        for i in range(len(Textbox)):
            textDraw += Textbox[i]
            uiUpdate = battleUIFont.render(textDraw, True, WHITE)
            screen.blit(uiUpdate, (30,390))
            pygame.display.update()
            clock.tick(60) 
        while True:
             for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                elif event.type == KEYDOWN:
                    return
    def checkEnemyDead():
        global enemyStats
        if enemyStats[0] <= 0:
            enemyStats[0] = 0
            battleScene.enemyDeath()
            return True
        
    def enemyDeath():
        global enemyDeath
        for i, anim in enumerate(enemyDeath):
            anim = pygame.transform.scale(anim,(128,128))
            battleScene.battleBG()
            screen.blit(anim,(325,150))
            pygame.display.update()
            clock.tick(20)
        
    def checkPlayerDead():
        global playerStats
        if playerStats[0] <= 0:
            playerStats[0] = 0
            return True
    
    def playerItem():
        #Sored as HP, MP, ATK, DEF, SPD as a reminder
        global playerItem
        global playerStats
        textDraw = ""
        match playerItem:
            case "NONE":
                Textbox = "Yo aint got no items bruh"
            case "RED POTION":
                Textbox = "Drank a cherry potion"
                playerStats[0] += 10
                playerStats[2] += 2
            case "BLUE POTION":
                Textbox = "Drank a blueberry potion"
                playerStats[1] += 20
                playerStats[3] += 2
            case "GREEN POTION":
                Textbox = "Drank a green apple potion"
                for i in range(len(playerStats)):
                    playerStats[i] += 1
        pygame.draw.rect(screen, BLACK, [(20,360),(780,460)])
        pygame.draw.rect(screen, WHITE, [(20,360),(750,130)],3)
        for i in range(len(Textbox)):
            textDraw += Textbox[i]
            uiUpdate = battleUIFont.render(textDraw, True, WHITE)
            screen.blit(uiUpdate, (30,390))
            pygame.display.update()
            clock.tick(60)
            
        while True:
             for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                elif event.type == KEYDOWN:
                    return

        pass
    
    def battlePayOut():
        global wallet
        global enemyPayout
        wallet += random.randint(enemyPayout-5,enemyPayout)


    
    def playerAction(playerAct):
        global enemyStats
        global playerStats
        global playerItem
        if playerAct == "ATTACK":
            battleScene.playerAnimation("ATTACK")
            battleScene.playerAttack()
            return True
        if playerAct == "SKILL" and playerStats[1]>=5:
            battleScene.playerAnimation("SKILL")
            battleScene.playerSkill()
            return True
        if playerAct == "ITEM" and playerItem != "NONE":
            battleScene.playerItem()
            return True
        if playerAct == "ITEM" and playerItem == "NONE":
            battleScene.playerItem()
            return False

    def playerCursor(choice):
        time = pygame.time.get_ticks()/1000
        sizeOne = math.sin(time) * 5
        sizeOne = int(sizeOne)
        pygame.draw.polygon(screen,WHITE,[(60+sizeOne,390+choice*20),(60+sizeOne,410+choice*20),(70+sizeOne,400+choice*20)])

    def deadScreen():
        screenTransition()
        screen.fill(BLACK)
        for i in range(255):
            gameOverText = gameOver.render("GAME OVER", True, (i,i,i))
            screen.blit(gameOverText,(((800/2)-300), (500/2)-100))
            pygame.display.update()
            clock.tick(60)
        retryChoice = 0
        retryText = ["YES", "NO"]
        
        while True:
            screen.fill(BLACK)
            gameOverText = gameOver.render("GAME OVER", True, WHITE)
            screen.blit(gameOverText,(((800/2)-300), (500/2)-100))
            gameOverText = battleUIFont.render("Will you try again", True, WHITE)
            screen.blit(gameOverText,(((800/2)-150), (500/2)))
            battleScene.deadScreenCursor(retryChoice)
            for f, option in enumerate(retryText):
                text = battleUIFont.render(option,True,WHITE)
                screen.blit(text,((300+f*150),300))
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                elif event.type == KEYDOWN:
                    if (event.key == K_LEFT):
                        retryChoice = 0
                    elif (event.key == K_RIGHT):
                        retryChoice = 1
                    elif (event.key == K_SPACE):
                        battleScene.deadScreenChoice(retryChoice)
                        return
            pygame.display.update()
            clock.tick(60)

    def deadScreenChoice(choice):
        global enemyStats
        global playerStats
        global playerClass
        classs = playerClass
        if choice == 0:
            screenTransition()
            setPlayerStats(classs)
            setEnemyStats()
        elif choice == 1:
            screenTransition()
            terminate()

    def deadScreenCursor(point):
        time = pygame.time.get_ticks()/1000
        sizeOne = math.sin(time) * 5
        sizeOne = int(sizeOne)
        pygame.draw.polygon(screen,WHITE,[(280+sizeOne+point*150,300),(280+sizeOne+point*150,320),(295+sizeOne+point*150,310)])
            
    def playerWin():
        textDraw = ""
        Textbox = "Y O U   W I N"
        pygame.draw.rect(screen, BLACK, [(20,360),(780,460)])
        pygame.draw.rect(screen, WHITE, [(20,360),(750,130)],3)
        for i in range(len(Textbox)):
            textDraw += Textbox[i]
            uiUpdate = battleUIFont.render(textDraw, True, WHITE)
            screen.blit(uiUpdate, (30,390))
            pygame.display.update()
            clock.tick(60)
        while True:
             for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                elif event.type == KEYDOWN:
                    return
        
    def battleLogic():
        battleScene.battleBGIntro()
        global playerStats
        global enemyStats
        eSpeed = enemyStats[-1]
        pSpeed = playerStats[-1]
        isPlayerTurn = True
        isPlayerChoiceValid = False
        isEnemyDead = False
        isPlayerDead = False
        isBattle = True
        if eSpeed > pSpeed:
            isPlayerTurn = False
        elif pSpeed > eSpeed:
            isPlayerTurn = True
        else:
            isPlayerTurn = True
        #Basically a battle, wait can I do something better for this?
        while isBattle:
            playerCommandOptions = ["ATTACK", "SKILL", "ITEM"]
            playerChoice = 0
            #Player turn
            while isPlayerTurn and not isEnemyDead and not isPlayerDead:
                screen.fill(BLACK)
                battleScene.battleBG()
                battleScene.drawEnemy()
                battleScene.battleUI(playerStats,enemyStats)
                for f in range(3):
                    playerChoiceText = battleUIFont.render(playerCommandOptions[f], True, WHITE)
                    screen.blit(playerChoiceText,(80,390+f*20))
                commandPrompt = battleUIFont.render("Commands", True, WHITE)
                screen.blit(commandPrompt,(60,370))
                battleScene.playerCursor(playerChoice)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        terminate()
                    elif event.type == KEYDOWN:
                        if (event.key == K_DOWN) and playerChoice < 2:
                            playerChoice += 1
                        elif (event.key == K_UP) and playerChoice > 0:
                            playerChoice -= 1
                        elif (event.key == K_SPACE):
                            isPlayerChoiceValid = battleScene.playerAction(playerCommandOptions[playerChoice])
                        elif event.key == K_ESCAPE:
                            terminate()
                pygame.display.update()
                clock.tick(60)
                isEnemyDead = battleScene.checkEnemyDead()
                if isPlayerChoiceValid and not isEnemyDead and not isPlayerDead:
                    isPlayerTurn = False
                elif isPlayerChoiceValid and isEnemyDead:
                    isPlayerTurn = False
                    isBattle = False
            #ENEMY Turn
            while not isPlayerTurn and not isEnemyDead and not isPlayerDead:
                battleScene.battleBG()
                battleScene.drawEnemy()
                battleScene.enemyChatter()
                battleScene.enemyAttack()
                isPlayerDead = battleScene.checkPlayerDead()
                if not isPlayerDead:
                    isPlayerTurn = True
                    isPlayerChoiceValid = False
                elif isPlayerDead:
                    isPlayerTurn = False
                    isBattle = False
            if isBattle == False:
                if isEnemyDead:
                    battleScene.battlePayOut()
                break
        if isEnemyDead:
            battleScene.playerWin()
            screenTransition()
            battleScene.shopLogic()
        if isPlayerDead:
            battleScene.deadScreen()

    def shopIntro():
        sprBennyShop = pygame.image.load("Art Files/BennyRPG ShopWindow.png")
        sprBennyCoin = pygame.image.load("Art Files/BennyRPG Benny Coin.png").convert_alpha()
        sprBluePotion = pygame.image.load("Art Files/Blue_Potion_1.png").convert_alpha()
        sprRedPotion = pygame.image.load("Art Files/Red_Potion_1.png").convert_alpha()
        sprGreenPotion = pygame.image.load("Art Files/Green_Potion_1.png").convert_alpha()
        sprEmptyBottle = pygame.image.load("Art Files/Empty_Bottle.png").convert_alpha()
        sprDoor = pygame.image.load("Art Files/BennyRPG_Door_Exit.png").convert_alpha()
        sprBluePotion = pygame.transform.scale(sprBluePotion,(48,48))
        sprRedPotion = pygame.transform.scale(sprRedPotion,(48,48))
        sprGreenPotion = pygame.transform.scale(sprGreenPotion,(48,48))
        sprDoor = pygame.transform.scale(sprDoor,(48,48))
        bennyInventory = [sprRedPotion, sprGreenPotion, sprBluePotion]
        bennyPrices = [20,15,10]
        bennyItemNames = ["Red Potion", "Green Potion", "Blue Potion", "Exit"]
        screen.fill(BLACK)
        fade = pygame.Surface((WIDTH,HEIGHT))
        fade.fill((0,0,0))
        for i in range(150):
            screen.blit(sprBennyShop,(0,0))
            fade.set_alpha(300-i*2)
            screen.blit(sprBennyShop,(0,0))
            screen.blit(sprBennyCoin,(5,5))
            inWallet = str(wallet)
            inWalletRender = battleUIFont.render(inWallet, True, WHITE)
            screen.blit(inWalletRender,(25,5))
            for i, stock in enumerate(bennyInventory):
                screen.blit(stock, (100+i*200,400))
            for j, stock in enumerate(bennyPrices):
                priceText = battleUIFont.render(str(stock),True,WHITE)
                screen.blit(priceText,(110+j*200,450))
            for k, stock in enumerate(bennyItemNames):
                itemName = battleUIFont.render(str(stock),True,WHITE)
                screen.blit(itemName,(75+k*200,370))
            screen.blit(sprDoor, (675,400))
            screen.blit(fade,(0,0))
            pygame.display.update()
            clock.tick(60)
            
    def shopLogic():
        #BennyRPG_Door_Exit
        sprBennyCoin = pygame.image.load("Art Files/BennyRPG Benny Coin.png").convert_alpha()
        sprBennyShop = pygame.image.load("Art Files/BennyRPG ShopWindow.png")
        sprBluePotion = pygame.image.load("Art Files/Blue_Potion_1.png").convert_alpha()
        sprRedPotion = pygame.image.load("Art Files/Red_Potion_1.png").convert_alpha()
        sprGreenPotion = pygame.image.load("Art Files/Green_Potion_1.png").convert_alpha()
        sprEmptyBottle = pygame.image.load("Art Files/Empty_Bottle.png").convert_alpha()
        sprDoor = pygame.image.load("Art Files/BennyRPG_Door_Exit.png").convert_alpha()
        sprBluePotion = pygame.transform.scale(sprBluePotion,(48,48))
        sprRedPotion = pygame.transform.scale(sprRedPotion,(48,48))
        sprGreenPotion = pygame.transform.scale(sprGreenPotion,(48,48))
        sprDoor = pygame.transform.scale(sprDoor,(48,48))
        battleScene.shopIntro()
        global wallet
        global playerItem
        global enemyStats
        pygame.display.update()
        clock.tick(60)
        shopChoice = 0
        bennyInventory = [sprRedPotion, sprGreenPotion, sprBluePotion]
        bennyPrices = [20,15,10]
        bennyItemNames = ["Red Potion", "Green Potion", "Blue Potion", "Exit"]
        #gameOverText = battleUIFont.render("Will you try again", True, WHITE)
         #   screen.blit(gameOverText,(((800/2)-150), (500/2)))
        while True:
            screen.blit(sprBennyShop,(0,0))
            screen.blit(sprBennyCoin,(5,5))
            inWallet = str(wallet)
            inWalletRender = battleUIFont.render(inWallet, True, WHITE)
            screen.blit(inWalletRender,(25,5))
            screen.blit(sprDoor, (675,400))
            for i, stock in enumerate(bennyInventory):
                screen.blit(stock, (100+i*200,400))
            for j, stock in enumerate(bennyPrices):
                priceText = battleUIFont.render(str(stock),True,WHITE)
                screen.blit(priceText,(110+j*200,450))
            for k, stock in enumerate(bennyItemNames):
                itemName = battleUIFont.render(str(stock),True,WHITE)
                screen.blit(itemName,(75+k*200,370))
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                elif event.type == KEYDOWN:
                    if (event.key == K_RIGHT) and shopChoice < 3:
                        shopChoice +=1
                    elif (event.key == K_LEFT) and shopChoice > 0:
                        shopChoice -=1
                    elif (event.key == K_SPACE):
                        inWallet = battleScene.buyItem(shopChoice)
                        setEnemyStats()
                        screenTransition()
                        return
            battleScene.shopCursor(shopChoice)
            pygame.display.update()
            clock.tick(60)
            screen.fill(BLACK)

    def shopCursor(point):
        time = pygame.time.get_ticks()/1000
        sizeOne = math.sin(time) * 5
        sizeOne = int(sizeOne)
        pygame.draw.polygon(screen,WHITE,[(90+sizeOne+point*195,410),(90+sizeOne+point*195,440),(100+sizeOne+point*195,425)])

        pass
    def buyItem(choice):
        global wallet
        global playerItem
        match choice:
            case 0:
                if wallet >= 20:
                    playerItem = "RED POTION"
                    return wallet - 20
            case 1:
                if wallet >= 15:
                    playerItem = "GREEN POTION"
                    return wallet - 15
            case 2:
                if wallet >= 10:
                    playerItem = "BLUE POTION"
                    return wallet - 10
            case 3:
                return wallet
        
        
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
