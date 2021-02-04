import pygame, pygame.freetype, sys, time, random
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (234, 153, 153)
BROWN = (102, 0, 0)
GREEN = (102, 204, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 255, 255)
PURPLE = (53, 28, 117)

MAX_AMOUNT = 15

def button(display, x, y, w, h, color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(display, BLACK, (x, y, w, h), 2, 2, 2, 2, 2)

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(display, color, (x, y, w, h))

def text(display, msg, x, y):
    font = pygame.freetype.SysFont('arial', 20)
    font.render_to(display, (x // 2, y // 2), msg, BLACK)
    pygame.display.flip()

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

def selectCurrent():
    print("current")

def showCurrent(DISPLAY):
    randomNumber = random.randint(0, 5)
    if randomNumber == 0:
        button(DISPLAY, 540, 230, 100, 100, RED, selectCurrent)
    elif randomNumber == 1:
        button(DISPLAY, 540, 230, 100, 100, BLUE, selectCurrent)
    elif randomNumber == 2:
        button(DISPLAY, 540, 230, 100, 100, GREEN, selectCurrent)
    elif randomNumber == 3:
        button(DISPLAY, 540, 230, 100, 100, BROWN, selectCurrent)
    elif randomNumber == 4:
        button(DISPLAY, 540, 230, 100, 100, PURPLE, selectCurrent)
    elif randomNumber == 5:
        button(DISPLAY, 540, 230, 100, 100, YELLOW, selectCurrent)

def calculateTime(start, end):
    return end - start

def calculateDelay():
    #Actual - Expected
    return "00:10"

def main():
    pygame.init()
    size = (width, height) = (685, 400)
    DISPLAY = pygame.display.set_mode(size)
    pygame.display.set_caption('Bus Stop Manager')

    global start
    global end

    start = time.time()

    #clock = pygame.time.Clock()

    DISPLAY.fill(WHITE)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        #print("Start: {}".format(start))
        end = time.time()
        if(calculateTime(start, end) >= 10):
            #print(calculateTime(start, end))
            print("Display current")
            start = time.time()
            showCurrent(DISPLAY)
                    
        button(DISPLAY, 15, 25, 100, 100, RED, selectRed)
        button(DISPLAY, 15 + (110 * 1), 25, 100, 100, BROWN, selectBrown)
        button(DISPLAY, 15 + (110 * 2), 25, 100, 100, GREEN, selectGreen)
        button(DISPLAY, 15 + (110 * 3), 25, 100, 100, YELLOW, selectYellow)
        button(DISPLAY, 15 + (110 * 4), 25, 100, 100, BLUE, selectBlue)
        button(DISPLAY, 15 + (110 * 5), 25, 100, 100, PURPLE, selectPurple)

        text(DISPLAY, "Expected Arrival: ", 100, 500)
        text(DISPLAY, "Actual Arrival: ", 100, 550)
        text(DISPLAY, "Delay: "+ calculateDelay(), 100, 600)

        text(DISPLAY, "Current Stop:", 1085, 410)
        
        pygame.display.update()
        #clock.tick(15)

if __name__ == "__main__":
    main()
