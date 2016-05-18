import src.screens.MainMenu as MainMenu
import src.screens.Controls as Controls
import src.screens.Select as Select
import src.screens.Game as Game
import src.config as config

if __name__ == '__main__':
    # The ordering must follow the return codes in config
    states = [MainMenu.run, Controls.run, Select.run, Game.run]
    settings = {}
    return_code = config.DEFAULT_SCREEN_CODE
    while return_code != config.EXIT_CODE:
        return_code = states[return_code](settings)
