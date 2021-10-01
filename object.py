import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.width = 140
        self.height = 140
        self.image = pygame.image.load('sprites/objects/Box.png').convert_alpha()
        self.rect = pygame.Rect(500, 620, self.width, self.height)

    def update(self, *args):
        self.image = pygame.transform.scale(self.image, [self.width, self.height])


