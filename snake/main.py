import pygame
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from Constants import Constants
from Game import Game

class main:

    def __init__(self):
        self.screen_width = Constants.screen_width
        self.screen_height = Constants.screen_height
        self.FPS = Constants.FPS
        self.main_screen = pygame.display.set_mode([self.screen_width, self.screen_height])

        pygame.font.init()
        self.play_screen = pygame.Surface(self.main_screen.get_size())
        pygame.display.set_caption(Constants.game_name)
        self.play_screen.fill((255, 255, 255))

    def game_loop(self):
        running = True
        game = Game(self.play_screen)
        while running:
            pygame.time.Clock().tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    game.key_event(event)
                if event.type == pygame.KEYDOWN and not game.running:
                    game.retry(event)
            if game.running:
                game.update()
            self.main_screen.blit(self.play_screen, (0, 0))
            pygame.display.update()

    def start(self):
        return self.game_loop()
