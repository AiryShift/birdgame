# Copyright 2017 Julian Tu

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pygame as pg
from pygame.math import Vector2
from sprites.ball import Ball
from sprites.bird import Bird, Keybinding
from views.view import AbstractView
import random


class GameView(AbstractView):
    def __init__(self, config, screen, clock):
        sprites = pg.sprite.Group()
        self.b1 = Bird(config,
                       pg.Color('RED'),
                       Keybinding(rotate_anti=pg.K_a, rotate_clock=pg.K_d, accelerate=pg.K_f, boost=pg.K_g))
        self.b2 = Bird(config,
                       pg.Color('BLUE'),
                       Keybinding(rotate_anti=pg.K_LEFT, rotate_clock=pg.K_RIGHT, accelerate=pg.K_SLASH, boost=pg.K_PERIOD))
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
        # TODO: proper initial launching
        self.ball.velocity = Vector2(5, 0).rotate(random.randrange(0, 360))

    def _handle_keypresses(self, pressed):
        # debugging
        if pressed[pg.K_p]:
            self._reset()
        for bird in self.birds:
            self._handle_bird_keypresses(pressed, bird)

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
        self.ball.acceleration = Vector2(self.acceleration_from_gravity) - self.config['ball_drag'] * self.ball.velocity
        self.ball.move()
        self.ball.keep_inside(self.screen_rect)

        # assumes that ball isn't on-screen iff exactly one bird has the ball
        if self.ball in self.sprites:
            # bird picking up a ball
            for bird in self.birds:
                if pg.sprite.collide_rect(self.ball, bird):
                    bird.take_ball(pg.Color('YELLOW'))
                    self.ball.kill()
                    break
        else:
            # steal the ball from another bird
            victim = next(bird for bird in self.birds if bird.has_ball)
            if victim.invulnerability == 0:
                for thief in self.birds:
                    if thief is not victim and pg.sprite.collide_rect(thief, victim):
                        victim.drop_ball()
                        # knock the victim around
                        victim.velocity += Vector2(self.config['boost_speed'], 0).rotate(random.randrange(0, 360))
                        thief.take_ball(pg.Color('YELLOW'))
                        thief.invulnerability += self.config['thief_invuln_time']
                        break

        for bird in self.birds:
            bird.keep_inside(self.screen_rect)

    def _handle_bird_keypresses(self, pressed, bird):
        if pressed[bird.keybind.rotate_anti]:
            bird.turn(self.config['bird_rotation_speed'])
        if pressed[bird.keybind.rotate_clock]:
            bird.turn(-self.config['bird_rotation_speed'])

        if pressed[bird.keybind.accelerate]:
            bird.acceleration = Vector2(self.config['accel'], 0)

            # boost handling
            if pressed[bird.keybind.boost]:
                bird.acceleration = bird.acceleration.lerp(Vector2(self.config['accel'] / self.config['boost_slowdown']),
                                                           bird.boost_time / self.config['boost_time_required'])
                bird.boost_time = min(bird.boost_time + 1, self.config['boost_time_required'])
            else:
                if bird.boost_time > 0:
                    speed = self.config['ball_launch_speed'] if bird.has_ball else self.config['boost_speed']
                    launchv = Vector2(0, 0).lerp(Vector2(speed, 0),
                                                 bird.boost_time / self.config['boost_time_required'])
                    launchv.rotate_ip(-bird.orientation)
                    if bird.has_ball:
                        # launch the ball
                        self.ball.velocity = launchv
                        self.ball.center = bird.center
                        self.sprites.add(self.ball)

                        bird.drop_ball()
                    else:
                        # launch the bird
                        bird.velocity += launchv
                    bird.boost_time = 0
            bird.acceleration.rotate_ip(-bird.orientation)
        else:
            # gravity
            bird.acceleration = Vector2(0, self.config['accel'])
        # drag
        bird.acceleration -= self.config['bird_drag'] * bird.velocity
