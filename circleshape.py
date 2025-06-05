import pygame
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        vectors = self.triangle()
        points = [ (point.x, point.y) for point in vectors ]
        pygame.draw.polygon(screen, "white", points, 2)

    def update(self, dt):
        # sub-classes must override
        pass

    def triangle(self):
        pass