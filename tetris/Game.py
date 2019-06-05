import pygame
from common.Utils import Utils
from Constants import Constants


class Game:

    def __init__(self, surface):
        self.surface = surface
        self.background = Utils.load_image("tetris", "bg.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (Constants.tile_width, Constants.tile_width))
        pass

    def draw_bg(self):
        for i in range(0, 10):
            for j in range(0, 20):
                self.surface.blit(self.background, (i*Constants.tile_width, j*Constants.tile_width))

    def update(self):
        self.draw_bg()
        # self.surface.blit(self.background, (0, 0))

