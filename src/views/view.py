import abc
import pygame as pg


class AbstractView(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, name, config, screen, clock, sprites):
        self.name = name
        self.config = config
        self.screen = screen
        self.clock = clock
        self.sprites = sprites

    @abc.abstractmethod
    def _reset(self):
        """
        Resets properties between screen changes
        """
        pass

    def render(self):
        """
        Renders the view

        :returns: view name to transition to
        """
        self._reset()
        transition = None
        while not transition:
            for event in pg.event.get():
                if not transition:
                    transition = self._handle_event(event)
            self._update_screen()
            self._wait()
        return transition

    @abc.abstractmethod
    def _handle_event(self, event):
        """
        Handles pygame events for this screen

        :returns: view name to transition to, otherwise None
        """
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN and event.key == pg.K_F11:
            # hardcoded to the F11 key
            self._flip_fullscreen()

    def _update_screen(self):
        self.screen.fill(config['BLACK'])
        self.sprites.draw(self.screen)
        pg.display.update()

    def _flip_fullscreen(self):
        # flips full-screened-ness on or off
        if self.screen.get_flags() & pg.FULLSCREEN:
            pg.display.set_mode(self.config['size'])
        else:
            pg.display.set_mode(self.config['size'], pg.FULLSCREEN)

    def _wait(self):
        self.clock.tick(config['fps'])
