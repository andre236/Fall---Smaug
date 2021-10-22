import pygame

class Scene():
    def __init__(self):
        self.level = 1
        self.bg_level = pygame.image.load('images/bg/map02.png')
        self.bg_level = pygame.transform.scale(self.bg_level, [3840, 1080])
        self.bg_level_pos_x = 0
        self.bg_level_pos_y = 0
        self.bg_level_ground = 625
        self.bg_minimum_x = 400
        self.bg_maximum_x = 1600
        self.bg_level2 = pygame.image.load('images/bg/level2.png')
        self.bg_level2 = pygame.transform.scale(self.bg_level2, [1920, 1080])
        self.bg_level2_pos_x = 0
        self.bg_level2_pos_y = 0

