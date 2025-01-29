import pygame
from constants import * 

def main():
    pygame.init() # initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #GUI Window
    infinity = float('inf')
    i = 0
    while i < infinity:
        i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        print(screen)
        pygame.display.flip()
    
    print("Starting asteroids!")

    
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")






if __name__ == "__main__":
    main()