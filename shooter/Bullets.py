import pygame
import os
import time
from Constants import Constants


class Bullets:
    
    def __init__(self, surface, velocity, frequency):
        self.surface = surface
        self.velocity = velocity
        self.frequency = frequency
        self.last_fired = time.time()
        self.bullets = []
        self.bullet_img = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "shooter", "bullet.png"))
        self.bullet_img = pygame.transform.scale(self.bullet_img, (Constants.bullet_width, Constants.bullet_height))
    
    # position = Position of the plane
    def add_bullets(self, position):
        positions = self.calculate_bullets_position(position)
        for i in positions:
            self.bullets.append(i)

    def remove_bullet(self, to_be_destroyed):
        for i in to_be_destroyed:
            self.bullets.remove(i)

    def draw(self):
        to_be_removed = []
        for i in range(len(self.bullets)):
            bullet = self.bullets[i]
            self.surface.blit(self.bullet_img, bullet, area=None, special_flags=0)
            if bullet[1] <= 0:
                to_be_removed.append(i)
            else:
                self.bullets[i] = (bullet[0], bullet[1] - self.velocity)
        for i in to_be_removed:
            del self.bullets[i]
            
    # position = Position of the plane
    def update(self, position):
        if time.time() - self.last_fired >= self.frequency:
            self.add_bullets(position)
            self.last_fired = time.time()
        self.draw()

    def calculate_bullets_position(self, position):
        p_x = position[0]
        p_y = position[1]
        p_w = Constants.player_width
        b_w = Constants.bullet_width
        x1 = p_x + (p_w / 4) - (b_w / 2)
        y1 = p_y
        x2 = (p_x + p_w) - (p_w / 4) - (b_w / 2)
        y2 = p_y
        return [(x1, y1), (x2, y2)]
