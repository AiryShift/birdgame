import pygame as pg
from src import config as cfg
from src.Vector import Vector
from src.obj.Button import Button, KeymapButton


def run(screen, settings):
    clock = pg.time.Clock()
    sprites = pg.sprite.Group()
    back_button = Button(position=Vector(x=cfg.buttons.BACK_BUTTON_X,
                                         y=cfg.buttons.BACK_BUTTON_Y),
                         size=cfg.buttons.BACK_BUTTON_SIZE, text='Back',
                         click=lambda: cfg.MAIN_MENU_CODE)

    p1_left_name = Button(position=Vector(x=cfg.buttons.CONTROLS_TOP_LEFT_X,
                                          y=cfg.buttons.CONTROLS_TOP_LEFT_Y),
                          size=cfg.buttons.CONTROLS_MENU_STD_SIZE,
                          text='P1 Left')
    p1_left_key = KeymapButton(
        position=Vector(
            x=cfg.buttons.CONTROLS_TOP_LEFT_X,
            y=cfg.buttons.CONTROLS_TOP_LEFT_Y + cfg.buttons.KEYMAP_OFFSET),
        size=cfg.buttons.CONTROLS_MENU_STD_SIZE,
        modifies='P1_LEFT', settings=settings)

    sprites.add(back_button, p1_left_name, p1_left_key)

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
            elif settings['KEYMAP_CLICKED'] and event.type == pg.KEYDOWN:
                for s in sprites:
                    if isinstance(s, KeymapButton) and s.clicked:
                        s.click(pg.key.get_pressed())

        screen.fill(cfg.BLACK)
        sprites.draw(screen)
        pg.display.update()
        clock.tick(cfg.FPS)

    return cfg.EXIT_CODE
