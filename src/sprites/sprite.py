# Copyright 2017 Julian Tu

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import abc

import pygame as pg
from pygame.math import Vector2


class AbstractStaticSprite(pg.sprite.Sprite, metaclass=abc.ABCMeta):
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

    @property
    def center(self):
        return self.rect.center

    @center.setter
    def center(self, value):
        self.rect.center = value


class AbstractPhysicsSprite(pg.sprite.Sprite, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, config, image):
        super().__init__()
        self.config = config
        self.image = image
        self.velocity = Vector2()
        self.acceleration = Vector2()
        self.invulnerability = 0

        # interact with this position vector instead of rect for accuracy
        self._rect = self.image.get_rect()
        self._position = Vector2(self._rect.x, self._rect.y)

        self._contained = False

    def move(self):
        self.velocity += self.acceleration
        self._position += self.velocity
        self.invulnerability = max(self.invulnerability - 1, 0)

    def keep_inside(self, containing_rect):
        # cannot clamp in place because rect is virtual
        if not containing_rect.contains(self.rect):
            self.rect = self.rect.clamp(containing_rect)
            self._contained = True

    def was_contained(self):
        """
        Returns whether there was a successful call to keep_inside

        Failed calls to keep_inside do not invalidate containment
        until it is called again
        """
        if self._contained:
            self._contained = False
            return True
        return False

    @property
    def position(self):
        """
        Gets the position vector

        The attributes of rect are derived from the position vector
        Setting rect still updates the position vector though
        """
        return self._position

    @position.setter
    def position(self, value):
        self._position = value
        self._rect.centerx = round(self._position.x)
        self._rect.centery = round(self._position.y)

    @property
    def rect(self):
        """
        Gets the pseudo-virtual attribute rect

        Generated based on the position vector
        """
        self._rect.centerx = round(self._position.x)
        self._rect.centery = round(self._position.y)
        return self._rect

    @rect.setter
    def rect(self, value):
        """
        Sets the pseudo-virtual attribute rect

        Do not set the normal pygame.Rect's virtual attributes
        """
        self._rect = value
        self._position.x = self._rect.centerx
        self._position.y = self._rect.centery

    @property
    def center(self):
        return self._rect.center

    @center.setter
    def center(self, value):
        """
        Gets the center of the sprite's rect

        Used because you cannot access virtual attributes of the
        virtual rect
        """
        self._rect.center = value
        self._position.x = self._rect.x
        self._position.y = self._rect.y
