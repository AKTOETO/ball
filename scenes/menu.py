from constants import RED, WHITE
from fileuploader import FileUploader
from objects.button import ButtonObject
from objects.text import TextObject
from scenes.base import BaseScene
from third_party.input_box.inputbox import InputBox


class MenuScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.next_state = False
        self.name = None
        self.game.fileul = FileUploader()
        self.objects.append(TextObject(self.game, self.game.width // 2,
                                       self.game.height // 2 - 145, "Enter your name:", WHITE))
        self.objects.append(InputBox(self.game, self.game.width // 2 - 100,
                                     self.game.height // 2 - 95 - 25, 200, 50, 'nick'))
        self.objects.append(
            ButtonObject(
                self.game, self.game.width // 2 - 100, self.game.height // 2 - 20 - 25, 200, 50,
                RED, self.start_game, text='Запуск игры'
            )
        )
        self.objects.append(
            ButtonObject(
                self.game, self.game.width // 2 - 100, self.game.height // 2 + 25, 200, 50,
                RED, self.game.exit_game, text='Выход'
            )
        )

    def process_logic(self):
        self.file_name()

    def file_name(self):
        if self.game.fileul.checking_for_name(self.objects[1].text):
            self.objects[0].update_text('Enter a different nickname:')
            self.next_state = False
        elif self.game.fileul.checking_for_name(self.objects[1].text) == 0:
            self.objects[0].update_text('Enter your name:')
            self.next_state = True

    def start_game(self):
        if self.next_state:
            self.game.set_scene(self.game.SCENE_GAME)
            self.game.fileul.set_name(f'{self.objects[1].text}')
