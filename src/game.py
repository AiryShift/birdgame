#! /usr/bin/env python

import json
import pygame as pg


def flip_fullscreen(screen, size):
    if screen.get_flags() & pg.FULLSCREEN:
        pg.display.set_mode(size)
    else:
        pg.display.set_mode(size, pg.FULLSCREEN)


if __name__ == '__main__':
    with open('config.json') as json_file:
        config = json.loads(json_file.read())

    pg.init()
    screen_size = (config['screen_width'], config['screen_height'])
    screen = pg.display.set_mode(
        screen_size,
        pg.FULLSCREEN
    )
    pg.display.set_caption(config['title'])

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_F11:
                flip_fullscreen(screen, screen_size)
