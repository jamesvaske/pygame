import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # Initialize the parent class
        super().__init__(x, y, radius)
        self.radius = radius  # Use radius here specifically for drawing
    
    def draw(self, screen):
        # Use self.position (a Vector2) for center coordinates
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        # Move the asteroid by its velocity over time
        self.position += self.velocity * dt
