import pygame as pg
from src import config as cfg
from src.obj.Button import Button, KeymapButton


def run(screen, settings):
    clock = pg.time.Clock()
    sprites = pg.sprite.Group()

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
                        code = s.click()
                        if code is not None:
                            return code
                    except NotImplementedError:
                        pass

        screen.fill(cfg.BLACK)
        sprites.draw(screen)
        pg.display.update()
        clock.tick(cfg.FPS)

    return cfg.EXIT_CODE
