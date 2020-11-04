from constants import *
import pygame

from objects.basefortable import BaseElTable
from objects.field import Field


class ScrollBar(BaseElTable):
    def __init__(self, game, T_rect, T_thic):
        super().__init__(game)
        self.T_thic = T_thic
        self.T_rect = T_rect
        self.grap = False
        self.thickness = 3
        self.rect.width = 10
        self.rect.height = 40
        print('height:', self.rect.height, '1:', self.game.height, '2:', (len(self.game.fileul.data[1:]) * Field.std_height))

        self.pos_y = self.T_rect.y + T_thic // 2
        self.rect.x = self.T_rect.right - self.rect.width - T_thic // 2
        self.rect.y = self.T_rect.y + T_thic // 2

    def process_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.grap = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.grap = False

    def process_logic(self):
        self.check_cursor()
        if pygame.mouse.get_pressed() and self.grap and self.inner and \
                self.rect.y > self.T_rect.y + self.T_thic // 2 and \
                self.rect.y + self.rect.height < self.T_rect.y + self.T_rect.height:
            self.get_pos_cursor()
            self.rect.centery = self.pos[1]
        elif self.rect.y <= self.T_rect.y + self.T_thic // 2:
            self.rect.y = self.T_rect.y + self.T_thic // 2 + 1
        elif self.rect.y + self.rect.height >= self.T_rect.y + self.T_rect.height:
            self.rect.y = self.T_rect.y + self.T_rect.height - self.T_thic // 2 + 1 \
                          - self.rect.height

    def process_draw(self):
        pygame.draw.rect(self.game.screen, WHITE, self.rect, self.thickness)
