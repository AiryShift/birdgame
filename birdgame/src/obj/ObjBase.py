import cmath
import math


class Vector():
    def __init__(self, *, x=1, y=0, arg=None):
        if arg is not None:
            self.vec = cmath.rect(1, arg)
        else:
            self.vec = complex(x, y)

    @property
    def x(self):
        return self.vec.real

    @x.setter
    def x(self, value):
        self.vec.real = value

    @property
    def y(self):
        return self.vec.imag

    @y.setter
    def y(self, value):
        self.vec.imag = value

    def __add__(self, other):
        if isinstance(other, Vector):
            other = other.vec
        elif not (isinstance(other, int) or isinstance(other, float)):
            raise TypeError('Vector does not support {} with type {}'.format(
                'addition', type(other)))
        result = self.vec + other
        return Vector(x=result.real, y=result.imag)

    def __mul__(self, other):
        if isinstance(other, Vector):
            other = other.vec
        elif not (isinstance(other, int) or isinstance(other, float)):
            raise TypeError('Vector does not support {} with type {}'.format(
                'multiplication', type(other)))
        result = self.vec * other
        return Vector(x=result.real, y=result.imag)

    __rmul__ = __mul__

    def __abs__(self):
        return abs(self.vec)

    def __eq__(self, other):
        if isinstance(other, Vector):
            other = other.vec
        elif not (isinstance(other, int) or isinstance(other, float)):
            raise TypeError('Vector does not support {} with type {}'.format(
                'equality', type(other)))
        return self.vec == other


class PhysicalObject():
    def __init__(self, position, velocity, acceleration, elasticity, mass):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.elasticity = elasticity
        self.mass = mass

    def move(self):
        self.velocity += self.acceleration
        self.position += self.velocity

if __name__ == '__main__':
    assert(Vector(arg=0) == Vector(x=1, y=0))
    try:
        Vector(arg=0) + 'a'
    except TypeError:
        pass
    assert(Vector(arg=0) * 2 == Vector(x=2))
    assert(2 * Vector(arg=0) == Vector(x=2))