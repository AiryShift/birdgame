#! /usr/bin/env python

# Copyright 2017 Julian Tu

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from controller import Controller
import json
from json_minify import json_minify
import pygame as pg


if __name__ == '__main__':
    with open('config.json') as json_file:
        config = json.loads(json_minify(json_file.read()))

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
