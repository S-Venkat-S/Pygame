import pygame, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),".."))
from Player import Player
from Constants import Constants
pygame.init()
screen_width = Constants.screen_width  # type: int
screen_height = Constants.screen_height
FPS = Constants.FPS
main_screen = pygame.display.set_mode([screen_width,screen_height])

play_screen = pygame.Surface(main_screen.get_size())
player = Player(play_screen)
pygame.display.set_caption(Constants.game_name)
clock = pygame.time.Clock()
running = True
main_screen.fill((255,255,255))
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            player.key_event(event)
    player.draw()
    main_screen.blit(play_screen,(0,0))
    pygame.display.update();

pygame.quit()
