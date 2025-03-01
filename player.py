import pygame
import constants
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen,(50, 255, 80) ,self.triangle(),2)

    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_MOVE_SPEED * dt

    def shoot(self, position, dt):
        x = position.x
        y = position.y
        _shot = Shot(x, y, constants.SHOT_RADIUS)
        _shot.velocity = (pygame.Vector2(0,1).rotate(self.rotation) * constants.PLAYER_SHOOT_SPEED)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shoot_cooldown -= dt
        
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_SPACE]:
            if self.shoot_cooldown < 0:
                self.shoot(self.position, dt)
                self.shoot_cooldown = constants.PLAYER_SHOOT_COOLDOWN
            else:
                return
        