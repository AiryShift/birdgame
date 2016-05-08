import cmath
import math


class Vector():
    def __init__(self, x=1, y=0):
        self._vec = complex(x, y)

    @property
    def x(self):
        return self._vec.real
    
    @x.setter
    def x(self, value):
        self._vec.real = value

    @property
    def y(self):
        return self._vec.imag

    @y.setter
    def y(self, value):
        self._vec.imag = value

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)



class PhysicalObject():
    def __init__(self, position, velocity, acceleration, elasticity):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.elasticity = elasticity

    def move(self):
        return NotImplementedError

if __name__ == '__main__':
    pass