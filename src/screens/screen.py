import abc
import color_constants
import pygame as pg


class AbstractScreen(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, config, screen, clock, sprites):
        self.config = config
        self.screen = screen
        self.clock = clock
        self.sprites = sprites

    def render(self):
        rendering = True
        while rendering:
            for event in pg.event.get():
                if rendering:
                    rendering = handle_event(event)
            self.update_screen()
            self.wait()

    @abc.abstractmethod
    def handle_event(self, event):
        """
        Handles pygame events for this screen

        :returns: True/False for continued rendering
        """
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.KEYDOWN and event.key == pg.K_F11:
            # hardcoded to the F11 key
            self.flip_fullscreen()
            return True

    def update_screen(self):
        self.screen.fill(color_constants.BLACK)
        self.sprites.draw(self.screen)
        pg.display.update()

    def flip_fullscreen(self):
        # flips full-screened-ness on or off
        if self.screen.get_flags() & pg.FULLSCREEN:
            pg.display.set_mode(self.config['size'])
        else:
            pg.display.set_mode(self.config['size'], pg.FULLSCREEN)

    def wait(self):
        self.clock.tick(config['fps'])
