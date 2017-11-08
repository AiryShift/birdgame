import abc
import pygame as pg


class AbstractView(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, name, config, screen, clock, sprites):
        self.name = name
        self.config = config
        self.screen = screen
        # assumes the screen's dimensions will not change
        self.screen_rect = self.screen.get_rect()
        self.clock = clock
        self.sprites = sprites

    def _reset(self):
        """
        Resets properties between screen changes
        """

    def render(self):
        """
        Renders the view

        :returns: view name to transition to
        """
        self._reset()
        transition = None
        while not transition:
            for event in pg.event.get():
                transition = transition or self._handle_event(event)
            transition = transition or self._handle_keypresses(pg.key.get_pressed())
            transition = transition or self._handle_bookkeeping()
            self._update_screen()
            self._wait()
        return transition

    def _handle_event(self, event):
        """
        Handles pygame events for this screen that aren't KEYDOWNs

        E.g. mousedown
        :returns: view name to transition to, otherwise None
        """
        if event.type == pg.QUIT:
            # pressing the 'X' button quits the game
            exit()

    def _handle_keypresses(self, pressed):
        """
        Handles keypresses for this screen

        :returns: view name to transition to, otherwise None
        """
        if pressed[pg.K_ESCAPE]:
            # pressing the ESC button quits the game
            exit()
        if pressed[pg.K_F11]:
            self._flip_fullscreen()

    def _handle_bookkeeping(self):
        """
        Handles general things once per render cycle

        :returns: view name to transition to, otherwise None
        """

    def _update_screen(self):
        self.screen.fill(pg.Color('BLACK'))
        self.sprites.draw(self.screen)
        pg.display.update()

    def _flip_fullscreen(self):
        # flips full-screened-ness on or off
        if self.screen.get_flags() & pg.FULLSCREEN:
            pg.display.set_mode(self.config['size'])
        else:
            pg.display.set_mode(self.config['size'], pg.FULLSCREEN)

    def _wait(self):
        self.clock.tick(self.config['fps'])
