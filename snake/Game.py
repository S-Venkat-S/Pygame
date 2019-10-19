import pygame
from Constants import Constants
from common.Constants import Constants as Cons
from common.colors import Colors as Color
from Snake import Snake


class Game:

    def __init__(self, surface):
        self.surface = surface
        self.snake = Snake(Constants.grid_width, Constants.grid_height, 0, self)
        self.state_update_timer = 0
        self.speed = 3 * 1000
        self.running = True
        self.data_instance = self.snake.data_instance


    # Gets the rect size to be filled according to the grid positions.
    # left = width, top = height
    def get_cell_rect(self, left_index, top_index):
        left = left_index * Constants.tile_size + Constants.offset / 2
        top = top_index * Constants.tile_size + Constants.offset / 2
        return pygame.Rect(left, top, Constants.tile_size, Constants.tile_size)

    def key_event(self, event):
        if event.scancode == Cons.key_code_up:
            self.snake.update_last_direction(Cons.up)
        if event.scancode == Cons.key_code_left:
            self.snake.update_last_direction(Cons.left)
        if event.scancode == Cons.key_code_right:
            self.snake.update_last_direction(Cons.right)
        if event.scancode == Cons.key_code_down:
            self.snake.update_last_direction(Cons.down)
        return

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
        for i in range(len(self.snake.tile)):
            row = self.snake.tile[i]
            for j in range(len(row)):
                cell = row[j]
                cell_rect = self.get_cell_rect(j, i)
                pygame.draw.rect(self.surface, self.snake.get_color_value(cell), cell_rect)
        self.update_score()

    def update_score(self):
        myfont = pygame.font.SysFont('tahoma', 14)
        textsurface = myfont.render(str(self.snake.score), False, (0, 0, 0))
        self.surface.blit(textsurface, (Constants.screen_width-40, 3))

    def update_ui(self):
        self.create_side_border_ui()
        self.update_snake_ui()
        if (self.state_update_timer + self.speed) < pygame.time.get_ticks():
            self.state_update_timer = pygame.time.get_ticks()
            self.snake.move()
            self.snake.update_grid()
        pass

    def update(self):
        self.update_ui()

    def snake_crashed(self):
        myfont = pygame.font.SysFont('tahoma', 30)
        self.running = False
        textsurface = myfont.render('Retry...', False, (0, 0, 0))
        pygame.draw.rect(self.surface, (255, 255, 255), (100, 100, 300, 300))
        self.surface.blit(textsurface, (100+20, 100+20))
        textsurface = myfont.render('(Y)es', False, (0, 0, 0))
        self.surface.blit(textsurface, (150+20, 225))
        textsurface = myfont.render('(N)o', False, (0, 0, 0))
        self.surface.blit(textsurface, (250+20, 225))

    def retry(self, event):
        if event.key == 121:
            self.snake = Snake(Constants.grid_width, Constants.grid_height, 0, self)
            self.running = True
        if event.key == 110:
            pygame.quit()
