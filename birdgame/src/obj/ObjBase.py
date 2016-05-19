import cmath
import pygame as pg


def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    """https://docs.python.org/3/library/cmath.html#cmath.isclose"""
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


class Vector:
    def __init__(self, *, x=1, y=0, arg=None):
        if arg is not None:
            self.vector = cmath.rect(1, arg)
        else:
            self.vector = complex(x, y)

    @property
    def x(self):
        return self.vector.real

    @x.setter
    def x(self, value):
        self.vector.real = value

    @property
    def y(self):
        return self.vector.imag

    @y.setter
    def y(self, value):
        self.vector.imag = value

    def __add__(self, other):
        if isinstance(other, Vector):
            other = other.vector
        result = self.vector + other
        return Vector(x=result.real, y=result.imag)

    def __mul__(self, other):
        if isinstance(other, Vector):
            other = other.vector
        result = self.vector * other
        return Vector(x=result.real, y=result.imag)

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, Vector):
            other = other.vector
        result = self.vector / other
        return Vector(x=result.real, y=result.imag)

    def __sub__(self, other):
        return self + (-1 * other)

    def __abs__(self):
        return abs(self.vector)

    def __eq__(self, other):
        if isinstance(other, Vector):
            other = other.vector
        return isclose(self.vector, other)


class PhysicalError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class PhysicalObject:
    """
    Base class for all rendered objects

    position defines centre of mass, NOT a corner of its bounding box
    """

    def __init__(self, position, size, velocity, acceleration, elasticity,
                 mass):
        self.rect = pg.Rect(0, 0, 0, 0)
        self.rect.center = (position.x, position.y)
        self.rect.size = (size.x, size.y)

        self.velocity = velocity
        self.acceleration = acceleration
        self.elasticity = elasticity
        self.mass = mass

    @property
    def x(self):
        return self.rect.centerx

    @x.setter
    def x(self, value):
        self.rect.centerx = value

    @property
    def y(self):
        return self.rect.centery

    @y.setter
    def y(self, value):
        self.rect.centery = value

    def move(self):
        """Applies acceleration and velocity vectors to displacement"""
        self.velocity += self.acceleration
        self.x += self.velocity.x
        self.y += self.velocity.y
