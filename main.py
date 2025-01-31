import pygame
from constants import * 
from player import Player
from asteroidfield import AsteroidField 
from asteroids import Asteroid
from circleshape import Shot
import sys

def main():
    pygame.init() # initialize pygame
    pygame.font.init()
    font = pygame.font.Font(None, 36)
    score = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    containers = shots

    updatable.add(shots)
    drawable.add(shots)
    
    clock_var = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #GUI Window
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()
    player = Player(x, y)
    
    infinity = float('inf')
    i = 0
    while i < infinity:
        i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collisions(asteroid):
                print("Game Over!")
                sys.exit()
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)

        score += dt
        score_text = font.render(f"Score: {int(score)}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        pygame.display.flip()
        dt = clock_var.tick(60) / 1000
        
        
    
    print("Starting asteroids!")

    
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")






if __name__ == "__main__":
    main()