import pygame as pg
from random import randrange


RES = 800
SIZE = 50
BACKGROUND_COLOR = (0, 255, 205)
WHITE = (255, 255, 255)
BLUE = (204, 255, 255)
RED = (224, 0, 0)
HEADER_COLOR = (0, 205, 155)
SNAKE_COLOR = (0, 102, 0)

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
food = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
dirs = {'W': True, 'S': True, 'A': True, 'D': True}
length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 5

pg.init()
screen = pg.display.set_mode([RES, RES])
clock = pg.time.Clock()

while True:
    screen.fill(BACKGROUND_COLOR)
    [(pg.draw.rect(screen, SNAKE_COLOR, (i, j, SIZE, SIZE))) for i, j in snake]
    pg.draw.rect(screen, RED, (*food, SIZE, SIZE))

    pg.display.flip()
    clock.tick(fps)

    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]

    if snake[-1] == food:
        food = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length += 1
        if length % 2 == 0:
            fps += 1

    if not 0 < x < RES - SIZE or not 0 < y < RES - SIZE or len(snake) != len(set(snake)):
        print('You lose')
        break

    for event in pg.event.get():
        if event.type == pg.QUIT:
            print('EXIT')
            exit(0)
    control = pg.key.get_pressed()
    if control[pg.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    if control[pg.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    if control[pg.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    if control[pg.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True}
