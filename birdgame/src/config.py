FPS = 60
GAME_CAPTION = 'Bird Game, by Julian'

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
