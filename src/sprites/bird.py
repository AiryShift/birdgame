from collections import namedtuple
import enum
import pygame as pg
from sprites.sprite import AbstractPhysicsSprite


class Rotation(enum.Enum):
    CLOCKWISE = enum.auto()
    ANTICLOCKWISE = enum.auto()


Keybinding = namedtuple('Keybinding', ['rotate_anti', 'rotate_clock', 'accelerate', 'boost'])


class Bird(AbstractPhysicsSprite):
    def __init__(self, config, color, keybind):
        size = config['bird_size']
        image = pg.Surface([size, size], pg.SRCALPHA)
        super().__init__(config, image)

        self.color = self.original_color = color
        self.keybind = keybind
        # orientation in degrees, 0 east, positive anticlockwise
        self.orientation = 0
        self.has_ball = False
        self.boost_time = 0

        # used for rotations
        self.original_image = self.image

    def turn(self, rotation):
        if rotation is Rotation.CLOCKWISE:
            self.orientation -= 5  # FIXME: better value
        else:
            self.orientation += 5  # FIXME: better value
        self._normalise_orientation()

        self.image = pg.transform.rotate(self.original_image, self.orientation)
        # rect needs to be readjusted to maintain original position
        self.rect = self.image.get_rect(center=self.center)

    def _normalise_orientation(self):
        if self.orientation > 0:
            while self.orientation > 360:
                self.orientation -= 360
        elif self.orientation < 0:
            while self.orientation < 0:
                self.orientation += 360

    def take_ball(self, color):
        self.color = color
        self.has_ball = True

    def drop_ball(self):
        self.color = self.original_color
        self.has_ball = False

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
        self.image.fill(self._color)
