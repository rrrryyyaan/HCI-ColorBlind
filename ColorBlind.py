import pygame, pygame.freetype, sys, time, random, csv
from pygame.locals import *
from os import path

# Color Blind Bus Stop Interface
# Project 1
# @Authors Ryan, Sam
# Date Created: 2/3/2021

# currentColor values
# 0 = red, 1 = brown, 2 = green, 3 = yellow, 4 = blue, 5 = purple

pygame.init()
size = (width, height) = (685, 400)
DISPLAY = pygame.display.set_mode(size)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (234, 153, 153)
BROWN = (102, 0, 0)
GREEN = (102, 204, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 255, 255)
PURPLE = (53, 28, 117)

MAX_AMOUNT = 31


def export(current, pressed, delay):
    if (path.exists('testResults.csv')):
        with open ('testResults.csv', 'a') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([colorToString(current),(pressed), delay])
    else:
        with open ('testResults.csv', 'w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([colorToString(current), (pressed), delay])

def button(x, y, w, h, color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(DISPLAY, BLACK, (x, y, w, h), 2, 2, 2, 2, 2)

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(DISPLAY, color, (x, y, w, h))

def text(msg, x, y):
    font = pygame.freetype.SysFont('arial', 20)
    font.render_to(DISPLAY, (x // 2, y // 2), msg, BLACK)
    pygame.display.flip()

def erase(x, y, w, h):
    pygame.draw.rect(DISPLAY, WHITE, (x, y, w, h))

def colorToString(colorInt):
    if colorInt == 0:
        return "Red"
    if colorInt == 1:
        return "Brown"
    if colorInt == 2:
        return "Green"
    if colorInt == 3:
        return "Yellow"
    if colorInt == 4:
        return "Blue"
    if colorInt == 5:
        return "Purple"

def selectRed():
    if currentColor == 0:
        displayActual(False)
    export(currentColor, "Red", calculateDelay())
        
def selectBlue():
    if currentColor == 4:
        displayActual(False)
    export(currentColor, "Blue", calculateDelay())

def selectGreen():
    if currentColor == 2:
        displayActual(False)
    export(currentColor, "Green", calculateDelay())

def selectPurple():
    if currentColor == 5:
        displayActual(False)
    export(currentColor, "Purple", calculateDelay())

def selectYellow():
    if currentColor == 3:
        displayActual(False)
    export(currentColor, "Yellow", calculateDelay())

def selectBrown():
    if currentColor == 1:
        displayActual(False)
    export(currentColor, "Brown", calculateDelay())

def displayCurrent():
    global currentColor
    randomNumber = random.randint(0, 5)
    while(currentColor == randomNumber):
        randomNumber = random.randint(0, 5)
    if randomNumber == 0:
        pygame.draw.rect(DISPLAY, RED, (540, 230, 100, 100))
    elif randomNumber == 1:
        pygame.draw.rect(DISPLAY, BROWN, (540, 230, 100, 100))
    elif randomNumber == 2:
        pygame.draw.rect(DISPLAY, GREEN, (540, 230, 100, 100))
    elif randomNumber == 3:
        pygame.draw.rect(DISPLAY, YELLOW, (540, 230, 100, 100))
    elif randomNumber == 4:
        pygame.draw.rect(DISPLAY, BLUE, (540, 230, 100, 100))
    elif randomNumber == 5:
        pygame.draw.rect(DISPLAY, PURPLE, (540, 230, 100, 100))
    currentColor = randomNumber

def displayAllStops():
    button(15, 25, 100, 100, RED, selectRed)
    button(15 + (110 * 1), 25, 100, 100, BROWN, selectBrown)
    button(15 + (110 * 2), 25, 100, 100, GREEN, selectGreen)
    button(15 + (110 * 3), 25, 100, 100, YELLOW, selectYellow)
    button(15 + (110 * 4), 25, 100, 100, BLUE, selectBlue)
    button(15 + (110 * 5), 25, 100, 100, PURPLE, selectPurple)

def displayExpected(init):
    if init == True:
        text("Expected Arrival:", 100, 500)
    else:
        erase(174, 245, 100, 22)
        text("Expected Arrival: {:0.2f}".format(calculateExpected()), 100, 500)

def displayActual(init):
    if init == True:
        text("Actual Arrival: ", 100, 550)
    else:
        erase(154, 270, 100, 22)
        text("Actual Arrival: {:0.2f}".format(calculateActual()), 100, 550)
        displayDelay(False)

def displayDelay(init):
    if init == True:
        text("Delay:", 100, 600)
    else:
        erase(97, 295, 230, 22)
        text("Delay: -{:0.2f}".format(calculateDelay()), 100, 600)

def displayAllComponents():
    displayAllStops()
    displayExpected(True)
    displayActual(True)
    displayDelay(True)

def displayArriveMessage():
    text("You are arriving shortly!", 500, 650)

# Handles selecting a new bus route every 10 seconds
def calculateTotalTime():
    return end - start

def calculateExpected():
    return end - expected

def calculateActual():
    return end - actual

# Calculates the delay from the bus route displaying to the user
# selecting the correct route
def calculateDelay():
    return end - expectedEnd

def main():
    pygame.display.set_caption('Bus Stop Manager')
    DISPLAY.fill(WHITE)

    global start
    global end
    global expected
    global actual
    global currentColor
    global expectedEnd

    start = time.time()
    expected = time.time()
    actual = time.time()
    currentColor = -1
    iterations = 0

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        end = time.time()
        elapsedTime = calculateTotalTime()
        if(elapsedTime >= 3 and elapsedTime < 7):
            displayArriveMessage()
        elif(elapsedTime >= 7):
            start = time.time()
            erase(240, 320, 200, 30)
            actual = time.time() - calculateExpected()
            expectedEnd = time.time()
            displayExpected(False)
            displayCurrent()
            iterations += 1
                    
        displayAllComponents()
        
        text("Current Stop", 1085, 410)
        
        pygame.display.update()
        
        #Code to stop after a certain amount of iterations
        if iterations == MAX_AMOUNT:
            text("You've completed your routes! Thank you!", 400, 650)
            erase(540, 230, 100, 100)
            run = False

    while run == False: #So you can still quit the game after it's finished
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
