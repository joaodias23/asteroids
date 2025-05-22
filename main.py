import pygame
from constants import *

def main():
    pygame.init()
    print("'Starting Asteroids!'")
    
if __name__ == "__main__":
    main()

print(f"'Screen width: {SCREEN_WIDTH}'")
print(f"'Screen height: {SCREEN_HEIGHT}'")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def game_loop():
    while 1 == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()

game_loop()