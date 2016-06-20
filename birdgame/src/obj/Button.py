import pygame as pg
from src.Vector import Vector
from . import ObjBase
from src import config as cfg


class Button(pg.sprite.Sprite, ObjBase.PhysicalObject):
    def __init__(self, position, size, text, *,
                 text_colour=cfg.WHITE, bg_colour=cfg.BLACK,
                 click=None):
        self.text_colour = text_colour
        self.bg_colour = bg_colour
        self.position = position
        self._text = text

        pg.sprite.Sprite.__init__(self)
        ObjBase.PhysicalObject.__init__(self, position, Vector(),
                                        None, None, None, None)

        self.font = pg.font.Font(None, size)
        self.image = self.font.render(
            self._text, False, self.text_colour, self.bg_colour)

        self.rect = self.image.get_rect()
        self.rect.center = (position.x, position.y)

        if click is not None:
            self.click = click

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, new_text):
        self._text = new_text
        self.image = self.font.render(
            self._text, False, self.text_colour, self.bg_colour)
        self.rect = self.image.get_rect()
        self.rect.center = (self.position.x, self.position.y)


class KeymapButton(Button):
    def __init__(self, position, size, modifies, settings, *,
                 text_colour=cfg.WHITE, bg_colour=cfg.BLACK):
        self.settings = settings  # Global settings dictionary
        super().__init__(position, size,
                         text=cfg.PYGAME_KEYMAPPING[self.settings[modifies]])
        self.settings['KEYMAP_CLICKED'] = False
        self.clicked = False

    def click(self, pressed_keys=None):
        if not self.settings['KEYMAP_CLICKED']:
            self.text = 'press a button'
            self.clicked = True
            self.settings['KEYMAP_CLICKED'] = True
        elif self.clicked:
            if pressed_keys is None:
                return
            for key in cfg.PYGAME_KEYMAPPING:
                if pressed_keys[key]:
                    self.text = cfg.PYGAME_KEYMAPPING[key]
                    self.clicked = False
                    self.settings['KEYMAP_CLICKED'] = False
                    break
