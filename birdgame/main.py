import src.screens.MainMenu as MainMenu
import src.screens.Controls as Controls
import src.screens.Select as Select
import src.screens.Game as Game
import src.config as cfg
import pygame as pg

if __name__ == '__main__':
    pg.init()
    # The ordering must follow the return codes in cfg
    states = [MainMenu.run, Controls.run, Select.run, Game.run]
    screen = pg.display.set_mode([cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT])
    pg.display.set_caption(cfg.GAME_CAPTION)
    settings = {}

    return_code = cfg.DEFAULT_SCREEN_CODE
    while return_code != cfg.EXIT_CODE:
        return_code = states[return_code](screen, settings)
