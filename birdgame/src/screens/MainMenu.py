import pygame as pg
from src.obj.Button import Button
from src.Vector import Vector
from src import config

def play_button_click():
    return config.SELECT_CODE


def run(screen, settings):
    clock = pg.time.Clock()
    sprites = pg.sprite.Group()
    play_button = Button(position=Vector(x=config.buttons.MAIN_MENU_X,
                                         y=config.buttons.MAIN_MENU_Y),
                         size=120, text='Play',
                         click=play_button_click)
    sprites.add(play_button)
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

        screen.fill(config.BLACK)
        sprites.draw(screen)
        pg.display.update()
        clock.tick(config.FPS)

    return config.EXIT_CODE


if __name__ == '__main__':
    pg.init()
