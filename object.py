import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.width = 90
        self.height = 90
        self.initial_pos_x = 500
        self.initial_pos_y = 700
        self.image = pygame.image.load('sprites/objects/Box.png').convert_alpha()
        self.rect = pygame.Rect(self.initial_pos_x, self.initial_pos_y, self.width, self.height)
