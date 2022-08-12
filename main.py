import pygame
from copy import deepcopy
from random import choice, randrange

W, H = 10, 20
TITLE = 45
GAME_RES = W * TITLE, H * TITLE
RES = 750, 940
FPS = 60

pygame.init()
sc = pygame.display.set_mode(RES)
game_sc = pygame.Surface(GAME_RES)
clock = pygame.time.Clock()

grid = [pygame.Rect(x * TITLE, y * TITLE, TITLE, TITLE) for x in range(W) for y in range(H)]

figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
			   [(0, -1), (-1, -1), (-1, 0), (0, 0)],
			   [(-1, 0), (-1, 1), (0, 0), (0, -1)],
			   [(0, 0), (-1, 0), (0, 1), (-1, -1)],
			   [(0, 0), (0, -1), (0, 1), (-1, -1)],
			   [(0, 0), (0, -1), (0, 1), (-1, 0)]]

figures = [[pygame.Rect(x + W // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in figures_pos]
figure_rect = pygame.Rect(0, 0, TITLE - 2, TITLE - 2)
field = [[0 for i in range(W)] for j in range(H)]

anim_count, anim_speed, anim_limit = 0, 60, 2000

bg = pygame.image.load('img/matrix.jpg').convert()
game_bg = pygame.image.load('img/matrix.jpg').convert()


pygame.display.flip()
clock.tick(FPS)