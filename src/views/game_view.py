import pygame as pg
from pygame.math import Vector2
from sprites.ball import Ball
from sprites.bird import Bird, Keybinding, Rotation
from views.view import AbstractView


DRAG_COEFFICIENT = 0.01


def handle_bird_movement(pressed_keys, bird):
    if pressed_keys[bird.keybind.rotate_anti]:
        bird.turn(Rotation.ANTICLOCKWISE)
    if pressed_keys[bird.keybind.rotate_clock]:
        bird.turn(Rotation.CLOCKWISE)
    if pressed_keys[bird.keybind.accelerate]:
        # negative of orientation because rotate goes clockwise
        # boosting in one direction imparts a constant velocity
        bird.velocity = Vector2(bird.config['speed'], 0).rotate(-bird.orientation)
        bird.acceleration = Vector2(0, 0)
    else:
        # gravity
        bird.acceleration = Vector2(0, bird.config['accel'])
        # drag
        bird.acceleration += -DRAG_COEFFICIENT * bird.velocity


class GameView(AbstractView):
    def __init__(self, config, screen, clock):
        sprites = pg.sprite.Group()
        self.b1 = Bird(config,
                       pg.Color('RED'),
                       Keybinding(rotate_anti=pg.K_a, rotate_clock=pg.K_d, accelerate=pg.K_f),
                       handle_bird_movement)
        self.b2 = Bird(config,
                       pg.Color('BLUE'),
                       Keybinding(rotate_anti=pg.K_LEFT, rotate_clock=pg.K_RIGHT, accelerate=pg.K_SLASH),
                       handle_bird_movement)
        self.birds = [self.b1, self.b2]

        self.ball = Ball(config)
        sprites.add(self.ball, *self.birds)
        super().__init__('game', config, screen, clock, sprites)
        self._init_constants()

    def _init_constants(self):
        self.acceleration_from_gravity = Vector2(0, self.config['accel'])

    def _reset(self):
        for bird in self.birds:
            bird.center = self.screen_rect.center
        self.ball.center = self.screen_rect.center
        self.ball.acceleration = Vector2(self.acceleration_from_gravity)
        self.ball.velocity = Vector2(5, 0)  # FIXME: temp for testing

    def _handle_keypresses(self, pressed):
        # debugging
        if pressed[pg.K_p]:
            self._reset()
        for bird in self.birds:
            bird.handle_keypresses(pressed)
        return super()._handle_keypresses(pressed)

    def _handle_bookkeeping(self):
        # movement for birds
        for bird in self.birds:
            bird.move()
            bird.keep_inside(self.screen_rect)

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

        if self.ball in self.sprites:
            # bird picking up a ball
            for bird in self.birds:
                if pg.sprite.collide_rect(self.ball, bird):
                    bird.take_ball(pg.Color('YELLOW'))
                    self.ball.kill()
        else:
            # steal the ball from another bird
            # assumes that ball isn't on-screen iff exactly one bird has the ball
            victim = next(bird for bird in self.birds if bird.has_ball)
            for thief in self.birds:
                if thief is not victim and pg.sprite.collide_rect(thief, victim):
                    victim.drop_ball()
                    thief.take_ball(pg.Color('YELLOW'))
