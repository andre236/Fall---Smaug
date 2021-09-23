import pygame

class Player(pygame.sprite.Sprite):
    #o que carregar do player quando iniciar:
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/entities/player/luca-walk0000.png').convert_alpha()
        self.imagesheet_runnning = [pygame.image.load('sprites/entities/player/luca-walk0000.png').convert_alpha(),
                                    pygame.image.load('sprites/entities/player/luca-walk0001.png').convert_alpha(),
                                    pygame.image.load('sprites/entities/player/luca-walk0002.png').convert_alpha(),
                                    pygame.image.load('sprites/entities/player/luca-walk0003.png').convert_alpha(),
                                    pygame.image.load('sprites/entities/player/luca-walk0004.png').convert_alpha(),
                                    pygame.image.load('sprites/entities/player/luca-walk0005.png').convert_alpha(),
                                    pygame.image.load('sprites/entities/player/luca-walk0006.png').convert_alpha(),
                                    pygame.image.load('sprites/entities/player/luca-walk0007.png').convert_alpha()]
        self.imagesheet_jumping = pygame.image.load('sprites/entities/player/luca-walk0001.png')
        self.rect = pygame.Rect(100, 100, 100, 100)
        self.mask = pygame.mask.from_surface(self.image)


    def update(self, *args):
        self.image = pygame.transform.scale(self.image, [100, 100])

    def jump(self,*args):
        pass

    def dead(self, *args):
        pass
