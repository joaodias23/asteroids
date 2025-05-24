import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        CircleShape.__init__(self, x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c] 
    
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)
        return self.rotation
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.timer <= 0:
                self.shoot()
        self.timer -= dt

    def shoot(self):
        new_shot = Shot(self.position.x, self.position.y)
        velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        new_shot.velocity = velocity * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN
    
    def draw(self, screen):

        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90)
        
       
        nose = self.position + forward * self.radius
        rear_left = self.position - forward * self.radius + right * self.radius * 0.5
        rear_right = self.position - forward * self.radius - right * self.radius * 0.5

        
        wing_left = self.position - forward * self.radius * 0.6 + right * self.radius
        wing_right = self.position - forward * self.radius * 0.6 - right * self.radius

      
        flame_tip = self.position - forward * self.radius * 1.5

       
        pygame.draw.polygon(screen, (255, 255, 255), [nose, rear_right, rear_left])
        
        
        pygame.draw.line(screen, (100, 100, 255), rear_left, wing_left, 2)
        pygame.draw.line(screen, (100, 100, 255), rear_right, wing_right, 2)

        # Draw rear flame if moving forward
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            pygame.draw.polygon(screen, (255, 165, 0), [rear_left, rear_right, flame_tip])
