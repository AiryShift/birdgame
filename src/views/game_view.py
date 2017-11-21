import pygame as pg
from pygame.math import Vector2
from sprites.ball import Ball
from sprites.bird import Bird, Keybinding, Rotation
from views.view import AbstractView
import random


def handle_bird_movement(pressed_keys, bird):
    if pressed_keys[bird.keybind.rotate_anti]:
        bird.turn(Rotation.ANTICLOCKWISE)
    if pressed_keys[bird.keybind.rotate_clock]:
        bird.turn(Rotation.CLOCKWISE)

    if pressed_keys[bird.keybind.accelerate]:
        bird.acceleration = Vector2(bird.config['accel'], 0)

        # boost handling
        if pressed_keys[bird.keybind.boost]:
            bird.acceleration = bird.acceleration.lerp(Vector2(bird.config['accel'] / bird.config['boost_slowdown']),
                                                       bird.boost_time / bird.config['boost_time_required'])
            bird.boost_time = min(bird.boost_time + 1, bird.config['boost_time_required'])
        else:
            if bird.boost_time > 0:
                dv = Vector2(0, 0).lerp(Vector2(bird.config['boost_speed'], 0),
                                        bird.boost_time / bird.config['boost_time_required'])
                bird.velocity += dv.rotate(-bird.orientation)
            bird.boost_time = 0
        bird.acceleration.rotate_ip(-bird.orientation)
    else:
        # gravity
        bird.acceleration = Vector2(0, bird.config['accel'])
    # drag
    bird.acceleration -= bird.config['drag'] * bird.velocity


class GameView(AbstractView):
    def __init__(self, config, screen, clock):
        sprites = pg.sprite.Group()
        self.b1 = Bird(config,
                       pg.Color('RED'),
                       Keybinding(rotate_anti=pg.K_a, rotate_clock=pg.K_d, accelerate=pg.K_f, boost=pg.K_g),
                       handle_bird_movement)
        self.b2 = Bird(config,
                       pg.Color('BLUE'),
                       Keybinding(rotate_anti=pg.K_LEFT, rotate_clock=pg.K_RIGHT, accelerate=pg.K_SLASH, boost=pg.K_PERIOD),
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
            bird.center = (0, 0)
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
        self.ball.acceleration = Vector2(self.acceleration_from_gravity) - self.config['drag'] * self.ball.velocity
        self.ball.move()
        self.ball.keep_inside(self.screen_rect)

        if self.ball in self.sprites:
            # bird picking up a ball
            for bird in self.birds:
                if pg.sprite.collide_rect(self.ball, bird):
                    bird.take_ball(pg.Color('YELLOW'))
                    self.ball.kill()
                    break
        else:
            # steal the ball from another bird
            # assumes that ball isn't on-screen iff exactly one bird has the ball
            victim = next(bird for bird in self.birds if bird.has_ball)
            for thief in self.birds:
                if thief is not victim and pg.sprite.collide_rect(thief, victim):
                    victim.drop_ball()
                    # knock the victim around
                    victim.velocity += Vector2(self.config['boost_speed'], 0).rotate(random.randrange(0, 360))
                    thief.take_ball(pg.Color('YELLOW'))
                    break

        for bird in self.birds:
            bird.keep_inside(self.screen_rect)
