import pygame as pg
from time import sleep


# class SnakeBody:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


BACKGROUND_COLOR = (50, 255, 205)
WHITE = (255, 255, 255)
BLUE = (204, 255, 255)
BLOCK_SIZE = 25
HEADER_COLOR = (0, 205, 155)
COLUMNS = 20
ROWS = 20
MARGIN = 2
HEADER_MARGIN = 80
size = [BLOCK_SIZE * (COLUMNS + 2) + MARGIN * (COLUMNS - 1),
        BLOCK_SIZE * (ROWS + 2) + HEADER_MARGIN + MARGIN * (ROWS - 1)]
window = pg.display.set_mode(size)
pg.display.set_caption('Змейка')


def draw_block(color, x, y):
    pg.draw.rect(window, color,
                 [BLOCK_SIZE * (x + 1) + MARGIN * (x + 1),
                  HEADER_MARGIN + BLOCK_SIZE * (y + 1) + MARGIN * (
                          y + 1), BLOCK_SIZE, BLOCK_SIZE])

while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            print('exit game')
            pg.quit()

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
    pg.display.flip()
