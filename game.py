import pygame

from constants import BLACK
from scenes.game import GameScene
from scenes.gameover import GameOverScene
from scenes.menu import MenuScene


class Game:
    size = width, height = 800, 600
    SCENE_MENU = 0
    SCENE_GAME = 1
    SCENE_GAMEOVER = 2
    current_scene_index = SCENE_MENU

    def __init__(self):
        self.fileul = None
        self.screen = pygame.display.set_mode(self.size)
        self.scenes = [
            MenuScene(self),
            GameScene(self),
            GameOverScene(self)
        ]
        self.game_over = False

    @staticmethod
    def exit_button_pressed(event):
        return event.type == pygame.QUIT

    @staticmethod
    def exit_hotkey_pressed(event):
        return event.type == pygame.KEYDOWN and event.mod & pygame.KMOD_CTRL and event.key == pygame.K_q

    def process_exit_events(self, event):
        if Game.exit_button_pressed(event) or Game.exit_hotkey_pressed(event):
            self.exit_game()

    def process_all_events(self):
        for event in pygame.event.get():
            self.process_exit_events(event)
            self.scenes[self.current_scene_index].process_event(event)

    def process_all_logic(self):
        self.scenes[self.current_scene_index].process_logic()

    def set_scene(self, index):
        self.scenes[self.current_scene_index].on_deactivate()
        self.current_scene_index = index
        self.scenes[self.current_scene_index].on_activate()

    def process_all_draw(self):
        self.screen.fill(BLACK)
        self.scenes[self.current_scene_index].process_draw()
        pygame.display.flip()

    def main_loop(self):
        while not self.game_over:
            self.process_all_events()
            self.process_all_logic()
            self.process_all_draw()
            pygame.time.wait(10)

    def exit_game(self):
        print('Bye bye')
        self.game_over = True
