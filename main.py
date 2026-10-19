import pygame
import math
from car import Car
from brain import create_network, forward

WIDTH, HEIGHT = 1200, 800
FPS = 60
USE_RULE = True   # True: einfache Test-Regel fährt, False: das (noch zufällige) Netz fährt

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True
    car = Car(130, 450, math.radians(270))
    track = pygame.image.load("track.png").convert()
    net = create_network([7, 15, 15, 4])
    while running:
        # 1. Inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 2. Physik / Update
        sensors = car.get_sensors(track)
        if USE_RULE:
            # [Gas, Bremse, Links, Rechts]; Strahlen bei -30 Grad (Nr. 2) und +30 Grad (Nr. 4)
            out = [1, -1, sensors[2] - sensors[4], sensors[4] - sensors[2]]
        else:
            out = forward(sensors, net)
        car.update(out[0] > 0, out[1] > 0, out[2] > 0, out[3] > 0)
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