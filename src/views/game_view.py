import pygame as pg
from pygame.math import Vector2
from sprites.bird import Bird, Rotation
from views.view import AbstractView


class GameView(AbstractView):
    def __init__(self, config, screen, clock):
        sprites = pg.sprite.Group()
        self.b1 = Bird(config)
        sprites.add(self.b1)
        super().__init__('game', config, screen, clock, sprites)

    def _reset(self):
        self.b1.center = self.screen.get_rect().center

    def _handle_event(self, event):
        super()._handle_event(event)

    def _handle_keypresses(self, pressed):
        if pressed[pg.K_a]:
            self.b1.turn(Rotation.ANTICLOCKWISE)
        if pressed[pg.K_d]:
            self.b1.turn(Rotation.CLOCKWISE)
        if pressed[pg.K_f]:
            # negative of orientation because rotate goes clockwise
            self.b1.velocity = Vector2(3, 0).rotate(-self.b1.orientation)
        else:
            self.b1.velocity = Vector2(0, 0)
        self.b1.move()

        return super()._handle_keypresses(pressed)
