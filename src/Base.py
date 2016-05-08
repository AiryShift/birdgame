import cmath
import math


def _principle_angle(angle):
    while angle > math.pi:
        angle -= 2 * math.pi
    while angle <= -math.pi:
        angle += 2 * math.pi
    return angle


class Vector():
    UP = math.pi / 2
    DOWN = -math.pi / 2
    LEFT = math.pi
    RIGHT = 0

    def __init__(self, modulus=1, argument=0):
        self.modulus = modulus
        self.argument = argument

    def __abs__(self):
        return self.modulus

    def __eq__(self, other):
        r_close = math.isclose(self.modulus, other.modulus)
        phi_close = math.isclose(self.argument, other.argument)
        return r_close and phi_close

    def __mul__(self, other):
        if isinstance(other, Vector):
            r = self.modulus * other.modulus
            phi = _principle_angle(self.argument + other.argument)
            return Vector(r, phi)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.modulus * other, self.argument)

    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector.__mul__(self, other)

    def __add__(self, other):
        left_rect = cmath.rect(self.modulus, self.argument)
        right_rect = cmath.rect(other.modulus, other.argument)
        r, phi = cmath.polar(left_rect + right_rect)
        return Vector(r, phi)


class PhysicalObject():
    def __init__(self, position, velocity, acceleration, elasticity):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.elasticity = elasticity

    def move(self):
        return NotImplementedError

if __name__ == '__main__':
    unit_vector = Vector()
    assert(-1 * unit_vector == Vector(1, math.pi))
