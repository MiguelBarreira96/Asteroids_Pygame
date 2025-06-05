import pygame
from circleshape import *
import random
from score import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        if self.radius == ASTEROID_MAX_RADIUS:
            self.points = 1
        elif self.radius == ASTEROID_MAX_RADIUS - ASTEROID_MIN_RADIUS:
            self.points = 2
        else:
            self.points = 3

    def get_points(self):
        return self.points
    
    def draw(self, screen):
        pygame.draw.circle(screen, "dark red", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, score, asteroids):
        self.kill()
        score.add_points(self.get_points())

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        new_direction = self.velocity.rotate(angle)
        op_new_direction = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid1.velocity = new_direction * 1.2
        asteroid2.velocity = op_new_direction * 1.2

        asteroids.add(asteroid1)
        asteroids.add(asteroid2)