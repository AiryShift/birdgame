import pygame as pg
from sprites.bird import Bird
from views.view import AbstractView


class GameView(AbstractView):
    def __init__(self, config, screen, clock):
        sprites = pg.sprite.Group()
        self.b1 = Bird(config)
        sprites.add(self.b1)
        super().__init__('game', config, screen, clock, sprites)

    def _reset(self):
        self.b1.rect.center = self.screen.get_rect().center

    def _handle_event(self, event):
        return super()._handle_event(event)
