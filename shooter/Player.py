from Constants import Constants
from common.Constants import Constants as C
from Bullets import Bullets
import pygame
import os
from Enemy import Enemy


class Player:
    pressed_keys = {"up": False, "left": False, "down": False, "right": False}
    velocity = 6

    def __init__(self, surface):
        self.surface = surface
        self.bullets = Bullets(surface, 10, 0.2)
        self.enemy = Enemy(3, surface)
        self.player_img = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "shooter", "plane.png"))
        self.player_img = pygame.transform.scale(self.player_img, (Constants.player_width, Constants.player_height))
        self.position = ((surface.get_width()/2) - (Constants.player_width/2), surface.get_height() - (Constants.player_height + 10))

    def draw(self):
        self.update_move()
        self.surface.fill((255, 255, 255))
        self.bullets.update(self.position)
        self.enemy.update(self.bullets.bullets)
        self.surface.blit(self.player_img, self.position, area=None, special_flags=0)
#         self.surface.fill((255, 255, 255))

    def key_event(self, event):
        if event.scancode == C.key_code_up:
            self.pressed_keys["up"] = ({True: True, False: False}[event.type == pygame.KEYDOWN])
        if event.scancode == C.key_code_left:
            self.pressed_keys["left"] = ({True: True, False: False}[event.type == pygame.KEYDOWN])
        if event.scancode == C.key_code_right:
            self.pressed_keys["right"] = ({True: True, False: False}[event.type == pygame.KEYDOWN])
        if event.scancode == C.key_code_down:
            self.pressed_keys["down"] = ({True: True, False: False}[event.type == pygame.KEYDOWN])
        pass

    def update_move(self):
        x = self.position[0]
        y = self.position[1]
        s = self.velocity
        if self.pressed_keys["up"]:
            x,y = x, y - s
        if self.pressed_keys["left"]:
            x,y = x - s, y
        if self.pressed_keys["down"]:
            x,y = x, y + s
        if self.pressed_keys["right"]:
            x,y = x + s, y
        self.set_position((x, y))

    def set_position(self, position):
        if self.check_surface_bounds(position):
            self.position = position
        return False

    def check_surface_bounds(self, position):
        x = position[0]
        y = position[1]
        w = self.surface.get_width()
        h = self.surface.get_height()
        pw = Constants.player_width
        ph = Constants.player_height
        if x < 0 or x+pw > w:
            return False
        if y < 0 or y+ph > h:
            return False
        return True
