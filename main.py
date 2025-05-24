import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from starfield import Starfield

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)
Shot.containers = (updatable, drawable, shots)

def game_loop(screen, clock, dt, player, starfield):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        starfield.update(dt)

        screen.fill((0, 0, 0))
        starfield.draw(screen)

        for draw_obj in drawable:
            draw_obj.draw(screen)

        updatable.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit()

        pygame.display.flip()

        dt = clock.tick(60) / 1000


def main():
    pygame.init()
    print("'Starting Asteroids!'")
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroid_field = AsteroidField()

    starfield = Starfield(SCREEN_WIDTH, SCREEN_HEIGHT, star_count=120)

    game_loop(screen, clock, dt, player, starfield)

if __name__ == "__main__":
    main()
