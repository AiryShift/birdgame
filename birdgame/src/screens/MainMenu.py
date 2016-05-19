import pygame as pg
from ..obj.Wall import Wall
from ..obj.ObjBase import Vector
from .. import config


def run(screen, settings):
    clock = pg.time.Clock()
    sprites = pg.sprite.Group()
    sprites.add(Wall(Vector(x=10, y=10), Vector(x=20, y=20)))
    quit = False

    while not quit:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit = True

        screen.fill(config.BLACK)
        sprites.draw(screen)
        pg.display.update()
        clock.tick(config.FPS)

    return config.EXIT_CODE


if __name__ == '__main__':
    pg.init()
