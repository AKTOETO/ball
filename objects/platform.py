import pygame
from random import *
from objects.image import ImageObject


class PlatformObject(ImageObject):
    filename = 'images/platform.png'
    image = pygame.image.load(filename)
    max_speed = 2

    def __init__(self, game, speed=None):
        super().__init__(game)
        self.rect.x = game.width // 2
        self.rect.y = game.height // 3 * 2.5
        self.radius = self.rect.width // 2
        self.direction = 1  # 1 right  -1 left
        self.speed = speed if speed else\
            randrange(PlatformObject.max_speed // 2, PlatformObject.max_speed)
        self.temp_speed = self.speed

    def process_event(self, event):
        if event.key == pygame.K_a:
            self.direction = -1
        elif event.key == pygame.K_d:
            self.direction = 1

    def step(self):
        self.rect.x += self.speed

    def process_logic(self):
        if self.rect.left <= 0 and self.direction == -1 or\
                self.rect.right >= self.game.width and self.direction == 1:
            self.speed = 0
        elif self.rect.left <= 0 and self.direction == 1:
            self.speed = self.temp_speed
        elif self.rect.right >= self.game.width and self.direction == -1:
            self.speed = -self.temp_speed
        elif self.rect.left > 0 and self.rect.right < self.game.width and self.direction == -1:
            self.speed = -self.temp_speed
        elif self.rect.left > 0 and self.rect.right < self.game.width and self.direction == 1:
            self.speed = self.temp_speed

        self.step()

