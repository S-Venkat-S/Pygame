import pygame, random
from common.Utils import Utils
from Constants import Constants
from common.Constants import Constants as C


class Game:

    tetri_i = [(0, 3), (0, 4), (0, 5), (0, 6)]  # (y, x) representation

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
        for i in range(len(self.game_data["current_tetri"])):
            cur_vec = self.game_data["current_tetri"][i]
            if (cur_vec[0] + 1) < self.grid_h:
                self.game_data["game_grid"][cur_vec[0]][cur_vec[1]] = 0
                cur_vec = (cur_vec[0] + 1, cur_vec[1])
                self.game_data["current_tetri"][i] = cur_vec
                self.game_data["game_grid"][cur_vec[0]][cur_vec[1]] = 1
            else:
                return
        pass

    def key_event(self, event):
        if event.scancode == C.key_code_up:
            pass
        if event.scancode == C.key_code_left:
            self.move_left()
        if event.scancode == C.key_code_right:
            self.move_right()
        if event.scancode == C.key_code_down:
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
        self.game_data["game_grid"][0][2] = 1
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
        self.update_ui_state()
        # self.surface.blit(self.background, (0, 0))


# g = Game("", mock=1)
# g.init_data()
# print g.game_data["game_grid"][0]
