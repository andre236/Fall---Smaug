import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.width = 90
        self.height = 90
        self.image = pygame.image.load('sprites/objects/Box.png').convert_alpha()
        self.rect = pygame.Rect(500, 700, self.width, self.height)
        self.image = pygame.transform.scale(self.image, [self.width, self.height])
        self.move_speed_box = 0

    def update(self, *args):
        self.pushing(self.move_speed_box)

    def pushing(self, speed):
        self.rect.x += speed

