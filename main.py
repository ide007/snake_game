import random
import pygame as pg
import sys


BLOCK_SIZE = 25
BACKGROUND_COLOR = (0, 255, 205)
WHITE = (255, 255, 255)
BLUE = (204, 255, 255)
RED = (224, 0, 0)
HEADER_COLOR = (0, 205, 155)
SNAKE_COLOR = (0, 102, 0)
COLUMNS = 20
ROWS = 25
HEADER_MARGIN = 80
MARGIN = 1

size = [BLOCK_SIZE * (COLUMNS + 2) + MARGIN * (COLUMNS - 1),
        BLOCK_SIZE * (ROWS + 2) + HEADER_MARGIN + MARGIN * (ROWS - 1)]
print(size)

window = pg.display.set_mode(size)
pg.display.set_caption('Змейка')
timer = pg.time.Clock()


class SnakeBody:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self):
        return 0 <= self.x < ROWS and 0 <= self.y < COLUMNS

    def __eq__(self, other):
        return isinstance(other, SnakeBody) and self.x == other.x and self.y == other.y


def get_random_empty_block():
    x = random.randint(0, COLUMNS - 1)
    y = random.randint(0, ROWS - 1)
    empty_block = SnakeBody(x, y)
    while empty_block in snake_blocks:
        empty_block.x = random.randint(0, COLUMNS -1)
        empty_block.y = random.randint(0, ROWS - 1)
    return empty_block


def draw_block(color, row, column):
    pg.draw.rect(window, color,
                 [BLOCK_SIZE * (row + 1) + MARGIN * (row + 1),
                  HEADER_MARGIN + BLOCK_SIZE * (column + 1) + MARGIN * (
                          column + 1), BLOCK_SIZE, BLOCK_SIZE])


snake_blocks = [SnakeBody(1, 1), SnakeBody(1, 2), SnakeBody(1, 3)]
food = get_random_empty_block()
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


    pg.draw.rect(window, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])

    head = snake_blocks[-1]
    if not head.is_inside():
        print('CRASH')
        pg.quit()
        sys.exit()

    draw_block(RED, food.x, food.y)
    for block in snake_blocks:
        draw_block(SNAKE_COLOR, block.y, block.x)

    if food == head:
        snake_blocks.append(food)
        food = get_random_empty_block()

    new_head = SnakeBody(head.x + d_row, head.y + d_col)
    snake_blocks.append(new_head)
    snake_blocks.pop(0)

    pg.display.flip()
    timer.tick(2)
