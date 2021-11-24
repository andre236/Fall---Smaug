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
        self.bg_level2 = pygame.transform.scale(self.bg_level2, [3840, 1080])
        self.bg_level2_pos_x = 0
        self.bg_level2_pos_y = 0
        self.bg_level2_ground = 625
        self.bg_level3 = pygame.image.load('images/bg/level3_reduzido.png')
        self.bg_level3 = pygame.transform.scale(self.bg_level3, [3840, 1080])
        self.bg_level3_pos_x = 0
        self.bg_level3_pos_y = -100
        self.bg_level3_ground = 725
        self.bg_level4 = pygame.image.load('images/bg/level4.png')
        self.bg_level4 = pygame.transform.scale(self.bg_level4, [3840, 1080])
        self.bg_level4_pos_x = 0
        self.bg_level4_pos_y = -200
        self.bg_level4_ground = 625
        self.bg_level5 = pygame.image.load('images/bg/level5.png')
        self.bg_level5 = pygame.transform.scale(self.bg_level5, [3840, 1080])
        self.bg_level5_pos_x = 0
        self.bg_level5_pos_y = -125
        self.bg_level5_ground = 625
        self.bg_level6 = pygame.image.load('images/bg/level6.png')
        self.bg_level6 = pygame.transform.scale(self.bg_level6, [3840, 1080])
        self.bg_level6_pos_x = 0
        self.bg_level6_pos_y = -175
        self.bg_level6_ground = 625