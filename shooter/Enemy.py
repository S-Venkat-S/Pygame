import pygame
import os
from Constants import Constants
from common.Utils import Utils
import time
import random


class Enemy:

    def __init__(self, velocity, surface, frequency=0.7):
        self.velocity = velocity
        self.surface = surface
        self.last_spawned = 0
        self.frequency = frequency
        self.enemies = [(160, 0)]
        self.max_spawn_x = self.surface.get_width() - Constants.enemy_width
        self.enemy_img = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "shooter", "enemy_1.png"))
        self.enemy_img = pygame.transform.scale(self.enemy_img, (Constants.enemy_width, Constants.enemy_height))
        self.blast_img = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "shooter", "blast.png"))
        self.blast_img = pygame.transform.scale(self.blast_img, (Constants.enemy_width, Constants.enemy_height))

    def add_enemy(self):
        x = random.randint(0, self.max_spawn_x)
        self.enemies.append((x, 0))

    def draw(self, to_be_destroyed):
        to_be_removed = []
        for i in range(len(self.enemies)):
            enemy = self.enemies[i]
            if enemy not in to_be_destroyed:
                self.surface.blit(self.enemy_img, enemy)
                if enemy[1] + self.velocity > self.surface.get_height():
                    to_be_removed.append(i)
                else:
                    self.enemies[i] = (enemy[0], enemy[1] + self.velocity)
            else:
                self.surface.blit(self.blast_img, enemy)
                to_be_removed.append(i)
        for i in to_be_removed:
            del self.enemies[i]

    def update(self, bullets):
        to_be_destroyed = []
        for enemy in self.enemies:
            x1 = enemy[0]
            y1 = enemy[1]
            w1 = Constants.enemy_width
            h1 = Constants.enemy_height
            for bullet in bullets:
                x2 = bullet[0]
                y2 = bullet[1]
                w2 = Constants.bullet_width
                h2 = Constants.enemy_height
                if Utils.is_collide(x1, y1, w1, h1, x2, y2, w2, h2):
                    print (x1, y1, w1, h1, x2, y2, w2, h2)
                    to_be_destroyed.append(enemy)
        if time.time() - self.last_spawned >= self.frequency:
            self.add_enemy()
            self.last_spawned = time.time()
        self.draw(to_be_destroyed)

