import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.width = 80
        self.height = 80
        self.initial_pos_x = 500
        self.initial_pos_y = 700
        self.image = pygame.image.load('sprites/objects/Box.png').convert_alpha()
        self.rect = pygame.Rect(self.initial_pos_x, self.initial_pos_y, self.width, self.height)


    def update(self):
        self.image = pygame.transform.scale(self.image, [self.width, self.height])
        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.width, self.height)
        #self.rect = pygame.Rect(self.rect.x + self.force, self.rect.y, 80, 80)
