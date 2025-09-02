# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# import everything from the module
# constants.py into the current file
from constants import *
from circleshape import *
from player import *






def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # update world
        updatable.update(dt)
        
        # render
        screen.fill("black")
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000  # seconds since last frame


if __name__ == "__main__":
    main()
