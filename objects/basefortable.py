from constants import ORANGE
from objects.base import DrawableObject
import pygame


class BaseElTable(DrawableObject):
    inaccuracy = 10

    def __init__(self, game):
        super().__init__(game)
        self.objects = []
        self.inner = False
        self.thickness = 0
        self.rect.x = 0
        self.rect.y = 0
        self.rect.width = 0
        self.rect.height = 0
        self.pos = (self.get_pos_cursor())

    def get_pos_cursor(self):
        self.pos = pygame.mouse.get_pos()

    def check_cursor(self):
        self.get_pos_cursor()
        if self.rect.x - BaseElTable.inaccuracy < self.pos[0] \
                < self.rect.right + BaseElTable.inaccuracy and \
                self.rect.y - BaseElTable.inaccuracy < self.pos[1] \
                < self.rect.bottom + BaseElTable.inaccuracy:
            self.inner = True
        else:
            self.inner = False

    def process_event(self, event):
        for object in self.objects:
            object.process_event(event)

    def process_logic(self):
        self.check_cursor()
        for object in self.objects:
            object.process_logic()

    def process_draw(self):
        for object in self.objects:
            object.process_draw()
