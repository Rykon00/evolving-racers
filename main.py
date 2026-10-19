import pygame
import json
import random
import math
from car import Car
from brain import crossover, mutate

WIDTH, HEIGHT = 1200, 800
FPS = 60
POPULATION = 50
MAX_FRAMES = 1200   # 20 Sekunden pro Generation
ELITE_KEEP = 3        # die 3 Besten kommen unverändert in die nächste Runde
BREEDING_POOL = 10    # aus den 10 Besten werden Eltern gezogen

def spawn_population(brains=None):
    cars = []
    for i in range(POPULATION):
        brain = None if brains is None else brains[i]
        cars.append(Car(130, 450, math.radians(270), brain))
    return cars

def next_generation(cars):
    ranked = sorted(cars, key=lambda car: car.distance, reverse=True)
    parents = ranked[:BREEDING_POOL]
    brains = [car.brain for car in ranked[:ELITE_KEEP]]
    while len(brains) < POPULATION:
        a, b = random.sample(parents, 2)
        child = crossover(a.brain, b.brain)
        mutate(child)
        brains.append(child)
    return spawn_population(brains)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)
    track = pygame.image.load("track.png").convert()
    cars = spawn_population()
    generation = 1
    frame = 0
    running = True
    record = 0
    while running:
        # 1. Inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 2. Physik / Update
        for car in cars:
            if car.alive:
                car.think(track)
        frame += 1
        alive = sum(1 for car in cars if car.alive)
        if alive == 0 or frame >= MAX_FRAMES:
            best_car = max(cars, key=lambda car: car.distance)
            best = best_car.distance
            print(f"Generation {generation}: beste Strecke {best:.0f}")
            if best > record:
                record = best
                with open("best_brain.json", "w") as f:
                    json.dump(best_car.brain, f)
            cars = next_generation(cars)
            generation += 1
            frame = 0

        # 3. Rendering
        screen.blit(track, (0, 0))
        for car in cars:
            if car.alive:
                car.draw(screen)
        text = font.render(f"Generation {generation}   Autos: {alive}", True, (255, 255, 0))
        screen.blit(text, (10, 10))
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()