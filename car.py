import math
import pygame

SENSOR_RANGE = 200

class Car:
    def __init__(self, x, y, angle=0.0):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 0.0
        self.steer = 0.0
        self.start = (self.x, self.y, self.angle)
        self.sensor_offsets = [-90, -60, -30, 0, 30, 60, 90]
        
    def update(self, gas, brake, left, right, handbrake=False):
        # TODO: Gas/Bremse -> speed ändern
        if gas:
            self.speed += 0.2
        if brake:
            self.speed -= 0.3
        self.speed *= 0.99
        self.speed = max(0, min(self.speed, 6))
        # TODO: Space bremst smooth
        if handbrake:
            self.speed *= 0.95
        # TODO: Links/Rechts -> angle ändern (nur wenn speed > 0)
        turn_speed = 0.04
        steer_smoothing = 0.1
        target = 0
        if left:
            target -= 1
        if right:
            target += 1
        self.steer += (target - self.steer) * steer_smoothing
        self.angle += self.steer * min(turn_speed * 3, turn_speed * self.speed)
        # TODO: Position aus angle und speed berechnen
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
    
    def on_track(self, track):
        for px, py in self.get_corners():
            x, y = int(px), int(py)
            if x < 0 or x >= track.get_width() or y < 0 or y >= track.get_height():
                return False
            if track.get_at((x, y))[:3] != (255, 255, 255):
                return False
        return True
    
    def reset(self):
        self.x, self.y, self.angle = self.start
        self.speed = 0.0
        self.steer = 0.0
        
    def get_corners(self):
        corners = [(16, 8), (16, -8), (-16, -8), (-16, 8)]
        points = []
        for lx, ly in corners:
            px = self.x + lx * math.cos(self.angle) - ly * math.sin(self.angle)
            py = self.y + lx * math.sin(self.angle) + ly * math.cos(self.angle)
            points.append((px, py))
        return points

    def draw(self, screen):
        points = self.get_corners()
        pygame.draw.polygon(screen, (220, 40, 40), points)
        
    def cast_ray(self, track, ray_angle, max_dist=SENSOR_RANGE):
        for d in range(0, max_dist):
            x = int(self.x + math.cos(ray_angle) * d)
            y = int(self.y + math.sin(ray_angle) * d)
            if x < 0 or x >= track.get_width() or y < 0 or y >= track.get_height():
                return d
            if track.get_at((x, y))[:3] != (255, 255, 255):
                return d
        return SENSOR_RANGE
    
    def get_sensors(self, track):
        distance = []
        for offset in self.sensor_offsets:
            ray_angle = self.angle + math.radians(offset)
            distance.append(self.cast_ray(track, ray_angle) / SENSOR_RANGE)
        return distance
    
    def draw_sensor(self, screen, track):
        for offset in self.sensor_offsets:
            ray_angle = self.angle + math.radians(offset)
            d = self.cast_ray(track, ray_angle)
            end_x = self.x + math.cos(ray_angle) * d
            end_y = self.y + math.sin(ray_angle) * d
            pygame.draw.line(screen, (255, 220, 0), (self.x, self.y), (end_x, end_y), 2)