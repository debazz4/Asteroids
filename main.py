# this allows us to use code from the open-source
# pygame library throughout this file

import pygame
from constants import *

def main():
    # initialize pygame modules
    pygame.init()

    # display.set_mode() to get a new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        pygame.display.flip()
    
    #output = f"Starting asteroids! \nScreen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}"
    #print(output)

if __name__ == "__main__":
    main()