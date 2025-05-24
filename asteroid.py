import pygame
import random
import math
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)
        self._generate_shape()

    def _generate_shape(self):
        num_points = 20
        angle_step = 2 * math.pi / num_points
        base_radius = self.radius
        self.render_points = []

        for i in range(num_points):
            angle = i * angle_step
            fluctuation = (math.cos(i * 1.5) * 0.15 + 0.85)
            offset = base_radius * fluctuation * random.uniform(0.9, 1.1)
            x = math.cos(angle) * offset
            y = math.sin(angle) * offset
            self.render_points.append(pygame.Vector2(x, y))

    def draw(self, screen):

        transformed = [self.position + point for point in self.render_points]
        int_points = [(int(p.x), int(p.y)) for p in transformed]

        base_color = pygame.Color(120, 120, 120)
        light_color = pygame.Color(180, 180, 180)
        
        glow_surf = pygame.Surface((self.radius * 4, self.radius * 4), pygame.SRCALPHA)
        glow_center = (glow_surf.get_width() // 2, glow_surf.get_height() // 2)
        scaled_points = [(p.x - self.position.x + glow_center[0], p.y - self.position.y + glow_center[1]) for p in transformed]

        pygame.draw.polygon(glow_surf, (base_color.r, base_color.g, base_color.b, 50), scaled_points)
        screen.blit(glow_surf, (self.position.x - glow_center[0], self.position.y - glow_center[1]))

        pygame.draw.polygon(screen, base_color, int_points)

        highlight_points = []
        for p in self.render_points:
            scaled_point = p * 0.85
            highlight_points.append(self.position + scaled_point)
        highlight_int_points = [(int(p.x), int(p.y)) for p in highlight_points]
        pygame.draw.polygon(screen, light_color, highlight_int_points)

        pygame.draw.polygon(screen, (220, 220, 220), int_points, 2)
        
    def update(self, dt):
        # sub-classes must override
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        randomized = random.uniform(20, 50)

        vel1 = self.velocity.rotate(randomized)
        vel2 = self.velocity.rotate(-randomized)
        vel1 *= 1.2
        vel2 *= 1.2

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        offset = vel1.normalize() * new_radius
        new_pos1 = self.position + offset

        offset2 = vel2.normalize() * new_radius
        new_pos2 = self.position + offset2

        new_asteroid = Asteroid(new_pos1.x, new_pos1.y, new_radius)
        other_new_asteroid = Asteroid(new_pos2.x, new_pos2.y, new_radius)
        new_asteroid.velocity = vel1
        other_new_asteroid.velocity = vel2