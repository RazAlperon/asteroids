import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pos = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, "white", pos, int(self.radius), 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
        else:
            r = random.uniform(20, 50)
            r1 = self.velocity.rotate(r)
            r2 = self.velocity.rotate(-r)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x, self.position.y, new_radius)
            a2 = Asteroid(self.position.x, self.position.y, new_radius)
            a1.velocity=r1*1.2
            a2.velocity=r2*1.2
            return [a1, a2]