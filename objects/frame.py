from constants import ORANGE
from objects.base import DrawableObject
import pygame

from objects.scrollbar import ScrollBar


class Frame(DrawableObject):
    def __init__(self, game):
        super().__init__(game)
        self.objects = []
        self.thickness = 12
        self.rect.x = self.game.width // 4
        self.rect.y = self.game.height // 4
        self.rect.width = self.game.width - (2 * self.rect.x)
        self.rect.height = self.game.height - self.rect.y
        self.pos = (self.get_pos_cursor())
        self.objects.append(ScrollBar(game, self.rect, self.thickness))

    def get_pos_cursor(self):
        self.pos = pygame.mouse.get_pos()
        print(self.pos)

    def check_cursor(self):
        self.get_pos_cursor()
        if self.rect.x < self.pos[0] < self.rect.right and \
                self.rect.y < self.pos[1] < self.rect.bottom:
            print('inner')

    def process_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

    def process_logic(self):
        self.check_cursor()
        for object in self.objects:
            object.process_logic()

    def process_draw(self):
        pygame.draw.rect(self.game.screen, ORANGE, self.rect, self.thickness)
        for object in self.objects:
            object.process_draw()
