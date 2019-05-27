import pygame
import os
from Constants import Constants
from common.Utils import Utils
import time
import random


class Enemy:

    def __init__(self, velocity, surface, frequency=0.3):
        self.velocity = velocity
        self.enemies_images = []
        self.surface = surface
        self.last_spawned = 0
        self.frequency = frequency
        self.enemies = []
        self.enemies_imgs = []
        self.max_spawn_x = self.surface.get_width() - Constants.enemy_width
        for enemy in Constants.enemies:
            i = Utils.load_image("shooter", enemy)
            self.enemies_images.append(pygame.transform.scale(i, (Constants.enemy_width, Constants.enemy_height)))
        self.blast_img = Utils.load_image("shooter", "blast.png")
        self.blast_img = pygame.transform.scale(self.blast_img, (Constants.enemy_width, Constants.enemy_height))
        self.dead_sound = pygame.mixer.Sound(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "shooter", "blast.wav"))
        self.dead_sound.set_volume(0.3)

    def add_enemy(self):
        x = random.randint(0, self.max_spawn_x)
        self.enemies.append((x, 0))
        self.enemies_imgs.append(self.get_random_enemy())

    def get_random_enemy(self):
        rand = random.randint(0, 3)
        return self.enemies_images[rand]

    def draw(self, to_be_destroyed):
        to_be_removed = []
        for i in range(len(self.enemies)):
            enemy = self.enemies[i]
            enemy_img = self.enemies_imgs[i]
            if enemy not in to_be_destroyed:
                self.surface.blit(enemy_img, enemy)
                if enemy[1] + self.velocity > self.surface.get_height():
                    to_be_removed.append(i)
                else:
                    self.enemies[i] = (enemy[0], enemy[1] + self.velocity)
            else:
                self.surface.blit(self.blast_img, enemy)
                self.dead_sound.play()
                to_be_removed.append(i)
        to_be_removed = list(dict.fromkeys(to_be_removed))
        to_be_removed.sort()
        to_be_removed.reverse()
        for i in to_be_removed:
            try:
                del self.enemies[i]
                del self.enemies_imgs[i]
            except IndexError:
                print self.enemies, i

    def update(self, bullets):
        enemy_to_be_destroyed = []
        bullet_to_be_destroyed = []
        for enemy in self.enemies:
            x1 = enemy[0]
            y1 = enemy[1]
            w1 = Constants.enemy_width
            h1 = Constants.enemy_height
            for bullet in bullets.bullets:
                x2 = bullet[0]
                y2 = bullet[1]
                w2 = Constants.bullet_width
                h2 = Constants.enemy_height
                if Utils.is_collide(x1, y1, w1, h1, x2, y2, w2, h2):
                    enemy_to_be_destroyed.append(enemy)
                    bullet_to_be_destroyed.append(bullet)
        if time.time() - self.last_spawned >= self.frequency:
            self.add_enemy()
            self.last_spawned = time.time()
        bullets.remove_bullet(bullet_to_be_destroyed)
        self.draw(enemy_to_be_destroyed)

