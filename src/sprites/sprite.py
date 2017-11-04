import abc
import pygame as pg


class AbstractSprite(pg.sprite.Sprite, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, config, image):
        """
        Initialises a sprite

        Must call this before any other initialisation
        """
        super().__init__()
        self.config = config
        self.image = image
        self.rect = self.image.get_rect()


class AbstractPhysicsSprite(AbstractSprite, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, config, image):
        super().__init__(config, image)
        self.velocity = pg.math.Vector2(0, 0)
        self.acceleration = pg.math.Vector2(0, 0)

    @abc.abstractmethod
    def move(self):
        self.velocity += self.acceleration
