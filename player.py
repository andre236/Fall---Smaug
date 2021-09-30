import pygame

class Player(pygame.sprite.Sprite):
    # O que carregar do player quando iniciar:
    def __init__(self, *groups):
        super().__init__(*groups)
        # Size and Sprite
        self.width = 68
        self.height = 147
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/entities/player/luca-walk0000.png'))
        self.sprites.append(pygame.image.load('sprites/entities/player/luca-walk0001.png'))
        self.sprites.append(pygame.image.load('sprites/entities/player/luca-walk0002.png'))
        self.sprites.append(pygame.image.load('sprites/entities/player/luca-walk0003.png'))
        self.sprites.append(pygame.image.load('sprites/entities/player/luca-walk0004.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.image_flipped = False
        # Size box collider
        self.rect = pygame.Rect(400, 600, self.width, self.height)
        self.movement_speed = 5
        self.moving_left = False
        self.animation_moving = False

    def update(self, *args):
        on_pressed_key = pygame.key.get_pressed()

        if on_pressed_key[pygame.K_RIGHT] or on_pressed_key[pygame.K_d]:
            self.image_flipped = False
            self.animation_moving = True
            self.moving_left = False
            self.current_sprite += 1
            # Voltar para sprite 0
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
            self.rect.x += self.movement_speed


        if on_pressed_key[pygame.K_LEFT] or on_pressed_key[pygame.K_a]:
            self.image_flipped = True
            self.animation_moving = True
            self.moving_left = True
            self.current_sprite += 1
            # Voltar para sprite 0
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

            self.rect.x -= self.movement_speed

        self.image = pygame.transform.scale(self.sprites[self.current_sprite], [self.width, self.height])


