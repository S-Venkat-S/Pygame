import pygame
import time
import random
from common.Utils import Utils
from Constants import Constants
from common.Constants import Constants as Cons
from common.colors import Colors as Color
from DataStructure import DataStructure


class Game:

    def __init__(self, surface):
        self.surface = surface
        self.data = DataStructure(Constants.grid_width, Constants.grid_height, 0)
        return

    # Gets the rect size to be filled according to the grid positions.
    # left = width, top = height
    def get_cell_rect(self, left_index, top_index):
        left = left_index * Constants.tile_size + Constants.offset / 2
        top = top_index * Constants.tile_size + Constants.offset / 2
        return pygame.Rect(left, top, Constants.tile_size, Constants.tile_size)

    def create_side_border_ui(self):
        top_border = pygame.Rect(0, 0, Constants.screen_width, Constants.offset / 2)
        bottom_border = pygame.Rect(0, Constants.screen_height - (Constants.offset / 2),
                                    Constants.screen_width, Constants.offset / 2)
        left_border = pygame.Rect(0, 0, Constants.offset / 2, Constants.screen_height)
        right_border = pygame.Rect(Constants.screen_width - (Constants.offset / 2),
                                   0, Constants.offset / 2, Constants.screen_height)
        all_borders = [top_border, bottom_border, left_border, right_border]
        for i in all_borders:
            pygame.draw.rect(self.surface, Color.Snake.BLUE, i)
        pass

    def update_snake_ui(self):
        for i in range(len(self.data.tile)):
            row = self.data.tile[i]
            for j in range(len(row)):
                cell = row[j]
                cell_rect = self.get_cell_rect(j, i)
                pygame.draw.rect(self.surface, self.data.get_color_value(cell), cell_rect)
        pass

    def update_ui(self):
        self.create_side_border_ui()
        self.update_snake_ui()
        pass

    def update(self):
        self.update_ui()
        # self.surface = pygame.transform.flip(self.surface, 1, 0)
        # self.surface.blit(self.background, (0, 0))


