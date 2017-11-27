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

from common.team import Team
from sprites.sprite import AbstractStaticSprite


def score_repr(score):
    return '{} - {}'.format(score[Team.LEFT], score[Team.RIGHT])


class Scoreboard(AbstractStaticSprite):
    def __init__(self, config, color, score=None):
        self._font = pg.font.Font(None, config['score_size'])
        self._score = score or {team: 0 for team in Team}
        self.color = color
        score_text = score_repr(self._score)
        image = self._font.render(score_text, True, color)
        super().__init__(config, image)

    @property
    def score(self):
        """
        Score for the Scoreboard

        Do not modify this in place without calling render_score afterwards
        Using the setter does not require calling render_score
        """
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
        self.render_score()

    def render_score(self):
        score_text = score_repr(self._score)
        self.image = self._font.render(score_text, True, self.color)
        self.rect = self.image.get_rect(center=self.center)
