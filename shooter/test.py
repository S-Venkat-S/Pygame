import pygame
import sys
sys.path.insert(0, "F:\\Pygame")
from common.colors import Colors;
pygame.init()
screen_width = 360
screen_height = 480
FPS = 30
screen = pygame.display.set_mode([screen_width,screen_height])
pygame.display.set_caption("Yep!...")
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.circle(screen,Colors.common["GREEN"], event.pos, 10, 2)
        pygame.display.flip()

pygame.quit()
