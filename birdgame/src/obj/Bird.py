from . import ObjBase
BIRD_MASS = 10  # temporary
BIRD_ELASTICITY = 0
BIRD_SIZE = ObjBase.Vector(x=10, y=10)  # temporary


class Bird(ObjBase.PhysicalObject):
    def __init__(
            self, position, size=BIRD_SIZE, velocity=0, acceleration=0,
            elasticity=BIRD_ELASTICITY, mass=BIRD_MASS, orientation=None,
            has_ball=False):
        super().__init__(position, size, velocity, acceleration, elasticity,
                         mass)
        if orientation is None:
            self.orientation = ObjBase.Vector(arg=0)
        self.has_ball = has_ball
