import pygame
import time
import random
from common.Utils import Utils
from Constants import Constants
from common.Constants import Constants as Cons


class Game:

    game_data = {
        "game_grid": []
    }
    tile_numbers = [0]
    tile_images = {}

    def __init__(self, surface):
        self.surface = surface
        # Preparing the list of tiles
        start = 2
        for i in range(11):
            self.tile_numbers.append(start)
            start = start * 2
        for i in self.tile_numbers:
            temp = Utils.load_image("2048", str(i)+".png").convert_alpha()
            self.tile_images[i] = pygame.transform.scale(temp, (Constants.tile_size, Constants.tile_size))
        self.init_data()
        return

    def get_random_cell(self):
        # 90% possibility of getting the number 2.
        # 10% possibility of getting the number 4.
        rand_num = random.random()
        if rand_num > 0.9:
            return 4
        return 2

    def get_empty_grids(self):
        empty_grids = []
        grid = self.game_data["game_grid"]
        for i in range(len(grid)):
            row = grid[i]
            for j in range(len(row)):
                cell = row[j]
                if cell == 0:
                    empty_grids.append((i, j))
        return empty_grids

    def get_random_position(self):
        empty_grids = self.get_empty_grids()
        return random.choice(empty_grids)

    def move_up(self):
        grid = self.game_data["game_grid"]
        tile_moved = False
        for i in range(len(grid)):
            for j in range(Constants.grid_height):
                cell = grid[j][i]
                if j != 0 and cell != 0:
                    last_position = j
                    last_value = cell
                    for k in range(j-1, -1, -1):
                        if grid[k][i] == 0:
                            tile_moved = True
                            self.update_tile((k, i), last_value)
                            self.update_tile((last_position, i), 0)
                            last_position = k
                        elif grid[k][i] == last_value and k != last_position:
                            tile_moved = True
                            last_value = last_value + last_value
                            self.update_tile((k, i), last_value)
                            self.update_tile((last_position, i), 0)
                            break
                        elif grid[k][i] != last_value:
                            break
        if tile_moved:
            self.spawn_cell()

    def move_down(self):
        grid = self.game_data["game_grid"]
        tile_moved = False
        for i in range(len(grid)):
            for j in range(Constants.grid_height-1, -1, -1):
                cell = grid[j][i]
                if j != 3 and cell != 0:
                    last_position = j
                    last_value = cell
                    for k in range(j, Constants.grid_height):
                        tile_moved = True
                        if grid[k][i] == 0:
                            self.update_tile((k, i), last_value)
                            self.update_tile((last_position, i), 0)
                            last_position = k
                        elif grid[k][i] == last_value and k != last_position:
                            tile_moved = True
                            last_value = last_value + last_value
                            self.update_tile((k, i), last_value)
                            self.update_tile((last_position, i), 0)
                            break
                        elif grid[k][i] != last_value:
                            break
        if tile_moved:
            self.spawn_cell()

    def move_left(self):
        grid = self.game_data["game_grid"]
        tile_moved = False
        for i in range(len(grid)):
            row = grid[i]
            for j in range(len(row)):
                cell = row[j]
                if j != 0 and cell != 0:
                    last_position = j
                    last_value = cell
                    # moving the cell in the left direction
                    for k in range(j, -1, -1):
                        # If the previous row is empty "Swap the value"
                        if row[k] == 0:
                            tile_moved = True
                            self.update_tile((i, k), last_value)
                            self.update_tile((i, last_position), 0)
                            last_position = k
                        # If the previous row has same valve "Add the value"
                        elif row[k] == last_value and k != last_position:
                            tile_moved = True
                            last_value = last_value+last_value
                            self.update_tile((i, k), last_value)
                            self.update_tile((i, last_position), 0)
                            break
                        elif row[k] != last_value:
                            break
        if tile_moved:
            self.spawn_cell()

    def move_right(self):
        grid = self.game_data["game_grid"]
        tile_moved = False
        for i in range(len(grid)):
            row = grid[i]
            for j in range(len(row)-1, -1, -1):
                cell = row[j]
                if j != 3 and cell != 0:
                    last_position = j
                    last_value = cell
                    # moving the cell in the right direction
                    for k in range(j, len(row), 1):
                        # If the previous row is empty "Swap the value"
                        if row[k] == 0:
                            tile_moved = True
                            self.update_tile((i, k), last_value)
                            self.update_tile((i, last_position), 0)
                            last_position = k
                        # If the previous row has same valve "Add the value"
                        elif row[k] == last_value and k != last_position:
                            tile_moved = True
                            last_value = last_value + last_value
                            self.update_tile((i, k), last_value)
                            self.update_tile((i, last_position), 0)
                            break
                        elif row[k] != last_value:
                            break
        if tile_moved:
            self.spawn_cell()

    def key_event(self, event):
        if event.scancode == Cons.key_code_up:
            self.move_up()
        if event.scancode == Cons.key_code_left:
            self.move_left()
        if event.scancode == Cons.key_code_right:
            self.move_right()
        if event.scancode == Cons.key_code_down:
            self.move_down()
        return

    def update_tile(self, position, value):
        self.game_data["game_grid"][position[0]][position[1]] = value
        return True

    def spawn_cell(self):
        random_tile = self.get_random_cell()
        random_position = self.get_random_position()
        self.update_tile(random_position, random_tile)

    def init_data(self):
        for i in range(Constants.grid_height):
            inner_list = []
            for j in range(Constants.grid_width):
                inner_list.append(0)
            self.game_data["game_grid"].append(inner_list)
        # Initializing two cell at the start of the game.
        self.spawn_cell()
        self.spawn_cell()

    def update_ui(self):
        for i in range(0, Constants.grid_height):
            for j in range(0, Constants.grid_width):
                cell_stat = self.game_data["game_grid"][i][j]
                self.surface.blit(self.tile_images[cell_stat], (j * Constants.tile_size, i * Constants.tile_size))

    def update(self):
        self.update_ui()
        # self.surface.blit(self.background, (0, 0))


# g = Game("", mock=1)
# g.init_data()
# print g.game_data["game_grid"][0]
