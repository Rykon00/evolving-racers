import math
import pygame



class Car:
    def __init__(self, x, y, angle=0.0):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 0.0
        self.steer = 0.0
        
    def update(self, keys):
        # TODO: Gas/Bremse -> speed ändern
        if keys[pygame.K_w]:
            self.speed += 0.2
        if keys[pygame.K_s]:
            self.speed -= 0.3
        self.speed *= 0.99
        self.speed = max(-2, min(self.speed, 6))
        # TODO: Space bremst smooth
        if keys[pygame.K_SPACE]:
            self.speed *= 0.95
        # TODO: Links/Rechts -> angle ändern (nur wenn speed > 0)
        turn_speed = 0.04
        steer_smoothing = 0.1
        target = 0
        if keys[pygame.K_a]:
            target -= 1
        if keys[pygame.K_d]:
            target += 1
        self.steer += (target - self.steer) * steer_smoothing
        self.angle += self.steer * min(turn_speed * 3, turn_speed * self.speed)
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