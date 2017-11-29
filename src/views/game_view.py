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

import random

import pygame as pg
from pygame.math import Vector2

from common.team import Team
from sprites.ball import Ball
from sprites.bird import Bird, Keybinding
from sprites.goal import Goal
from sprites.scoreboard import Scoreboard
from views.view import AbstractView


class GameView(AbstractView):
    def __init__(self, config, screen, clock):
        self.b1 = Bird(config,
                       pg.Color('RED'),
                       Keybinding(rotate_anti=pg.K_a, rotate_clock=pg.K_d, accelerate=pg.K_f, boost=pg.K_g),
                       Team.LEFT)
        self.b2 = Bird(config,
                       pg.Color('BLUE'),
                       Keybinding(rotate_anti=pg.K_LEFT, rotate_clock=pg.K_RIGHT, accelerate=pg.K_SLASH, boost=pg.K_PERIOD),
                       Team.RIGHT)
        self.g1 = Goal(config, config['goal_size'], pg.Color('GREEN'), Team.LEFT)
        self.g2 = Goal(config, config['goal_size'], pg.Color('GREEN'), Team.RIGHT)
        self.scoreboard = Scoreboard(config, pg.Color('WHITE'))
        self.birds = [self.b1, self.b2]
        self.goals = [self.g1, self.g2]
        self.ball = Ball(config)
        sprites = pg.sprite.Group(self.ball, *self.birds, *self.goals, self.scoreboard)

        self.score = {team: 0 for team in Team}
        super().__init__('game', config, screen, clock, sprites)

    def _init_constants(self):
        super()._init_constants()
        self.acceleration_from_gravity = Vector2(0, self.config['accel'])
        self.ball_stolen_color = pg.Color('YELLOW')

    def _soft_reset(self):
        """
        Resets properties enough to start a new round of the game

        This is distinct from _reset which is used for screen transitions
        """
        screen_x, screen_y = self.config['size']
        for bird in self.birds:
            if bird.team is Team.LEFT:
                bird.center = (screen_x // 2 - 400, screen_y // 2)
                bird.orientation = 0  # facing right
            else:
                bird.center = (screen_x // 2 + 400, screen_y // 2)
                bird.orientation = 180  # facing left
            bird.drop_ball()
        self.sprites.add(self.ball)
        self.ball.center = self.screen_rect.center
        self.ball.acceleration = Vector2(self.acceleration_from_gravity)

        # TODO: proper initial launching
        self.ball.velocity = Vector2(5).rotate(random.randrange(0, 360))

    def _reset(self):
        screen_x, screen_y = self.config['size']
        # place goals on opposite sides of the starting positions
        self.g1.center = (screen_x, screen_y // 2)
        self.g2.center = (0, screen_y // 2)
        self.scoreboard.center = (screen_x // 2, 0)

        self.g1.rect.clamp_ip(self.screen_rect)
        self.g2.rect.clamp_ip(self.screen_rect)
        self.scoreboard.rect.clamp_ip(self.screen_rect)

        self.score = {team: 0 for team in Team}
        self.scoreboard.score = self.score
        self._soft_reset()

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

        # bird-ball interaction
        # assumes that ball isn't on-screen iff exactly one bird has the ball
        if self.ball in self.sprites:
            # bird picking up a ball
            for bird in self.birds:
                if pg.sprite.collide_rect(self.ball, bird):
                    bird.take_ball(self.ball_stolen_color)
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
                        victim.velocity += Vector2(self.config['boost_speed']).rotate(random.randrange(0, 360))
                        thief.take_ball(self.ball_stolen_color)
                        thief.invulnerability += self.config['thief_invuln_time']
                        break

        # scoring
        ball_rect = None
        if self.ball in self.sprites:
            ball_rect = self.ball.rect
        else:
            ball_rect = next(bird.rect for bird in self.birds if bird.has_ball)
        if ball_rect is not None:
            for goal in self.goals:
                if goal.rect.contains(ball_rect):
                    # score for the team that owns the goalposts
                    self.score[goal.team] += 1
                    self.scoreboard.score = self.score
                    self._soft_reset()
                    break

        for bird in self.birds:
            bird.keep_inside(self.screen_rect)

    def _handle_bird_keypresses(self, pressed, bird):
        if pressed[bird.keybind.rotate_anti]:
            bird.orientation += self.config['bird_rotation_speed']
        if pressed[bird.keybind.rotate_clock]:
            bird.orientation -= self.config['bird_rotation_speed']

        if pressed[bird.keybind.accelerate]:
            if bird.has_ball:
                bird.acceleration = Vector2(self.config['accel_ball'])
            else:
                bird.acceleration = Vector2(self.config['accel'])

            bird.acceleration.rotate_ip(-bird.orientation)
        else:
            # gravity
            bird.acceleration = Vector2(0, self.config['accel'])

        if pressed[bird.keybind.boost]:
            if pressed[bird.keybind.accelerate]:
                bird.acceleration = bird.acceleration.lerp(Vector2(self.config['accel'] / self.config['boost_slowdown']).rotate(-bird.orientation),
                                                           bird.boost_time / self.config['boost_time_required'])
            bird.boost_time = min(bird.boost_time + 1, self.config['boost_time_required'])
        elif bird.boost_time > 0:
            speed = self.config['ball_launch_speed'] if bird.has_ball else self.config['boost_speed']
            launchv = Vector2().lerp(Vector2(speed),
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

        # drag
        bird.acceleration -= self.config['bird_drag'] * bird.velocity
