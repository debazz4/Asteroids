import pygame
import random
from constants import *
from circleshape import CircleShape
from player import Player

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
#currently working here
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        self.velocity = self.velocity.rotate(random.uniform(-angle, angle))
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = 
        print(angle)
        self.kill()
