from src.Vector import Vector
from src.config import config
from . import ObjBase
BIRD_SIZE = Vector(x=10, y=10)  # temporary


class Bird(ObjBase.PhysicalObject):
    def __init__(
            self, position, team, size=config.BIRD_SIZE, velocity=0,
            acceleration=0, elasticity=config.BIRD_ELASTICITY,
            mass=config.BIRD_MASS, orientation=None, has_ball=False):
        super().__init__(position, size, velocity, acceleration, elasticity,
                         mass)
        if orientation is None:
            self.orientation = Vector(arg=0)
        self.team = team
        self.has_ball = has_ball
