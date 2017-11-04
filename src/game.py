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
    # sets delay before keypress event is sent to 1ms
    # keypress event is repeated at a rate of 60Hz
    pg.key.set_repeat(1, 1000 // config['fps'])

    controller = Controller(config, screen, clock)
    controller.run()
