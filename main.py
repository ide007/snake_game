import random

import pygame
import pygame as pg
import sys
import pygame_menu

pg.init()
bg_image = pg.image.load('logo.jpg')
BLOCK_SIZE = 25
BACKGROUND_COLOR = (0, 255, 205)
WHITE = (255, 255, 255)
BLUE = (204, 255, 255)
RED = (224, 0, 0)
HEADER_COLOR = (0, 205, 155)
SNAKE_COLOR = (0, 102, 0)
COLUMNS = 22
ROWS = 25
HEADER_MARGIN = 80
MARGIN = 1

size = [BLOCK_SIZE * (COLUMNS + 2) + MARGIN * (COLUMNS - 1),
        BLOCK_SIZE * (ROWS + 2) + HEADER_MARGIN + MARGIN * (ROWS - 1)]
print(size)

window = pg.display.set_mode(size)
pg.display.set_caption('Змейка')
timer = pg.time.Clock()
font_score = pg.font.SysFont('Arial', 26, bold=True)
font_end = pg.font.SysFont('Arial', 56, bold=True)


class SnakeBody:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self):
        return 0 <= self.x < ROWS and 0 <= self.y < COLUMNS

    def __eq__(self, other):
        return isinstance(other, SnakeBody) and \
               self.x == other.x and self.y == other.y


def draw_block(color, row, column):
    pg.draw.rect(window, color,
                 [BLOCK_SIZE * (row + 1) + MARGIN * (row + 1),
                  HEADER_MARGIN + BLOCK_SIZE * (column + 1) + MARGIN * (
                          column + 1), BLOCK_SIZE, BLOCK_SIZE])


def start_the_game():
    def get_random_empty_block():
        x = random.randint(0, COLUMNS - 1)
        y = random.randint(0, ROWS - 1)
        empty_block = SnakeBody(x, y)
        while empty_block in snake_blocks:
            empty_block.x = random.randint(0, COLUMNS - 1)
            empty_block.y = random.randint(0, ROWS - 1)
        return empty_block

    snake_blocks = [SnakeBody(COLUMNS // 2, ROWS // 2),
                    SnakeBody(COLUMNS // 2 - 1, ROWS // 2)]

    food = get_random_empty_block()
    d_row = buf_row = 0
    d_col = buf_col = 1
    score = 0
    speed = 1

    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                print('exit game')
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP and d_col != 0:
                    buf_row = -1
                    buf_col = 0
                elif event.key == pg.K_DOWN and d_col != 0:
                    buf_row = 1
                    buf_col = 0
                elif event.key == pg.K_LEFT and d_row != 0:
                    buf_row = 0
                    buf_col = -1
                elif event.key == pg.K_RIGHT and d_row != 0:
                    buf_row = 0
                    buf_col = 1

        window.fill(BACKGROUND_COLOR)
        pg.draw.rect(window, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])

        for row in range(ROWS):
            for column in range(COLUMNS):
                if (row + column) % 2 == 0:
                    color = WHITE
                else:
                    color = BLUE
                draw_block(color, column, row)

        head = snake_blocks[-1]
        if not head.is_inside():
            print('CRASH TO WALL')
            render_end = font_end.render(f'CRASH TO THE WALL!', True,
                                         pg.Color('orange'))
            window.blit(render_end, (BLOCK_SIZE * 3, size[1] // 3))
            break

        draw_block(RED, food.y, food.x)

        for block in snake_blocks:
            draw_block(SNAKE_COLOR, block.y, block.x)

        if food == head:
            snake_blocks.append(food)
            food = get_random_empty_block()
            score += 1
            speed = score // 5 + 1

        d_row = buf_row
        d_col = buf_col

        new_head = SnakeBody(head.x + d_row, head.y + d_col)

        if new_head in snake_blocks:
            print('CRASH TO YOURSELF')
            render_end = font_end.render(f'YOU CRASH TO YOURSELF!', True,
                                         pg.Color('orange'))
            window.blit(render_end, (size[0] // 10, size[1] // 3))
            break

        snake_blocks.append(new_head)
        snake_blocks.pop(0)
        render_score = font_score.render(f'SCORE: {score}', True,
                                         pg.Color('orange'))
        render_speed = font_score.render(f'SPEED: {speed}', True,
                                         pg.Color('orange'))
        window.blit(render_score, (BLOCK_SIZE, HEADER_MARGIN // 3))
        window.blit(render_speed,
                    (BLOCK_SIZE * COLUMNS // 2, HEADER_MARGIN // 3))

        pg.display.flip()
        timer.tick(3 + speed)


theme = pygame_menu.themes.THEME_DARK.copy()
theme.set_background_color_opacity(0.4)
menu = pygame_menu.Menu('', 300, 200,
                        theme=theme, position=(50, 65, True))

# menu.add.text_input('Имя игрока : ', default='Игрок 1')
menu.add.button('Старт', start_the_game)
menu.add.button('Выход', pygame_menu.events.EXIT)

while True:
    window.blit(bg_image, (0, 0))
    events = pygame.event.get()
    for event in events:
        if event.type == pg.QUIT:
            exit()

    if menu.is_enabled():
        menu.update(events)
        menu.draw(window)

    pg.display.update()
