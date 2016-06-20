import pygame as pg
import src.screens.MainMenu as MainMenu
import src.screens.Controls as Controls
import src.screens.Select as Select
import src.screens.Game as Game
import src.config as cfg
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Plays a game')
    parser.add_argument('-d', '--debug',
                        type=int,
                        default=0,
                        help='tarts game on screen with specified screen code')
    args = parser.parse_args()
    cfg.DEFAULT_SCREEN_CODE = args.debug

    pg.init()
    # The ordering must follow the return codes in cfg
    # Each state must implement a function run(screen, settings)
    states = [MainMenu.run, Controls.run, Select.run, Game.run]
    screen = pg.display.set_mode([cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT])
    pg.display.set_caption(cfg.GAME_CAPTION)
    settings = dict(cfg.DEFAULT_SETTINGS)

    return_code = cfg.DEFAULT_SCREEN_CODE
    while return_code != cfg.EXIT_CODE:
        return_code = states[return_code](screen, settings)
