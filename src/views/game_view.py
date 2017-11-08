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
        self._init_constants()

    def _init_constants(self):
        self.acceleration_from_gravity = Vector2(0, self.config['accel'])

    def _reset(self):
        self.b1.center = self.screen_rect.center
        self.ball.center = self.screen_rect.center
        self.ball.acceleration = Vector2(self.acceleration_from_gravity)
        self.ball.velocity = Vector2(5, 0)  # FIXME: temp for testing

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
            # gravity
            self.b1.acceleration = Vector2(self.acceleration_from_gravity)
            # drag
            self.b1.acceleration += -DRAG_COEFFICIENT * self.b1.velocity

        return super()._handle_keypresses(pressed)

    def _handle_bookkeeping(self):
        # movement for birds
        self.b1.move()
        self.b1.keep_inside(self.screen_rect)


        # movement for the ball
        # bounce
        if self.ball.was_contained():
            THRESHOLD = 50  # FIXME: better way
            # checking distance from walls to determine which it bounced off

            # left or right
            if self.ball.rect.x < THRESHOLD or self.ball.rect.x > self.screen_rect.width - THRESHOLD:
                self.ball.velocity.x *= -1
            # top or bottom
            if self.ball.rect.y < THRESHOLD or self.ball.rect.y > self.screen_rect.height - THRESHOLD:
                self.ball.velocity.y *= -1
        # drag
        self.ball.acceleration = Vector2(self.acceleration_from_gravity) + -DRAG_COEFFICIENT * self.ball.velocity
        self.ball.move()
        self.ball.keep_inside(self.screen_rect)
