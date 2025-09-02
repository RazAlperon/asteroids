# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *






def main():

    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # update world
        updatable.update(dt)

        for a in asteroids:
            if player.collisionDetection(a):
                print("Game over!")
                sys.exit()

            for s in shots:
                if s.collisionDetection(a):
                    s.kill()
                    children = a.split()
                    asteroids.add(children)
                    updatable.add(children)
                    drawable.add(children)
        
        # render
        screen.fill("black")
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000  # seconds since last frame


if __name__ == "__main__":
    main()
