import pygame

class Boo(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super ().__init__ (*groups)
        self.width = 80
        self.height = 80
        self.initial_pos_x = 750
        self.initial_pos_y = 600
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/entities/boo/boo-semfundo-parado0000.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/entities/boo/boo-semfundo-parado0001.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/entities/boo/boo-semfundo-parado0002.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/entities/boo/boo-semfundo-parado0003.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/entities/boo/boo-semfundo-parado0004.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/entities/boo/boo-semfundo-parado0005.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/entities/boo/boo-semfundo-parado0006.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/entities/boo/boo-semfundo-parado0007.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/entities/boo/boo-semfundo-parado0008.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/entities/boo/boo-semfundo-parado0009.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/entities/boo/boo-semfundo-parado0010.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/entities/boo/boo-semfundo-parado0011.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/entities/boo/boo-semfundo-parado0012.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/entities/boo/boo-semfundo-parado0013.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/entities/boo/boo-semfundo-parado0014.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/entities/boo/boo-semfundo-parado0015.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/entities/boo/boo-semfundo-parado0016.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/entities/boo/boo-semfundo-parado0017.png').convert_alpha())
        self.current_sprite = 0
        self.current_sprite_speed = 0.1
        self.image_flipped = False
        self.rect = pygame.Rect(self.initial_pos_x, self.initial_pos_y,  self.width, self.height)
        self.destiny = 0
        self.image = pygame.transform.scale(pygame.transform.flip(self.sprites[self.current_sprite],
                                                                  self.image_flipped, False), [self.width, self.height])

    def update(self,):
        self.movement()
        self.image = pygame.transform.scale(pygame.transform.flip(self.sprites[self.current_sprite],
                                                                  self.image_flipped, False), [self.width, self.height])

    def movement(self):
        #Velocidade da mudanca de sprite
        self.current_sprite_speed += 0.1
        # Se a velocidade chegar a 1 inteiro, zere e mude para a próxima sprite
        if self.current_sprite_speed > 1:
            self.current_sprite_speed = 0
            self.current_sprite += 1
            # Se a atual sprite for maior ou igual a quantidade de sprites, volte a 0
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

