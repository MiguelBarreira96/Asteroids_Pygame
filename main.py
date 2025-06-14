import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
import sys
from score import *

def main():
    pygame.init()
    dt = 0
    score = Score()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    print("Large asteroids gives 1 point, medium asteroids give 2 and small asteroids give 3.")
    print("=========================")
    
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Shot.containers = (updatable, drawables, shots)
    Asteroid.containers = (asteroids, updatable, drawables)
    Player.containers = (updatable, drawables)

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for drawable in drawables:
            drawable.draw(screen)
        
        updatable.update(dt)
        pygame.display.flip()  #Update step
        for asteroid in asteroids:
            if asteroid.colide(player):
                print("Good job!!!")
                print(f"Your score was: {score.get_score()}")
                print("=========================")
                sys.exit("Game over!")
                
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.colide(shot):
                    asteroid.split(score, asteroids)
                    shot.kill()
                    

        if (player.position.x > SCREEN_WIDTH
            or player.position.x < 0
            or player.position.y > SCREEN_HEIGHT
            or player.position.y < 0):
            print("Good job!!!")
            print(f"Your score was: {score.get_score()}")
            print("=========================")
            sys.exit("Game over!")
        dt = clock.tick(60) / 1000

        


if __name__ == "__main__":
    main()