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
        # TODO: Links/Rechts -> angle ändern (nur wenn speed > 0)
        # TODO: Position aus angle und speed berechnen
        pass
    
    def draw(self, screen):
        # TODO:  Rechteck gedreht zeichnen
        pass
