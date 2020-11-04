from constants import *
from fileuploader import FileUploader
from objects.base import DrawableObject
import pygame

from objects.basefortable import BaseElTable
from objects.text import TextObject


class Field(BaseElTable):
    std_height = 60

    def __init__(self, game, T_rect, SB_rect, T_thic=0, SB_thic=0):
        super().__init__(game)
        self.file = FileUploader(name=123, score=1)
        self.thickness = T_thic // 3
        self.SB_thic = SB_thic
        self.SB_rect = SB_rect
        self.T_rect = T_rect
        self.rect.x = self.T_rect.x + self.thickness #// 2
        self.rect.y = self.T_rect.y + self.thickness #// 2
        self.rect.width = self.T_rect.width - self.SB_rect.width - self.SB_thic*3 - self.thickness
        self.rect.height = Field.std_height
        self.name = TextObject(self.game, 0, 0, )

    def process_draw(self):
        pygame.draw.rect(self.game.screen, ORANGE, self.rect, self.thickness)

    def process_logic(self):
        self.file.read_file_data()
        print(self.file.data[1])
