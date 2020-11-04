from constants import ORANGE
from objects.field import Field
from objects.base import DrawableObject
import pygame

from objects.basefortable import BaseElTable
from objects.scrollbar import ScrollBar


class Frame(BaseElTable):
    def __init__(self, game):
        super().__init__(game)
        self.thickness = 12
        self.rect.x = self.game.width // 4
        self.rect.y = self.game.height // 4
        self.rect.width = self.game.width - (2 * self.rect.x)
        self.rect.height = self.game.height - self.rect.y
        self.pos = (self.get_pos_cursor())

    def process_draw(self):
        pygame.draw.rect(self.game.screen, ORANGE, self.rect, self.thickness)
