import json
import math
import pygame
from car import Car

WIDTH, HEIGHT = 1200, 800
FPS = 60

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    track = pygame.image.load("track_final.png").convert()
    with open("best_brain.json") as f:
        brain = json.load(f)
    car = Car(130, 450, math.radians(270), brain)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if car.alive:
            car.think(track)

        screen.blit(track, (0, 0))
        car.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()