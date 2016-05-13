import ObjBase
BIRD_MASS = 10
BIRD_ELASTICITY = 0


class Bird(ObjBase.PhysicalObject):
    def __init__(self, position, orientation=None, velocity=0, acceleration=0, elasticity=BIRD_ELASTICITY, mass=BIRD_MASS):
        super().__init__(position, velocity, acceleration, elasticity, mass)
        if orientation is None:
            orientation = ObjBase.Vector(arg=0)
