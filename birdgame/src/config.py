import pygame as pg
FPS = 60
GAME_CAPTION = 'Bird Game, by Julian'

# Controls
PYGAME_KEYMAPPING = {
    pg.K_a: 'a',
    pg.K_b: 'b',
    pg.K_c: 'c',
    pg.K_d: 'd',
    pg.K_e: 'e',
    pg.K_f: 'f',
    pg.K_g: 'g',
    pg.K_h: 'h',
    pg.K_i: 'i',
    pg.K_j: 'j',
    pg.K_k: 'k',
    pg.K_l: 'l',
    pg.K_m: 'm',
    pg.K_n: 'n',
    pg.K_o: 'o',
    pg.K_p: 'p',
    pg.K_q: 'q',
    pg.K_r: 'r',
    pg.K_s: 's',
    pg.K_t: 't',
    pg.K_u: 'u',
    pg.K_v: 'v',
    pg.K_w: 'w',
    pg.K_x: 'x',
    pg.K_y: 'y',
    pg.K_z: 'z',
    pg.K_UP: 'up arrow',
    pg.K_DOWN: 'down arrow',
    pg.K_RIGHT: 'right arrow',
    pg.K_LEFT: 'left arrow',
    pg.K_COMMA: ',',
    pg.K_PERIOD: '.',
    pg.K_SLASH: '/',
}

DEFAULT_SETTINGS = {
    'P1_LEFT': pg.K_LEFT,
    'P1_RIGHT': pg.K_RIGHT,
    'P1_ACCEL': pg.K_SLASH,
    'P1_THROW': pg.K_PERIOD,

    'P2_LEFT': pg.K_a,
    'P2_RIGHT': pg.K_d,
    'P2_ACCEL': pg.K_e,
    'P2_THROW': pg.K_r,
}

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Display
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Different screens
EXIT_CODE = -1
MAIN_MENU_CODE = 0
CONTROLS_CODE = 1
SELECT_CODE = 2
GAME_CODE = 3

DEFAULT_SCREEN_CODE = MAIN_MENU_CODE


# Objects
BIRD_MASS = 10  # temporary
BIRD_ELASTICITY = 0

BALL_MASS = 10  # temporary
BALL_ELASTICITY = 5  # temporary


class buttons:
    # MainMenu
    PLAY_BUTTON_X = SCREEN_WIDTH // 2
    PLAY_BUTTON_Y = 420  # <3 you gongy
    PLAY_BUTTON_SIZE = 120

    CONTROLS_BUTTON_X = PLAY_BUTTON_X
    CONTROLS_BUTTON_Y = PLAY_BUTTON_Y + 100
    CONTROLS_BUTTON_SIZE = PLAY_BUTTON_SIZE

    GAME_NAME_X = PLAY_BUTTON_X
    GAME_NAME_Y = PLAY_BUTTON_Y - 170
    GAME_NAME_SIZE = 250
