import pygame

class Player(pygame.sprite.Sprite):
    # O que carregar do player quando iniciar:
    def __init__(self, *groups):
        super().__init__(*groups)
        # Size and Sprite
        self.width = 68
        self.height = 147
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/entities/player/luca-walk0000.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/entities/player/luca-walk0001.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/entities/player/luca-walk0002.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/entities/player/luca-walk0003.png').convert_alpha())
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.image_flipped = False
        # Size box collider
        self.rect = pygame.Rect(400, 600, self.width, self.height)
        # State position
        self.movement_speed = 0
        self.movement_max_speed = 8
        self.movement_acceleration = 0.8
        # State Jumping
        self.player_jumping = False
        self.jump_force = 0
        self.jump_acceleration = 8
        self.jump_peak = 50

    def update(self, *args):
        self.move_player()
        self.player_jump()

        self.image = pygame.transform.scale(pygame.transform.flip(self.sprites[self.current_sprite],
                                                                      self.image_flipped, False), [self.width, self.height])

    def move_player(self):
        on_pressed_key = pygame.key.get_pressed()

        if on_pressed_key[pygame.K_RIGHT] or on_pressed_key[pygame.K_d]:
            self.image_flipped = False
            self.current_sprite += 1
            # Voltar para sprite 0
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

            self.rect.x += self.movement_speed
            self.movement_speed += self.movement_acceleration

            if self.movement_speed >= self.movement_max_speed:
                self.movement_speed = self.movement_max_speed

        elif on_pressed_key[pygame.K_LEFT] or on_pressed_key[pygame.K_a]:
            self.image_flipped = True
            self.current_sprite += 1
            # Voltar para sprite 0
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

            self.rect.x -= self.movement_speed
            self.movement_speed += self.movement_acceleration

            if self.movement_speed >= self.movement_max_speed:
                self.movement_speed = self.movement_max_speed

        else:
            self.movement_speed = 0

    def player_jump(self):
        on_pressed_key = pygame.key.get_pressed()

        if on_pressed_key[pygame.K_SPACE]:
            self.player_jumping = True
            # Se ta pulando
            if self.player_jumping:
                self.rect.y -= self.jump_force
                self.jump_force += self.jump_acceleration
                if self.jump_force >= self.jump_peak and self.player_jumping:
                    self.jump_force = self.jump_peak

