import pygame as pg


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
