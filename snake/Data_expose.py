# Exposing data through side class.
class Data_expose:

    snake = None

    def __init__(self, snake):
        self.snake = snake

    def get_score(self):
        return self.snake.score

    def get_snake_position(self):
        return self.snake.snake_grid

    def get_food_position(self):
        return self.snake.food_pos

    def set_direction(self, direction):
        if direction in self.snake.opposite_directions.viewkeys():
            return self.snake.update_last_direction(direction)

