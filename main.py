import pygame
import math
from car import Car

WIDTH, HEIGHT = 1200, 800
FPS = 60

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True
    car = Car(130, 450, math.radians(270))
    track = pygame.image.load("track.png").convert()
    while running:
        # 1. Inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # 2. Physik / Update
        car.update(pygame.key.get_pressed())
        print(car.get_sensors(track))
        if not car.on_track(track):
            car.reset()
        # 3. Rendering
        screen.blit(track, (0, 0))
        car.draw(screen)
        car.draw_sensor(screen, track)
        pygame.display.flip()
        
        clock.tick(FPS)
        
    pygame.quit()

if __name__ == "__main__":
    main()