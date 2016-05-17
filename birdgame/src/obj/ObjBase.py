import cmath


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
        elif not (isinstance(other, int) or isinstance(other, float)):
            raise TypeError('Vector does not support {} with type {}'.format(
                'addition', type(other)))
        result = self.vector + other
        return Vector(x=result.real, y=result.imag)

    def __mul__(self, other):
        if isinstance(other, Vector):
            other = other.vector
        elif not (isinstance(other, int) or isinstance(other, float)):
            raise TypeError('Vector does not support {} with type {}'.format(
                'multiplication', type(other)))
        result = self.vector * other
        return Vector(x=result.real, y=result.imag)

    __rmul__ = __mul__

    def __abs__(self):
        return abs(self.vector)

    def __eq__(self, other):
        if isinstance(other, Vector):
            other = other.vector
        elif not (isinstance(other, int) or isinstance(other, float)):
            raise TypeError('Vector does not support {} with type {}'.format(
                'equality', type(other)))
        return self.vector == other


class PhysicalObject:
    """
    Base class for all rendered objects

    position defines centre of mass, NOT a corner of its bounding box
    """

    def __init__(self, position, size, velocity, acceleration, elasticity,
                 mass):
        self.position = position
        self.size = size
        self.velocity = velocity
        self.acceleration = acceleration
        self.elasticity = elasticity
        self.mass = mass

    def move(self):
        """Applies acceleration and velocity vectors to movement"""
        self.velocity += self.acceleration
        self.position += self.velocity

    def detect_collision(self, other):
        """Detects collision with another object using bounding rectangle"""
        my_corner = self.position - (self.size / 2)
        other_corner = other.position - (other.size / 2)

        x_intersect = abs(my_corner.x - other_corner.x) * 2 <= (
            self.size.x + other.size.x)
        y_intersect = abs(my_corner.y - other_corner.y) * 2 <= (
            self.size.y + other.size.y)

        return x_intersect and y_intersect
