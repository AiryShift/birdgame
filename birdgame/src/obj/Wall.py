from . import ObjBase
from src import cfg as cfg
import pygame as pg


class Wall(pg.sprite.Sprite, ObjBase.PhysicalObject):
    def __init__(self, position, size, color=cfg.WHITE):
        pg.sprite.Sprite.__init__(self)
        ObjBase.PhysicalObject.__init__(self, position, size,
                                        None, None, None, None)
        self.image.fill(color)

    def move(self):
        raise ObjBase.PhysicalError('Walls do not move')
