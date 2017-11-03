import pygame as pg
from views.game_view import GameView

class Controller:
    def __init__(self, config, screen, clock):
        self.config = config
        self.screen = screen
        self.clock = clock

        view_list = [view(config, screen, clock) for view in [GameView]]
        self.views = {view.name: view for view in view_list}

    def run(self):
        transition = 'game'  # default first view, TODO: something more customisable
        while True:
            next_view = self.views[transition]
            transition = next_view.render()
