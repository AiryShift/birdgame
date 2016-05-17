from . import ObjBase


class Wall(ObjBase.PhysicalObject):
    def __init__(self):
        pass

    def move(self):
        raise TypeError('Walls do not move')
