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
def main():
    #Any globals here I guess
    global clock, screen, font, delta, transitionScreen, playerStats, wallet, battleUIFont, enemyStats, enemySprite, enemyName, playerItem, playerClass, battleCount, enemyPayout, gameOver
    
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
    global enemeySprite
    global enemyName
    global enemyStats
    global enemyPayout
    enemyName = "TEMP BENNY"
    enemyStats = [20,10,500,5,1]
    enemyPayout = 20

class battleScene():
    def battleUI(pStat,eStat):
        #Print player stats
        #HP
        toPrint = str(pStat[0])
        headerText = battleUIFont.render("HP " + toPrint, False, WHITE)
        screen.blit(headerText,(300,420))
        #MP
        toPrint = str(pStat[1])
        headerText = battleUIFont.render("MP " +toPrint, False, WHITE)
        screen.blit(headerText,(300,440))
        #pygame.display.update()
        #clock.tick(60)
        
    def battleBGIntro():
        targetHeight = 270
        targetWidth = 780
        newHeight = 60
        newWidth = 10
        while newHeight != targetHeight:
            newHeight += 10
            pygame.draw.rect(screen, BATTLEBG, [(10,60),(newWidth,newHeight)])
            pygame.display.update()
            clock.tick(60)
        while newWidth != targetWidth:
            newWidth += 10
            pygame.draw.rect(screen, BATTLEBG, [(10,60),(newWidth,newHeight)])
            pygame.display.update()
            clock.tick(60)
            
    def battleBG():
        pygame.draw.rect(screen, BATTLEBG, [(10,60),(780,270)])

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
            return True
    
    def checkPlayerDead():
        global playerStats
        if playerStats[0] <= 0:
            playerStats[0] = 0
            return True
    
    def playerItem():
        global playerItem
        global playerStats
        textDraw = ""
        if playerItem == "NONE":
            Textbox = "Yo aint got no items bruh"
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
            battleScene.playerAttack()
            return True
        if playerAct == "SKILL" and playerStats[1]>=5:
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
        for i in range(30):
            screen.fill(BLACK)
            shopTitle = "Benny Emporium of Goods"
            shopRender = font.render(shopTitle, True, WHITE)
            screen.blit(shopRender,(-370+i*15,40))
            pygame.display.update()
            clock.tick(60)
    
    def shopLogic():
        screen.fill(BLACK)
        battleScene.shopIntro()
        global wallet
        global playerItem
        screen.fill(BLACK)
        shopTitle = "Benny Emporium of Goods"
        shopRender = font.render(shopTitle, True, WHITE)
        screen.blit(shopRender,(-370+30*15,40))
        pygame.display.update()
        clock.tick(60)
        shopChoice = 0
        while True:
            screen.fill(BLACK)
            shopTitle = "Benny Emporium of Goods"
            shopRender = font.render(shopTitle, True, WHITE)
            screen.blit(shopRender,(-370+30*15,40))
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                elif event.type == KEYDOWN:
                    if (event.key == K_RIGHT) and shopChoice < 2:
                        shopChoice +=1
                    elif (event.key == K_LEFT) and shopChoice > 0:
                        shopChoice -=1
                    elif (event.key == K_SPACE):
                        print(shopChoice)
                        #buy
            pygame.display.update()
            clock.tick(60)

    def buyItem():
        pass
        
        
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
