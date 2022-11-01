import pygame as pg
from time import sleep
import sys

class SnakeBody:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self):
        return 0 <= self.x < COLUMNS and 0 <= self.y < ROWS


BACKGROUND_COLOR = (50, 255, 205)
WHITE = (255, 255, 255)
BLUE = (204, 255, 255)
BLOCK_SIZE = 25
HEADER_COLOR = (0, 205, 155)
SNAKE_COLOR = (0, 102, 0)
COLUMNS = 20
ROWS = 25
MARGIN = 1
HEADER_MARGIN = 80
size = [BLOCK_SIZE * (COLUMNS + 2) + MARGIN * (COLUMNS - 1),
        BLOCK_SIZE * (ROWS + 2) + HEADER_MARGIN + MARGIN * (ROWS - 1)]
print(size)
window = pg.display.set_mode(size)
pg.display.set_caption('Змейка')
snake_blocks = [SnakeBody(10, 8), SnakeBody(10, 9), SnakeBody(10, 10)]
timer = pg.time.Clock()


def draw_block(color, x, y):
    pg.draw.rect(window, color,
                 [BLOCK_SIZE * (x + 1) + MARGIN * (x + 1),
                  HEADER_MARGIN + BLOCK_SIZE * (y + 1) + MARGIN * (
                          y + 1), BLOCK_SIZE, BLOCK_SIZE])


d_row = 0
d_col = 1

while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            print('exit game')
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and d_col != 0:
                d_row = -1
                d_col = 0
            elif event.key == pg.K_DOWN and d_col != 0:
                d_row = 1
                d_col = 0
            elif event.key == pg.K_LEFT and d_row != 0:
                d_row = 0
                d_col = -1
            elif event.key == pg.K_RIGHT and d_row != 0:
                d_row = 0
                d_col = 1

    window.fill(BACKGROUND_COLOR)
    for row in range(ROWS):
        for column in range(COLUMNS):
            if (row + column) % 2 == 0:
                color = WHITE
            else:
                color = BLUE
            draw_block(color, column, row)
            # pg.draw.rect(window, color,
            #              [BLOCK_SIZE * (column + 1) + MARGIN * (column + 1),
            #               HEADER_MARGIN + BLOCK_SIZE * (row + 1) + MARGIN * (
            #                           row + 1), BLOCK_SIZE, BLOCK_SIZE])

    pg.draw.rect(window, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])

    head = snake_blocks[-1]
    if not head.is_inside():
        print('CRASH')
        pg.quit()
        sys.exit()

    for block in snake_blocks:
        draw_block(SNAKE_COLOR, block.y, block.x)

    new_head = SnakeBody(head.x + d_row, head.y + d_col)
    snake_blocks.append(new_head)
    snake_blocks.pop(0)

    pg.display.flip()
    timer.tick(2)
