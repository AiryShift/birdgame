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

from collections import namedtuple

import pygame as pg

from sprites.sprite import AbstractPhysicsSprite

Keybinding = namedtuple('Keybinding', ['rotate_anti', 'rotate_clock', 'accelerate', 'boost'])


class Bird(AbstractPhysicsSprite):
    def __init__(self, config, color, keybind, team):
        size = config['bird_size']
        image = pg.Surface([size, size], pg.SRCALPHA)
        super().__init__(config, image)

        self._color = self._original_color = color
        self.image.fill(self._color)
        self.keybind = keybind
        self.team = team
        # orientation in degrees, 0 east, positive anticlockwise
        self._orientation = 0
        self.has_ball = False
        self.boost_time = 0

        # used for rotations
        self._original_image = self.image

    def _rotate_image(self):
        self.image = pg.transform.rotate(self._original_image, self.orientation)
        # rect needs to be readjusted to maintain original position
        self.rect = self.image.get_rect(center=self.center)

    def take_ball(self, color):
        self.color = color
        self.has_ball = True

    def drop_ball(self):
        self.color = self._original_color
        self.has_ball = False

    def _init_image(self, color):
        size = self.config['bird_size']
        image = pg.Surface([size, size], pg.SRCALPHA)
        image.fill(color)
        return image

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
        self._original_image = self._init_image(self._color)
        self._rotate_image()

    @property
    def orientation(self):
        return self._orientation

    @orientation.setter
    def orientation(self, value):
        self._orientation = value
        # restrict possible values
        if self._orientation > 360:
            while self._orientation > 360:
                self._orientation -= 360
        elif self._orientation < 0:
            while self._orientation < 0:
                self._orientation += 360
        self._rotate_image()
