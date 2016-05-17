from . import ObjBase


class Wall(ObjBase.PhysicalObject):
    def __init__(self, position, size):
        super().__init__(position, size, None, None, None, None)

    def move(self):
        raise ObjBase.PhysicalError('Walls do not move')
