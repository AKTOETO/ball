from objects.field import Field
from objects.base import DrawableObject
import pygame

from objects.basefortable import BaseElTable
from objects.scrollbar import ScrollBar
from objects.frame import Frame


class Table(BaseElTable):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.game.fileul.read_file_data()
        self.objects.append(Frame(game))
        self.objects.append(ScrollBar(game, self.objects[0].rect, self.objects[0].thickness))
        self.count_fields()

    def count_fields(self):
        s_data = sorted(self.game.fileul.data[1:], key=lambda val: val[1])
        for item in range(len(s_data)):
            self.objects.append(Field(self.game, self.objects[0].rect, self.objects[1].rect, item + 1,
                                      self.objects[0].thickness, self.objects[1].thickness,
                                      Field.std_height * item))

    def process_logic(self):
        for item in self.objects[2:]:
            item.set_pos_y(-(self.objects[1].rect.y - self.objects[1].pos_y))
            item.process_logic()
            self.objects[1].process_logic()
