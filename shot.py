import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        CircleShape.__init__(self, x, y, SHOT_RADIUS)

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.circle(
            screen,
            "white",
            (int(self.position.x), int(self.position.y)),
            SHOT_RADIUS,
            2,
        )

    def update(self, dt):
        # sub-classes must override
        self.position += self.velocity * dt