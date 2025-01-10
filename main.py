# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
from constants import *



def main():
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True :
        screen.fill("grey")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.display.flip()





if __name__ == "__main__":
    main()