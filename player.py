import pygame

class Player(pygame.sprite.Sprite):
    #o que carregar do player quando iniciar:
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/entities/player/luca-walk0000t.png').convert_alpha()
        self.rect = pygame.Rect(420, 640, 100, 100)
        self.image = pygame.transform.scale(self.image, [200, 200])
        self.mask = pygame.mask.from_surface(self.image)

    #def update(self, *args):
        #def movement_player():
            #key = pygame.key.get_pressed()
            #if key[pygame.K_RIGHT]: