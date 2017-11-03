#! /usr/bin/env python

from controller import Controller
import json
import pygame as pg


if __name__ == '__main__':
    with open('config.json') as json_file:
        config = json.loads(json_file.read())

    pg.init()
    screen = pg.display.set_mode(
        config['size'],
        pg.FULLSCREEN
    )
    pg.display.set_caption(config['title'])
    clock = pg.time.Clock()

    controller = Controller(config, screen, clock)
    controller.run()
