import pygame
import random

class Starfield:
    def __init__(self, width, height, star_count=100):
        self.width = width
        self.height = height
        self.stars = [
            {
                "pos": pygame.Vector2(random.randint(0, width), random.randint(0, height)),
                "radius": random.choice([1, 1, 2]),
                "speed": random.uniform(5, 20),
            }
            for _ in range(star_count)
        ]

    def update(self, dt):
        for star in self.stars:
            star["pos"].y += star["speed"] * dt
            if star["pos"].y > self.height:
                star["pos"].y = 0
                star["pos"].x = random.randint(0, self.width)

    def draw(self, screen):
        for star in self.stars:
            pygame.draw.circle(screen, (255, 255, 255), (int(star["pos"].x), int(star["pos"].y)), star["radius"])
