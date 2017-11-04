import pygame as pg
from sprites.bird import Bird, Rotation
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
        super()._handle_event(event)

    def _handle_keypresses(self, pressed):
        if pressed[pg.K_a]:
            self.b1.turn(Rotation.ANTICLOCKWISE)
        if pressed[pg.K_d]:
            self.b1.turn(Rotation.CLOCKWISE)
        if pressed[pg.K_LSHIFT]:
            self.b1.move()

        return super()._handle_keypresses(pressed)
