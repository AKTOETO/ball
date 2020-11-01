from random import randint

import pygame

from objects.ball import BallObject
from objects.text import TextObject
from scenes.base import BaseScene
from objects.platform import PlatformObject


class GameScene(BaseScene):
    max_collisions = 15
    balls_count = 1
    collision_tolerance = 4

    def __init__(self, game):
        super().__init__(game)
        self.platform = PlatformObject(game)
        self.balls = [BallObject(game) for _ in range(GameScene.balls_count)]
        self.collision_count = 0
        # self.status_text = TextObject(self.game, 0, 0, self.get_collisions_text(), (255, 255, 255))
        # self.status_text.move(10, 10)
        self.objects += self.balls
        # self.objects.append(self.status_text)
        self.objects.append(self.platform)
        self.reset_balls_position()

    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.set_scene(self.game.SCENE_MENU)
            elif event.key == pygame.K_a or event.key == pygame.K_d:
                self.platform.process_event(event)

    def get_random_position(self, radius):
        return randint(10, self.game.width - radius*2 - 10), randint(10, self.game.height - radius*2 - 10)

    def set_random_position(self, ball):
        pos = self.get_random_position(ball.radius)
        ball.move(*pos)

    def reset_balls_position(self):
        for ball in self.balls:
            ball.move(self.game.width, self.game.height)

    def set_random_unique_position(self):
        for index in range(len(self.balls)):
            other_rects = [self.balls[i].rect for i in range(len(self.balls)) if i != index]
            self.set_random_position(self.balls[index])
            while self.balls[index].rect.collidelist(other_rects) != -1:
                self.set_random_position(self.balls[index])

    def on_activate(self):
        self.collision_count = 0
        self.reset_balls_position()
        self.set_random_unique_position()
        # self.status_text.update_text(self.get_collisions_text())
        # self.status_text.move(10, 10)

    #def check_ball_intercollisions(self):
    #    for i in range(len(self.balls) - 1):
    #        for j in range(i + 1, len(self.balls)):
    #            if self.balls[i].collides_with(self.balls[j]):
    #                self.balls[i].bounce(self.balls[j])

    def collide_platform_with_ball(self):
        if self.platform.rect.colliderect(self.balls[0].rect):
            if abs(self.balls[0].rect.bottom - self.platform.rect.top) < GameScene.collision_tolerance and\
                    self.balls[0].speed[1] > 0:
                self.balls[0].speed[1] *= -1
            elif abs(self.balls[0].rect.left - self.platform.rect.right) < GameScene.collision_tolerance and\
                    self.balls[0].speed[0] < 0:
                self.balls[0].speed[0] *= -1
            elif abs(self.balls[0].rect.right - self.platform.rect.left) < GameScene.collision_tolerance and\
                    self.balls[0].speed[0] > 0:
                self.balls[0].speed[0] *= -1

    #def get_collisions_text(self):
    #    return 'Wall collisions: {}/{}'.format(self.collision_count, GameScene.max_collisions)

    #def check_ball_edge_collision(self):
    #    for ball in self.balls:
    #        if ball.edge_collision():
    #            self.collision_count += 1
    #            self.status_text.update_text(self.get_collisions_text())
    #            self.status_text.move(10, 10)

    def check_game_over(self):
        if self.balls[0].rect.bottom >= self.game.height:
            self.game.set_scene(self.game.SCENE_GAMEOVER)

    def process_logic(self):
        super().process_logic()
        self.collide_platform_with_ball()
        #self.check_ball_intercollisions()
        #self.check_ball_edge_collision()
        self.check_game_over()
