import pygame as pg
from src.obj.Wall import Wall
from src.obj.Button import Button
from src.Vector import Vector
from src import config


def run(screen, settings):
    clock = pg.time.Clock()
    sprites = pg.sprite.Group()
    sprites.add(Wall(Vector(x=245, y=10), Vector(x=245, y=502)))
    sprites.add(Button(Vector(), 100, 'i am not happy'))
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
