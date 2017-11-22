from collections import namedtuple
import enum
import pygame as pg
from sprites.sprite import AbstractPhysicsSprite


Keybinding = namedtuple('Keybinding', ['rotate_anti', 'rotate_clock', 'accelerate', 'boost'])


class Bird(AbstractPhysicsSprite):
    def __init__(self, config, color, keybind):
        size = config['bird_size']
        image = pg.Surface([size, size], pg.SRCALPHA)
        super().__init__(config, image)

        self._color = self._original_color = color
        self.image.fill(self._color)
        self.keybind = keybind
        # orientation in degrees, 0 east, positive anticlockwise
        self._orientation = 0
        self.has_ball = False
        self.boost_time = 0

        # used for rotations
        self._original_image = self.image

    def turn(self, rotation):
        self.orientation += rotation
        self._rotate_image()

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
