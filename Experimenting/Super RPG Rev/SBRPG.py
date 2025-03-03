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
    global clock, screen, font, delta, transitionScreen

    pygame.init()
    font = pygame.font.Font("Fonts/BennyFont.ttf", 24)
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    transitionScreen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Super Benny RPG!")
    delta = clock.tick(FPS)/100
    while True:
        introGame()
        chooseYourBenny()

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
    #To do, make a benny select thing in the while function with a cursor pointing to the different benny types
    while True:
        if checkKey():
            pygame.event.get()
            return
        

#Scuffed
def screenTransition():
    currSize = 10
    for i in range(50):
        currSize += 25
        pygame.draw.circle(transitionScreen, BLACK, (400,200),currSize,0)
        pygame.display.update()
        clock.tick(60)
        
if __name__ == '__main__':
    main()
