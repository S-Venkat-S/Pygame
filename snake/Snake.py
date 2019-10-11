from common.colors import Colors
from common.Constants import Constants as Cons
import random


class Snake:
    tile = []
    grid_height = 0
    grid_width = 0
    last_direction = Cons.right
    food_pos = None
    # Snake positions in (x, y)
    snake_grid = []
    game_instance = None

    opposite_directions = {
        Cons.up: Cons.down,
        Cons.down: Cons.up,
        Cons.left: Cons.right,
        Cons.right: Cons.left
    }

    def __init__(self, g_width, g_height, init_value, game_instance):
        # 0 -> Non filled cell.
        # 1 -> Cell occupied by snake.
        # 8 -> Cell currently have food.
        # At later game the higher value means higher food.
        self.grid_height = g_height
        self.grid_width = g_width
        self.game_instance = game_instance
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
            self.snake_grid.append((middle_w + i, middle_h))
        self.update_snake_in_grid()
        self.get_random_food()

    def update_grid(self):
        self.update_snake_in_grid()
        self.update_food_in_grid()

    def update_food_in_grid(self):
        self.place_value(self.food_pos[0], self.food_pos[1], 8)

    def empty_grid_pos(self, pos_vector):
        self.place_value(pos_vector[0], pos_vector[1], 0)

    def update_snake_in_grid(self):
        if self.is_collided(self.snake_grid[-1]):
            print "Drive carefully!!!"
            self.game_instance.snake_crashed()
            return
        for i in self.snake_grid:
            self.place_value(i[0], i[1], 1)

    def is_food_eaten(self, pos_vector):
        if pos_vector == self.food_pos:
            self.get_random_food()
            return True

    def get_color_value(self, value):
        # TODO: No need for handling the value "0"
        if value == 0:
            return Colors.Snake.BLACK
        elif value == 1:
            return Colors.Snake.GREEN
        elif value == 8:
            return Colors.Snake.PINK

    def update_last_direction(self, direction):
        if self.last_direction is self.opposite_directions[direction]:
            return
        self.last_direction = direction

    def place_value(self, x, y, value):
        self.tile[y][x] = value

    def move(self):
        direction = self.last_direction
        if direction == Cons.left:
            self.move_left()
        if direction == Cons.right:
            self.move_right()
        if direction == Cons.up:
            self.move_up()
        if direction == Cons.down:
            self.move_down()
        pass

    def update_snake_head(self, head_vector):
        self.snake_grid.append(head_vector)
        if not self.is_food_eaten(head_vector):
            self.empty_grid_pos(self.snake_grid[0])
            del self.snake_grid[0]

    def is_collided(self, pos_vector):
        if pos_vector[0] == self.grid_width:
            return True
        if pos_vector[0] == -1:
            return True
        if pos_vector[1] == -1:
            return True
        if pos_vector[1] == self.grid_height:
            return True

    def move_up(self):
        snake_head = self.snake_grid[-1]
        new_head = (snake_head[0], snake_head[1] - 1)
        self.update_snake_head(new_head)

    def move_right(self):
        snake_head = self.snake_grid[-1]
        new_head = (snake_head[0] + 1, snake_head[1])
        self.update_snake_head(new_head)

    def move_down(self):
        snake_head = self.snake_grid[-1]
        new_head = (snake_head[0], snake_head[1] + 1)
        self.update_snake_head(new_head)

    def move_left(self):
        snake_head = self.snake_grid[-1]
        new_head = (snake_head[0] - 1, snake_head[1])
        self.update_snake_head(new_head)

    def get_random_food(self):
        attempt = 0
        while attempt <= self.grid_height*self.grid_width:
            attempt = attempt+1
            x = random.randrange(0, self.grid_width)
            y = random.randrange(0, self.grid_height)
            if self.tile[y][x] == 0:
                self.food_pos = (x, y)
                return
        # Can't find the place for food.
        # Bigger snake!!!
        return
