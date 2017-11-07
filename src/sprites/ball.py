import pygame as pg
from sprites.sprite import AbstractPhysicsSprite


class Ball(AbstractPhysicsSprite):
    def __init__(self, config):
        size = config['ball_size']
        image = pg.Surface([size, size], pg.SRCALPHA)
        pg.draw.circle(image, pg.Color('WHITE'), image.get_rect().center, size // 2)
        super().__init__(config, image)
