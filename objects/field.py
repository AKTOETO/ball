from constants import *
from fileuploader import FileUploader
from objects.base import DrawableObject
import pygame

from objects.basefortable import BaseElTable
from objects.text import TextObject


class Field(BaseElTable):
    std_height = 35

    def __init__(self, game, T_rect, SB_rect, Number, T_thic=0, SB_thic=0, shift=0):
        super().__init__(game)
        self.can_draw = True
        self.shift = shift
        self.num = Number
        self.thickness = T_thic // 3
        self.SB_thic = SB_thic
        self.SB_rect = SB_rect
        self.T_rect = T_rect
        self.rect.x = self.T_rect.x + self.thickness  # // 2
        self.rect.y = self.T_rect.y + self.thickness + self.shift  # // 2
        self.rect.width = self.T_rect.width - self.SB_rect.width - self.SB_thic * 3 - self.thickness
        self.rect.height = Field.std_height
        self.text = TextObject(self.game, 0, 0, self.get_status_text(), WHITE)

    def check_borders(self):
        if self.rect.y < self.T_rect.y:
            self.can_draw = False
        else:
            self.can_draw = True

    def process_draw(self):
        self.check_borders()
        if self.can_draw:
            pygame.draw.rect(self.game.screen, ORANGE, self.rect, self.thickness)
            self.text.process_draw()

    def get_status_text(self):
        #self.game.fileul.read_file_data()
        return f'Name: {self.game.fileul.data[self.num][0]} Score: {self.game.fileul.data[self.num][1]}'

    def process_logic(self):
        self.text.update_text(self.get_status_text())
        self.text.move_center(self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2)

    def set_pos_y(self, y):
        self.rect.y = self.T_rect.y + self.thickness + self.shift + y
