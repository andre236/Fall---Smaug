import pygame

class Boo(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super ().__init__ (*groups)
        self.width = 40
        self.height = 40
        self.initial_pos_x = 750
        self.initial_pos_y = 600
        self.image = pygame.image.load('sprites/entities/boo/boo.png')
        self.rect = pygame.Rect(self.initial_pos_x, self.initial_pos_y,  self.width, self.height)
        self.destiny = 0

    def update(self,):
        self.movement()

    def movement(self):
        while(self.initial_pos_x > self.destiny):
            self.rect.x -= 1
