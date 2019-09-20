from common.colors import Colors
import random

class DataStructure:

    tile = []
    grid_height = 0
    grid_width = 0

    def __init__(self, g_width, g_height, init_value):
        # 0 -> Non filled cell.
        # 1 -> Cell occupied by snake.
        # 8 -> Cell currently have food.
        self.grid_height = g_height
        self.grid_width = g_width
        for i in range(g_height):
            row = []
            for j in range(g_width):
                row.append(init_value)
            self.tile.append(row)
        # Snake starts with a length of 3 tile size.
        # Placing the snake middle (nearly) of the grid
        middle_w = g_width / 2
        middle_h = g_height / 2
        snake_init = [-1, 0, 1]
        for i in snake_init:
            self.tile[middle_h][middle_w + i] = 1
        self.place_random_food()

    def get_color_value(self, value):
        # TODO: No need for handling the value "0"
        if value == 0:
            return Colors.Snake.BLACK
        elif value == 1:
            return Colors.Snake.GREEN
        elif value == 8:
            return Colors.Snake.PINK

    def place_value(self, x, y, value):
        self.tile[y][x] = value

    def place_random_food(self):
        is_found = False
        while not is_found:
            x = random.randrange(0, self.grid_width)
            y = random.randrange(0, self.grid_height)
            if self.tile[y][x] == 0:
                is_found = True
                self.place_value(x, y, 8)
