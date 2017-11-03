import pygame as pg
from views.view import AbstractView


class GameView(AbstractView):
    def __init__(self, config, screen, clock):
        sprites = pg.sprite.Group()
        super().__init__('game', config, screen, clock, sprites)

    def _reset(self):
        pass

    def _handle_event(self, event):
        return super()._handle_event(event)
