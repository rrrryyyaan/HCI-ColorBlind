import pygame, sys
from pygame.locals import *

def main():
    pygame.init()
    DISPLAY = pygame.display.set_mode((1000, 400), 0, 32)

    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BROWN = (127, 96, 0)
    GREEN = (56, 87, 35)
    YELLOW = (255, 255, 0)
    BLUE = (0, 47, 142)
    PURPLE = (112, 48, 160)

    DISPLAY.fill(WHITE)

    pygame.draw.rect(DISPLAY, RED, (50, 150, 50, 50))
    pygame.draw.rect(DISPLAY, BROWN, (150, 150, 50, 50))
    pygame.draw.rect(DISPLAY, GREEN, (250, 150, 50, 50))
    pygame.draw.rect(DISPLAY, YELLOW, (350, 150, 50, 50))
    pygame.draw.rect(DISPLAY, BLUE, (450, 150, 50, 50))
    pygame.draw.rect(DISPLAY, PURPLE, (550, 150, 50, 50))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == "__main__":
    main()
