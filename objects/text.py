import pygame

from objects.base import DrawableObject


def main():
    pass


if __name__ == '__main__':
    main()


class TextObject(DrawableObject):
    def __init__(self, game, x, y, text, color):
        super().__init__(game)
        self.color = color
        self.y = y
        self.x = x
        self.font = pygame.font.SysFont('Comic Sans MS', 30, True)
        self.update_text(text)

    def update_text(self, text):
        self.text = text
        self.surface = self.font.render(self.text, True, self.color)

    def process_draw(self):
        self.game.screen.blit(self.surface, (self.x, self.y))