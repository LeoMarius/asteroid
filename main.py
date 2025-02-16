# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *



def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shoots = pygame.sprite.Group()


    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shoots,updatable,drawable)
    

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    asteroid_field = AsteroidField()

    dt = 0


    while True :

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for object in updatable:
            object.update(dt)

        for asteroid in asteroids :
            if player.collides_with(asteroid):
                print("Game Over!")
                return
            
            for bullet in shoots:
                if asteroid.collides_with(bullet):
                    bullet.kill()
                    asteroid.split()


        for object in drawable:
            object.draw(screen)




        pygame.display.flip()
        dt = clock.tick(60) / 1000





if __name__ == "__main__":
    main()