import pygame
from circleshape import *
from player import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "gold", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt