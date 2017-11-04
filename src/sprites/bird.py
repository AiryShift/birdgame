import pygame as pg
from sprites.sprite import AbstractPhysicsSprite


class Bird(AbstractPhysicsSprite):
    def __init__(self, config):
        image = pg.Surface([10, 10])
        image.fill(pg.Color('RED'))
        super().__init__(config, image)

        self.direction = 0

    def move(self):
        super().move()
