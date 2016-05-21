from src.Vector import Vector
from . import ObjBase
from src import config as cfg
import pygame as pg


class Button(pg.sprite.Sprite, ObjBase.PhysicalObject):
    def __init__(self, position, size, text, *,
                 text_colour=cfg.WHITE, bg_colour=cfg.BLACK,
                 click=None):
        pg.sprite.Sprite.__init__(self)
        ObjBase.PhysicalObject.__init__(self, position, Vector(),
                                        None, None, None, None)
        self.image.fill(bg_colour)
        self.font = pg.font.Font(None, size)
        self.image = self.font.render(text, False, text_colour, bg_colour)
        self.rect = self.image.get_rect()
        self.rect.center = (position.x, position.y)
        if click is not None:
            self.click = click
