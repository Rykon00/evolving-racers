import math
import pygame

class Car:
    def __init__(self, x, y, angle=0.0):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 0.0
        
    def update(self, keys):
        # TODO: Gas/Bremse -> speed ändern
        if keys[pygame.K_w]:
            self.speed += 0.2
        if keys[pygame.K_s]:
            self.speed -= 0.3
        # TODO: Links/Rechts -> angle ändern (nur wenn speed > 0)
        if keys[pygame.K_a]:
            self.angle -= 0.1
        if keys[pygame.K_d]:
            self.angle += 0.1
        # TODO: Position aus angle und speed berechnen
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
    
    def draw(self, screen):
        corners = [(16, 8), (16, -8), (-16, -8), (-16, 8)]
        points = []
        for lx, ly in corners:
            px = self.x + lx * math.cos(self.angle) - ly * math.sin(self.angle)
            py = self.y + lx * math.sin(self.angle) + ly * math.cos(self.angle)
            points.append((px, py))
        pygame.draw.polygon(screen, (220, 40, 40), points)