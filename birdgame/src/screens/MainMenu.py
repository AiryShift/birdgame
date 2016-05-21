import pygame as pg
from src.obj.Button import Button
from src.Vector import Vector
from src import config as cfg


def play_button_click():
    return cfg.SELECT_CODE


def controls_button_click():
    return cfg.CONTROLS_CODE


def run(screen, settings):
    clock = pg.time.Clock()
    sprites = pg.sprite.Group()
    play_button = Button(position=Vector(x=cfg.buttons.PLAY_BUTTON_X,
                                         y=cfg.buttons.PLAY_BUTTON_Y),
                         size=cfg.buttons.PLAY_BUTTON_SIZE, text='Play',
                         click=play_button_click)
    controls_button = Button(position=Vector(x=cfg.buttons.CONTROLS_BUTTON_X,
                                             y=cfg.buttons.CONTROLS_BUTTON_Y),
                             size=cfg.buttons.CONTROLS_BUTTON_SIZE,
                             text='Controls', click=controls_button_click)
    sprites.add(play_button, controls_button)
    quit = False

    while not quit:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit = True
            elif event.type == pg.MOUSEBUTTONUP:
                mouse_pos = pg.mouse.get_pos()
                clicked_sprites = (
                    s for s in sprites if s.rect.collidepoint(mouse_pos))
                for s in clicked_sprites:
                    try:
                        return s.click()
                    except NotImplementedError:
                        pass

        screen.fill(cfg.BLACK)
        sprites.draw(screen)
        pg.display.update()
        clock.tick(cfg.FPS)

    return cfg.EXIT_CODE


if __name__ == '__main__':
    pg.init()
