import pygame as pg
from pygame.math import Vector2
from sprites.ball import Ball
from sprites.bird import Bird, Rotation
from views.view import AbstractView


DRAG_COEFFICIENT = 0.01


class GameView(AbstractView):
    def __init__(self, config, screen, clock):
        sprites = pg.sprite.Group()
        self.b1 = Bird(config, pg.Color('RED'))
        self.ball = Ball(config)
        sprites.add(self.b1, self.ball)
        super().__init__('game', config, screen, clock, sprites)

    def _reset(self):
        self.b1.center = self.screen_rect.center
        self.ball.center = self.screen_rect.center

    def _handle_keypresses(self, pressed):
        if pressed[pg.K_a]:
            self.b1.turn(Rotation.ANTICLOCKWISE)
        if pressed[pg.K_d]:
            self.b1.turn(Rotation.CLOCKWISE)
        # debugging
        if pressed[pg.K_p]:
            self._reset()

        if pressed[pg.K_f]:
            # negative of orientation because rotate goes clockwise
            # boosting in one direction imparts a constant velocity
            self.b1.velocity = Vector2(self.config['speed'], 0).rotate(-self.b1.orientation)
            self.b1.acceleration = Vector2(0, 0)
        else:
            # gravity, max velocity is capped
            if self.b1.velocity.y < 2 * self.config['speed']:
                self.b1.acceleration = Vector2(0, self.config['accel'])
            # drag
            self.b1.acceleration += -DRAG_COEFFICIENT * self.b1.velocity

        return super()._handle_keypresses(pressed)

    def _handle_bookkeeping(self):
        self.b1.move()
        self.b1.keep_inside(self.screen_rect)
