import src.screens.MainMenu as MainMenu
import src.screens.Controls as Controls
import src.screens.Select as Select
import src.screens.Game as Game
import pygame as pg


if __name__ == '__main__':
    pg.init()
    clock = pg.time.Clock()

    # The ordering must follow the return codes in config with exit last
    states = [MainMenu.run, Controls.run, Select.run, Game.run, pg.exit]
    settings = {}
    return_code = 0
    while True:
        return_code = states[return_code](settings)
