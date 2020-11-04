from datetime import datetime

from constants import RED
from objects.button import ButtonObject
from objects.frame import Frame
from objects.table import Table
from objects.text import TextObject
from scenes.base import BaseScene


class GameOverScene(BaseScene):
    text_format = 'Game over'

    def __init__(self, game):
        super().__init__(game)
        self.table = Table(game)
        self.gomenu = False
        self.objects.append(
            ButtonObject(
                self.game, self.game.width - 150, self.game.height - 100, 100, 50,
                RED, self.go_menu, text='MENU'
            )
        )
        self.text = TextObject(self.game, self.game.width // 2, self.game.height // 5, self.get_gameover_text_formatted(), (255, 255, 255))
        self.objects.append(self.text)
        self.objects.append(self.table)

    def on_activate(self):
        self.gomenu = False

    def process_logic(self):
        super().process_logic()
        if self.gomenu:
            self.game.set_scene(self.game.SCENE_MENU)

    def go_menu(self):
        self.gomenu = True
        pass

    def get_gameover_text_formatted(self):
        return GameOverScene.text_format
