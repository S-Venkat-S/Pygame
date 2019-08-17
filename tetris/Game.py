import pygame
import time
import random
from common.Utils import Utils
from Constants import Constants
from common.Constants import Constants as Cons


class Game:

    #[(-1, 2), (0, 1), (1, 0), (2, -1)]
    tetri_i = {"init_pos": [(-1, 3), (-1, 4), (-1, 5), (-1, 6)],
               "no_of_transpose": 4,
               "trans_0_to_1": [(-1, 2), (0, 1), (1, 0), (2, -1)],
               "trans_1_to_2": [(2, -2), (1, -1), (0, 0), (-1, 1)],
               "trans_2_to_3": [(-2, 1), (-1, 0), (0, -1), (1, -2)],
               "trans_3_to_0": [(1, -1), (0, 0), (-1, 1), (-2, 2)],
               "name": "tetri_i"}
    tetri_o = {"init_pos": [(-1, 4), (-1, 5), (-2, 4), (-2, 5)],
               "no_of_transpose": 4,
               "trans_0_to_1": [(0, 0), (0, 0), (0, 0), (0, 0)],
               "trans_1_to_2": [(0, 0), (0, 0), (0, 0), (0, 0)],
               "trans_2_to_3": [(0, 0), (0, 0), (0, 0), (0, 0)],
               "trans_3_to_0": [(0, 0), (0, 0), (0, 0), (0, 0)],
               "name": "tetri_o"}
    tetri_t = {"init_pos": [(-1, 3), (-1, 4), (-1, 5), (-2, 4)],
               "no_of_transpose": 4,
               "trans_0_to_1": [(-1, 1), (0, 0), (1, -1), (1, 1)],
               "trans_1_to_2": [(1, -1), (0, 0), (-1, 1), (1, -1)],
               "trans_2_to_3": [(-1, 1), (0, 0), (1, -1), (-1, -1)],
               "trans_3_to_0": [(1, -1), (0, 0), (-1, 1), (-1, 1)],
               "name": "tetri_t"}
    tetri_j = {"init_pos": [(-2, 5), (-1, 3), (-1, 4), (-1, 5)],
               "no_of_transpose": 4,
               "trans_0_to_1": [(0, -1), (0, 1), (1, 0), (1, 0)],
               "trans_1_to_2": [(1, 1), (0, 0), (-1, -1), (0, -2)],
               "trans_2_to_3": [(1, -1), (0, 0), (-1, 1), (-2, 0)],
               "trans_3_to_0": [(-2, 1), (0, -1), (1, 0), (1, 2)],
               "name": "tetri_j"}
    tetri_l = {"init_pos": [(-2, 3), (-1, 3), (-1, 4), (-1, 5)],
               "no_of_transpose": 4,
               "trans_0_to_1": [(0, 2), (-1, 1), (0, 0), (1, -1)],
               "trans_1_to_2": [(2, 0), (1, 1), (0, 0), (-1, -1)],
               "trans_2_to_3": [(0, -2), (1, -1), (0, 0), (-1, 1)],
               "trans_3_to_0": [(-2, 0), (-1, -1), (0, 0), (1, 1)],
               "name": "tetri_l"}
    tetri_s = {"init_pos": [(-1, 3), (-1, 4), (-2, 4), (-2, 5)],
               "no_of_transpose": 4,
               "trans_0_to_1": [(-1, 1), (0, 0), (1, 1), (2, 0)],
               "trans_1_to_2": [(1, 1), (0, 0), (1, -1), (0, -2)],
               "trans_2_to_3": [(-1, -2), (0, -1), (-1, 0), (0, 1)],
               "trans_3_to_0": [(1, 0), (0, 1), (-1, 0), (-2, 1)],
               "name": "tetri_s"}
    tetri_z = {"init_pos": [(-2, 3), (-2, 4), (-1, 4), (-1, 5)],
               "no_of_transpose": 4,
               "trans_0_to_1": [(0, 2), (1, 1), (0, 0), (1, -1)],
               "trans_1_to_2": [(1, -2), (0, -1), (1, 0), (0, 1)],
               "trans_2_to_3": [(-1, 1), (0, 0), (-1, -1), (0, -2)],
               "trans_3_to_0": [(0, -1), (-1, 0), (0, 1), (-1, 2)],
               "name": "tetri_z"}

    tetris_list = [tetri_i, tetri_o, tetri_t, tetri_j,
                   tetri_l, tetri_s, tetri_z]
    speed = 0.50
    old_time = 0

    game_data = {
        "game_grid": [],
        "next_tetri": None,
        "current_tetri": None,
        "cur_transpose_pos": 0,
        "current_tetri_instance": None,
        "next_tetri_instance":None
    }

    def current_tetri_instance(self):
        return self.game_data["current_tetri_instance"]

    def get_cur_transpose_pos(self):
        return self.game_data["cur_transpose_pos"]

    def set_cur_transpose_pos(self, val):
        self.game_data["cur_transpose_pos"] = val
        return True

    def reset_cur_transpose_pos(self):
        self.game_data["cur_transpose_pos"] = 0
        return True

    def get_next_transpose_data(self):
        tetri = self.current_tetri_instance()
        cur_pos = self.get_cur_transpose_pos()
        total_pos = tetri["no_of_transpose"] - 1
        next_pos = cur_pos + 1
        if next_pos > total_pos:
            next_pos = 0
        trans_text = "trans_"+str(cur_pos)+"_to_"+str(next_pos)
        data = tetri[trans_text]
        return {"data": data, "next_pos": next_pos}



    def check_cell(self, y, x):
        if y < 0:
            return False
        if x < 0:
            return True
        if self.game_data["game_grid"][y][x]:
            return True
        else:
            return False

    def get_next_tetri(self):
        tetri = random.choice(self.tetris_list)
        self.reset_cur_transpose_pos()
        return list(tetri["init_pos"]), tetri

    def fill_cells(self, y, x):
        if y < 0:
            return True
        if self.game_data["game_grid"][y][x] == 0:
            self.game_data["game_grid"][y][x] = 1
            return True
        else:
            return False

    def erase_cells(self, y, x):
        if y < 0:
            return True
        if self.game_data["game_grid"][y][x] == 1:
            self.game_data["game_grid"][y][x] = 0
            return True
        else:
            return False

    def update_current_tetri(self, cells):
        self.game_data["current_tetri"] = cells
        return True

    def clear_and_fill(self, no_fill, fill):
        for j in no_fill:
            self.erase_cells(j[0], j[1])
        for i in fill:
            self.fill_cells(i[0], i[1])
        return True

    def validate_moves(self, no_fill, fill):
        for i in fill:
            if i in no_fill or not self.check_cell(i[0], i[1]):
                pass
            else:
                return False
        return True

    def move(self, no_fill, fill):
        # Validate moves
        if not self.validate_moves(no_fill, fill):
            return False
        # Filling and non-filling cells
        if not self.clear_and_fill(no_fill, fill):
            return False
        # Updating the current tetri with the cells to be filled
        return self.update_current_tetri(fill)

    def move_left(self):
        no_fill = list(self.game_data["current_tetri"])
        fill = []

        # Generating list of possible moves
        for i in no_fill:
            y = i[0]
            x = i[1]
            if x - 1 >= 0:
                x = x - 1
                fill.append((y, x))
            else:
                return False
        return self.move(no_fill, fill)

    def move_right(self):
        no_fill = list(self.game_data["current_tetri"])
        fill = []

        # Generating list of possible moves
        for i in no_fill:
            y = i[0]
            x = i[1]
            if x + 1 < Constants.grid_width:
                x = x + 1
                fill.append((y, x))
            else:
                return False
        return self.move(no_fill, fill)

    def move_down(self):
        no_fill = list(self.game_data["current_tetri"])
        fill = []

        # Generating list of possible moves
        for i in no_fill:
            y = i[0]
            x = i[1]
            if y + 1 < Constants.grid_height:
                y = y + 1
                fill.append((y, x))
            else:
                return False
        return self.move(no_fill, fill)

    def transpose(self):
        # TODO
        no_fill = list(self.game_data["current_tetri"])
        fill = []
        transpose_data = self.get_next_transpose_data()
        next_pos = transpose_data["next_pos"]
        data = transpose_data["data"]

        # Generating list of possible moves
        for i in range(len(no_fill)):
            no_fill_data = no_fill[i]
            trans_data = data[i]
            y = no_fill_data[0] + trans_data[0]
            x = no_fill_data[1] + trans_data[1]
            if y < Constants.grid_height and x < Constants.grid_width:
                fill.append((y, x))
            else:
                return False
        print no_fill, "NF"
        print data, "Tr"
        print fill, "FL"
        if self.move(no_fill, fill):
            self.set_cur_transpose_pos(next_pos)

    def key_event(self, event):
        if event.scancode == Cons.key_code_up:
            self.transpose()
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
                # if (height, width) in self.game_data["current_tetri"]:
                #     res = 1
                current_row.append(res)
            self.game_data["game_grid"].append(current_row)
        # self.game_data["game_grid"][3][5] = 1
        cur_tetri_data = self.get_next_tetri()
        next_tetri_data = self.get_next_tetri()
        self.game_data["current_tetri"] = cur_tetri_data[0]
        self.game_data["current_tetri_instance"] = cur_tetri_data[1]
        self.game_data["next_tetri"] = next_tetri_data[0]
        self.game_data["next_tetri_instance"] = next_tetri_data[1]
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
        c_time = time.time()
        if (c_time - self.old_time) > self.speed:
            self.old_time = c_time
            if not self.move_down():
                self.game_data["current_tetri"] = self.game_data["next_tetri"]
                self.game_data["current_tetri_instance"] = self.game_data["next_tetri_instance"]
                next_tetri_data = self.get_next_tetri()
                self.game_data["next_tetri"] = next_tetri_data[0]
                self.game_data["next_tetri_instance"] = next_tetri_data[1]

    def update_ui_state(self):
        for i in range(0, self.grid_h):
            for j in range(0, self.grid_w):
                cell_stat = self.game_data["game_grid"][i][j]
                if cell_stat:
                    self.surface.blit(self.fill, (j * Constants.tile_size, i * Constants.tile_size))
                else:
                    self.surface.blit(self.no_fill, (j * Constants.tile_size, i * Constants.tile_size))

    def update(self):
        self.update_state()
        self.update_ui_state()
        # self.surface.blit(self.background, (0, 0))


# g = Game("", mock=1)
# g.init_data()
# print g.game_data["game_grid"][0]
