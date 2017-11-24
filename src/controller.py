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

import pygame as pg
from views.game_view import GameView

class Controller:
    def __init__(self, config, screen, clock):
        self.config = config
        self.screen = screen
        self.clock = clock

        view_list = [view(config, screen, clock) for view in [GameView]]
        self.views = {view.name: view for view in view_list}

    def run(self):
        transition = self.config['first_view']
        while True:
            next_view = self.views[transition]
            transition = next_view.render()
