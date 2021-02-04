import pygame, sys
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (234, 153, 153)
BROWN = (102, 0, 0)
GREEN = (102, 204, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 255, 255)
PURPLE = (53, 28, 117)

def button(display, x, y, w, h, color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(display, BLACK, (x, y, w, h), 2, 2, 2, 2, 2)

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(display, color, (x, y, w, h))

    #smallText = pygame.font.Font("freesansbold.ttf", 20)
    #textSurf, textRect = text_objects(msg, smallText)
    #textRect.center = ( (x+(w/2)), (y+(h/2)) )
    #gameDisplay.blit(textSurf, textRect)

def selectRed():
    print("red")

def selectBlue():
    print("blue")

def selectGreen():
    print("green")

def selectPurple():
    print("purple")

def selectYellow():
    print("yellow")

def selectBrown():
    print("brown")

def showCurrent():
    print("Showing current stop")

def calculateDelay():
    #Actual - Expected
    print("Delay")

def main():
    pygame.init()
    size = (width, height) = (685, 400)
    DISPLAY = pygame.display.set_mode(size)
    pygame.display.set_caption('Bus Stop Manager')

    #clock = pygame.time.Clock()

    DISPLAY.fill(WHITE)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        button(DISPLAY, 15, 25, 100, 100, RED, selectRed)
        button(DISPLAY, 15 + (110 * 1), 25, 100, 100, BROWN, selectBrown)
        button(DISPLAY, 15 + (110 * 2), 25, 100, 100, GREEN, selectGreen)
        button(DISPLAY, 15 + (110 * 3), 25, 100, 100, YELLOW, selectYellow)
        button(DISPLAY, 15 + (110 * 4), 25, 100, 100, BLUE, selectBlue)
        button(DISPLAY, 15 + (110 * 5), 25, 100, 100, PURPLE, selectPurple)

        
        
        pygame.display.update()
        #clock.tick(15)

if __name__ == "__main__":
    main()
