from src.Vector import Vector
from src.config import config
from . import ObjBase


class Bird(ObjBase.PhysicalObject):
    def __init__(
            self, position, team, image, velocity=0,
            acceleration=0, elasticity=config.BIRD_ELASTICITY,
            mass=config.BIRD_MASS, orientation=None, has_ball=False):
        raise NotImplementedError
        super().__init__(position, None, velocity, acceleration, elasticity,
                         mass)
        if orientation is None:
            self.orientation = Vector(arg=0)
        self.team = team
        self.has_ball = has_ball
