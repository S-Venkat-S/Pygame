import pygame
import time
from common.Utils import Utils
from Constants import Constants
from common.Constants import Constants as Cons


class Game:

    tetri_i = [(-1, 3), (-1, 4), (-1, 5), (-1, 6)]  # (y, x) representation
    speed = 0.10
    old_time = 0

    game_data = {
        "game_grid": [],
        "next_tetri": {},
        "current_tetri": list(tetri_i)
    }

    def check_cell(self, y, x):
        if self.game_data["game_grid"][y][x]:
            return True
        else:
            return False

    def move_left(self):
        for i in range(len(self.game_data["current_tetri"])):
            cur_vec = self.game_data["current_tetri"][i]
            if (cur_vec[1] - 1) > -1 and not self.check_cell(cur_vec[0], cur_vec[1] - 1):
                self.game_data["game_grid"][cur_vec[0]][cur_vec[1]] = 0
                cur_vec = (cur_vec[0], cur_vec[1] - 1)
                self.game_data["current_tetri"][i] = cur_vec
                self.game_data["game_grid"][cur_vec[0]][cur_vec[1]] = 1
            else:
                return
        return

    def move_right(self):
        for i in range(len(self.game_data["current_tetri"])-1, -1, -1):
            cur_vec = self.game_data["current_tetri"][i]
            if (cur_vec[1] + 1) < self.grid_w and not self.check_cell(cur_vec[0], cur_vec[1] + 1):
                self.game_data["game_grid"][cur_vec[0]][cur_vec[1]] = 0
                cur_vec = (cur_vec[0], cur_vec[1] + 1)
                self.game_data["current_tetri"][i] = cur_vec
                self.game_data["game_grid"][cur_vec[0]][cur_vec[1]] = 1
            else:
                return
        pass

    def move_down(self):
        no_fill = []
        fill = []
        for i in range(len(self.game_data["current_tetri"])):
            cur_vec = self.game_data["current_tetri"][i]
            if (cur_vec[0] + 1) < self.grid_h and not self.check_cell(cur_vec[0] + 1, cur_vec[1]):
                no_fill.append(cur_vec)
                cur_vec = (cur_vec[0] + 1, cur_vec[1])
                fill.append(cur_vec)
            else:
                return False
        for i in range(len(fill)):
            self.game_data["current_tetri"][i] = fill[i]
            self.game_data["game_grid"][fill[i][0]][fill[i][1]] = 1
            if no_fill[i][0] >= 0:
                self.game_data["game_grid"][no_fill[i][0]][no_fill[i][1]] = 0
        return True

    def key_event(self, event):
        if event.scancode == Cons.key_code_up:
            pass
        if event.scancode == Cons.key_code_left:
            self.move_left()
        if event.scancode == Cons.key_code_right:
            self.move_right()
        if event.scancode == Cons.key_code_down:
            self.move_down()
        pass
        return

    def init_data(self):
        for height in range(0, self.grid_h, 1):
            current_row = []
            for width in range(0, self.grid_w, 1):
                res = 0
                if (height, width) in self.game_data["current_tetri"]:
                    res = 1
                current_row.append(res)
            self.game_data["game_grid"].append(current_row)
        # self.game_data["game_grid"][3][5] = 1
        return True

    def __init__(self, surface, mock=False):
        self.grid_h = Constants.grid_height
        self.grid_w = Constants.grid_width
        self.init_data()
        if mock:
            return
        self.surface = surface
        self.no_fill = Utils.load_image("tetris", "bg_1.png").convert_alpha()
        self.no_fill = pygame.transform.scale(self.no_fill, (Constants.tile_size, Constants.tile_size))
        self.fill = Utils.load_image("tetris", "bg.png").convert_alpha()
        self.fill = pygame.transform.scale(self.fill, (Constants.tile_size, Constants.tile_size))
        return

    def update_state(self):
        for height in range(0, self.grid_h, 1):
            for width in range(0, self.grid_w, 1):
                if (height, width) in self.game_data["current_tetri"]:
                    self.game_data["game_grid"][height][width] = 1
        return True

    def update_ui_state(self):
        for i in range(0, self.grid_h):
            for j in range(0, self.grid_w):
                cell_stat = self.game_data["game_grid"][i][j]
                if cell_stat:
                    self.surface.blit(self.fill, (j * Constants.tile_size, i * Constants.tile_size))
                else:
                    self.surface.blit(self.no_fill, (j * Constants.tile_size, i * Constants.tile_size))

    def update(self):
        # self.update_state()
        c_time = time.time()
        if (c_time - self.old_time) > self.speed:
            self.old_time = c_time
            if not self.move_down():
                self.game_data["current_tetri"] = list(self.tetri_i)
        self.update_ui_state()
        # self.surface.blit(self.background, (0, 0))


# g = Game("", mock=1)
# g.init_data()
# print g.game_data["game_grid"][0]
