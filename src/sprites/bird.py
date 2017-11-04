import enum
import pygame as pg
from sprites.sprite import AbstractPhysicsSprite


class Rotation(enum.Enum):
    CLOCKWISE = enum.auto()
    ANTICLOCKWISE = enum.auto()


class Bird(AbstractPhysicsSprite):
    def __init__(self, config):
        image = pg.Surface([10, 10])
        image.fill(pg.Color('RED'))
        super().__init__(config, image)

        # orientation in degrees, 0 east, positive anticlockwise
        self.orientation = 0

    def move(self):
        super().move()

    def turn(self, rotation):
        if rotation is Rotation.CLOCKWISE:
            self.orientation -= 5  # FIXME: better value
        else:
            self.orientation += 5  # FIXME: better value
        self.orientation = Bird._normalise_orientation(orientation)

    @staticmethod
    def _normalise_orientation(orientation):
        if orientation > 0:
            while orientation > 360:
                orientation -= 360
        elif orientation < 0:
            while orientation < 0:
                orientation += 360
        return orientation
