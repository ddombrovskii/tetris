import random
import sys
import time
import sqlite3

import pygame as pg
from pygame.locals import *

COLORS = ((0, 0, 225), (0, 225, 0), (225, 0, 0), (225, 225, 0))  # blue, green, red, yellow
LIGHTCOLORS = ((30, 30, 255), (50, 255, 50),
               (255, 30, 30), (255, 255, 30))  # light-blue, light-green, light-red, light-yellow

WHITE, GRAY, BLACK = (255, 255, 255), (185, 185, 185), (0, 0, 0)
BRD_COLOR, BG_COLOR, TXT_COLOR, TITLE_COLOR, INFO_COLOR = WHITE, GRAY, WHITE, COLORS[3], COLORS[0]
GRD_COLOR = (160, 160, 160)

FIG_W, FIG_H = 5, 5
EMPTY = 'o'

FIGURES = {'S': [['ooooo',
                  'ooooo',
                  'ooxxo',
                  'oxxoo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'ooxxo',
                  'oooxo',
                  'ooooo']],
           'Z': [['ooooo',
                  'ooooo',
                  'oxxoo',
                  'ooxxo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'oxxoo',
                  'oxooo',
                  'ooooo']],
           'J': [['ooooo',
                  'oxooo',
                  'oxxxo',
                  'ooooo',
                  'ooooo'],
                 ['ooooo',
                  'ooxxo',
                  'ooxoo',
                  'ooxoo',
                  'ooooo'],
                 ['ooooo',
                  'ooooo',
                  'oxxxo',
                  'oooxo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'ooxoo',
                  'oxxoo',
                  'ooooo']],
           'L': [['ooooo',
                  'oooxo',
                  'oxxxo',
                  'ooooo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'ooxoo',
                  'ooxxo',
                  'ooooo'],
                 ['ooooo',
                  'ooooo',
                  'oxxxo',
                  'oxooo',
                  'ooooo'],
                 ['ooooo',
                  'oxxoo',
                  'ooxoo',
                  'ooxoo',
                  'ooooo']],
           'I': [['ooxoo',
                  'ooxoo',
                  'ooxoo',
                  'ooxoo',
                  'ooooo'],
                 ['ooooo',
                  'ooooo',
                  'xxxxo',
                  'ooooo',
                  'ooooo']],
           'O': [['ooooo',
                  'ooooo',
                  'oxxoo',
                  'oxxoo',
                  'ooooo']],
           'T': [['ooooo',
                  'ooxoo',
                  'oxxxo',
                  'ooooo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'ooxxo',
                  'ooxoo',
                  'ooooo'],
                 ['ooooo',
                  'ooooo',
                  'oxxxo',
                  'ooxoo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'oxxoo',
                  'ooxoo',
                  'ooooo']]}


def pause_screen():
    pause = pg.Surface((600, 500), pg.SRCALPHA)
    pause.fill((0, 0, 255, 127))
    display_surf.blit(pause, (0, 0))


def main(login, width, height, speed):
    global display_surf, fps_clock, basic_font, big_font
    global FPS, WINDOW_W, WINDOW_H, BLOCK, CUP_H, CUP_W, SIDE_FREQ, DOWN_FREQ, SIDE_MARGIN, TOP_MARGIN

    FPS = 25
    WINDOW_W, WINDOW_H = 600, 500
    BLOCK = 20
    CUP_H, CUP_W = height, width

    SIDE_FREQ, DOWN_FREQ = 0.15, 0.1

    SIDE_MARGIN = int((WINDOW_H - CUP_W * BLOCK) / 2)
    TOP_MARGIN = WINDOW_H - (CUP_H * BLOCK) - 5

    pg.init()
    fps_clock = pg.time.Clock()
    display_surf = pg.display.set_mode((WINDOW_W, WINDOW_H))
    basic_font = pg.font.SysFont('arial', 20)
    big_font = pg.font.SysFont('verdana', 45)
    pg.display.set_caption('Tetris')

    points = run_tetris(login, speed)
    stop_game()
    # print(points)
    # pause_screen()
    # show_text('Игра закончена')

    return points


def run_tetris(login, speed):
    cup = empty_cup()
    last_move_down = time.time()
    last_side_move = time.time()
    last_fall = time.time()
    going_down = False
    going_left = False
    going_right = False
    points = 0
    fall_speed = 0.27 - (speed * 0.02)
    falling_fig = get_new_fig()
    next_fig = get_new_fig()

    while True:
        if falling_fig is None:
            # если нет падающих фигур, генерируем новую
            falling_fig = next_fig
            next_fig = get_new_fig()
            last_fall = time.time()

            if not check_pos(cup, falling_fig):
                return points
        quit_game()

        for event in pg.event.get():
            if event.type == KEYUP:
                if event.key == K_SPACE:
                    pause_screen()
                    show_text('Pause')
                    last_fall = time.time()
                    last_move_down = time.time()
                    last_side_move = time.time()
                elif event.key == K_LEFT:
                    going_left = False
                elif event.key == K_RIGHT:
                    going_right = False
                elif event.key == K_DOWN:
                    going_down = False

            elif event.type == KEYDOWN:
                if event.key == K_LEFT and check_pos(cup, falling_fig, adjX=-1):
                    falling_fig['x'] -= 1
                    going_left = True
                    going_right = False
                    last_side_move = time.time()

                elif event.key == K_RIGHT and check_pos(cup, falling_fig, adjX=1):
                    falling_fig['x'] += 1
                    going_right = True
                    going_left = False
                    last_side_move = time.time()

                elif event.key == K_UP:
                    falling_fig['rotation'] = (falling_fig['rotation'] + 1) % len(FIGURES[falling_fig['shape']])
                    if not check_pos(cup, falling_fig):
                        falling_fig['rotation'] = (falling_fig['rotation'] - 1) % len(FIGURES[falling_fig['shape']])

                elif event.key == K_DOWN:
                    going_down = True
                    if check_pos(cup, falling_fig, adjY=1):
                        falling_fig['y'] += 1
                    last_move_down = time.time()

                elif event.key == K_RETURN:
                    going_down = False
                    going_left = False
                    going_right = False
                    for i in range(1, CUP_H):
                        if not check_pos(cup, falling_fig, adjY=i):
                            break
                    falling_fig['y'] += i - 1

        if (going_right or going_left) and time.time() - last_side_move > SIDE_FREQ:
            if going_left and check_pos(cup, falling_fig, adjX=-1):
                falling_fig['x'] -= 1
            elif going_right and check_pos(cup, falling_fig, adjX=1):
                falling_fig['x'] += 1
            last_side_move = time.time()

        if going_down and time.time() - last_move_down > DOWN_FREQ and check_pos(cup, falling_fig, adjY=1):
            falling_fig['y'] += 1
            last_move_down = time.time()

        if time.time() - last_fall > fall_speed:
            if not check_pos(cup, falling_fig, adjY=1):
                add_to_cup(cup, falling_fig)
                points += clear_completed(cup)
                # level, fall_speed = calc_speed(points)
                falling_fig = None
            else:
                falling_fig['y'] += 1
                last_fall = time.time()

        display_surf.fill(BG_COLOR)
        draw_title()
        game_cup(cup, login)
        draw_info(points)
        if get_next_fig_state(login):
            draw_next_fig(next_fig)

        if falling_fig is not None:
            draw_fig(falling_fig)
        pg.display.update()
        fps_clock.tick(FPS)


def txt_objects(text, font, color):
    surf = font.render(text, True, color)
    return surf, surf.get_rect()


def stop_game():
    # pg.display.quit()
    pg.quit()
    # sys.exit()


def check_keys():
    quit_game()

    for event in pg.event.get([KEYDOWN, KEYUP]):
        if event.type == KEYDOWN:
            continue
        return event.key

    return None


def show_text(text):
    title_surf, title_rect = txt_objects(text, big_font, TITLE_COLOR)
    title_rect.center = (int(WINDOW_W / 2) - 3, int(WINDOW_H / 2) - 3)
    display_surf.blit(title_surf, title_rect)

    press_key_surf, press_key_rect = txt_objects("Нажмите любую клавишу для продолжения", basic_font, TITLE_COLOR)
    press_key_rect.center = (int(WINDOW_W / 2), int(WINDOW_H / 2) + 100)
    display_surf.blit(press_key_surf, press_key_rect)

    while check_keys() is None:
        pg.display.update()
        fps_clock.tick()


def quit_game():
    for event in pg.event.get(QUIT):
        stop_game()
    for event in pg.event.get(KEYUP):
        if event.key == K_ESCAPE:
            stop_game()
        pg.event.post(event)


'''
def calc_speed(points):
    level = int(points / 10) + 1
    fall_speed = 0.27 - (level * 0.02)
    return level, fall_speed
'''


def get_new_fig():
    shape = random.choice(list(FIGURES.keys()))
    new_figure = {'shape': shape,
                  'rotation': random.randint(0, len(FIGURES[shape]) - 1),
                  'x': int(CUP_W / 2) - int(FIG_W / 2),
                  'y': -2,
                  'color': random.randint(0, len(COLORS) - 1)}

    return new_figure


def add_to_cup(cup, fig):
    for x in range(FIG_W):
        for y in range(FIG_H):
            if FIGURES[fig['shape']][fig['rotation']][y][x] != EMPTY:
                cup[x + fig['x']][y + fig['y']] = fig['color']


def empty_cup():
    cup = []

    for i in range(CUP_W):
        cup.append([EMPTY] * CUP_H)

    return cup


def in_cup(x, y):
    return 0 <= x < CUP_W and y < CUP_H


def check_pos(cup, fig, adjX=0, adjY=0):
    for x in range(FIG_W):
        for y in range(FIG_H):
            above_cup = y + fig['y'] + adjY < 0
            if above_cup or FIGURES[fig['shape']][fig['rotation']][y][x] == EMPTY:
                continue
            if not in_cup(x + fig['x'] + adjX, y + fig['y'] + adjY):
                return False
            if cup[x + fig['x'] + adjX][y + fig['y'] + adjY] != EMPTY:
                return False

    return True


def is_completed(cup, y):
    for x in range(CUP_W):
        if cup[x][y] == EMPTY:
            return False

    return True


def clear_completed(cup):
    removed_lines = 0
    y = CUP_H - 1

    while y >= 0:
        if is_completed(cup, y):
            for push_down_y in range(y, 0, -1):
                for x in range(CUP_W):
                    cup[x][push_down_y] = cup[x][push_down_y - 1]

            for x in range(CUP_W):
                cup[x][0] = EMPTY
            removed_lines += 1
        else:
            y -= 1

    return removed_lines


def convert_coords(block_x, block_y):
    return (SIDE_MARGIN + (block_x * BLOCK)), (TOP_MARGIN + (block_y * BLOCK))


def draw_block(block_x, block_y, color, pixelx=None, pixely=None):
    if color == EMPTY:
        return

    if pixelx is None and pixely is None:
        pixelx, pixely = convert_coords(block_x, block_y)

    pg.draw.rect(display_surf, COLORS[color], (pixelx + 1, pixely + 1, BLOCK - 1, BLOCK - 1), 0, 1)
    pg.draw.rect(display_surf, LIGHTCOLORS[color], (pixelx + 1, pixely + 1, BLOCK - 4, BLOCK - 4), 0, 1)
    # pg.draw.circle(display_surf, COLORS[color], (pixelx + BLOCK / 2, pixely + BLOCK / 2), 5)


def game_cup(cup, login):
    pg.draw.rect(display_surf, BRD_COLOR, (SIDE_MARGIN - 4, TOP_MARGIN - 4, (CUP_W * BLOCK) + 8, (CUP_H * BLOCK) + 8),
                 5)

    # фон игрового поля
    pg.draw.rect(display_surf, BG_COLOR, (SIDE_MARGIN, TOP_MARGIN, BLOCK * CUP_W, BLOCK * CUP_H))

    if get_grid_state(login):
        for i in range(CUP_H):
            pg.draw.line(display_surf, GRD_COLOR, (SIDE_MARGIN, TOP_MARGIN + i * BLOCK),
                         (SIDE_MARGIN + (CUP_W * BLOCK), TOP_MARGIN + i * BLOCK), 1)
            for j in range(CUP_W):
                pg.draw.line(display_surf, GRD_COLOR, (SIDE_MARGIN + j * BLOCK, TOP_MARGIN),
                             (SIDE_MARGIN + j * BLOCK, TOP_MARGIN + (CUP_H * BLOCK)))

    for x in range(CUP_W):
        for y in range(CUP_H):
            draw_block(x, y, cup[x][y])


def draw_title():
    title_surf = big_font.render('Tetris', True, TITLE_COLOR)
    title_rect = title_surf.get_rect()
    title_rect.topleft = (WINDOW_W - 425, 30)
    display_surf.blit(title_surf, title_rect)


def draw_info(points):
    points_surf = basic_font.render(f'Баллы: {points}', True, TXT_COLOR)
    points_rect = points_surf.get_rect()
    points_rect.topleft = (WINDOW_W - 550, 180)
    display_surf.blit(points_surf, points_rect)

    '''    level_surf = basic_font.render(f'Уровень: {level}', True, TXT_COLOR)
    level_rect = level_surf.get_rect()
    level_rect.topleft = (WINDOW_W - 550, 250)
    display_surf.blit(level_surf, level_rect)'''

    pause_surf = basic_font.render("Пауза: пробел", True, INFO_COLOR)
    pause_rect = pause_surf.get_rect()
    pause_rect.topleft = (WINDOW_W - 140, 420)
    display_surf.blit(pause_surf, pause_rect)

    escb_surf = basic_font.render("Выход: Esc", True, INFO_COLOR)
    escb_rect = escb_surf.get_rect()
    escb_rect.topleft = (WINDOW_W - 140, 450)
    display_surf.blit(escb_surf, escb_rect)


def draw_fig(fig, pixelx=None, pixely=None):
    fig_to_draw = FIGURES[fig['shape']][fig['rotation']]
    if pixelx is None and pixely is None:
        pixelx, pixely = convert_coords(fig['x'], fig['y'])

    for x in range(FIG_W):
        for y in range(FIG_H):
            if fig_to_draw[y][x] != EMPTY:
                draw_block(None, None, fig['color'], pixelx + (x * BLOCK), pixely + (y * BLOCK))


def draw_next_fig(fig):
    next_surf = basic_font.render("Следующая:", True, TXT_COLOR)
    next_rect = next_surf.get_rect()
    next_rect.topleft = (WINDOW_W - 150, 180)
    display_surf.blit(next_surf, next_rect)

    draw_fig(fig, pixelx=WINDOW_W - 150, pixely=230)


def get_grid_state(login):
    if login == 'guest':
        return True

    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql_update_query = """SELECT * FROM users WHERE login = ?"""
    sql.execute(sql_update_query, (login,))
    records = sql.fetchall()[0]
    _, _, _, grid, _, _ = records
    sql.close()

    if grid == 1:
        return True
    else:
        return False


def get_next_fig_state(login):
    if login == 'guest':
        return True

    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql_update_query = """SELECT * FROM users WHERE login = ?"""
    sql.execute(sql_update_query, (login,))
    records = sql.fetchall()[0]
    _, _, _, _, next_fig, _ = records
    sql.close()

    if next_fig == 1:
        return True
    else:
        return False


if __name__ == '__main__':
    main('guest')
