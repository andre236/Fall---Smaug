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
        # State position
        self.initial_pos_x = 400
        self.initial_pos_y = 550
        self.movement_speed = 0
        self.movement_max_speed = 10
        self.movement_acceleration = 0.9
        # State Jumping
        self.gravity = 18
        self.player_on_ground = False
        self.player_jumping = False
        self.jump_force = 5 # Velocidade
        self.jump_peak = 11
        self.jump_acceleration = 2.3

        # Size box collider
        self.rect = pygame.Rect(self.initial_pos_x, self.initial_pos_y, self.width, self.height)


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
        on_pressed_key_space = pygame.key.get_pressed()[pygame.K_SPACE]
        height_ground = 625

        if on_pressed_key_space and not self.player_jumping and self.player_on_ground:
            self.player_jumping = True

        # Se estiver no alto
        if self.rect.y < height_ground:
            self.player_on_ground = False
        else:
            self.player_on_ground = True

        if not self.player_on_ground and not self.player_jumping:
            self.rect.y += self.gravity

        # o Pulo
        if self.player_jumping:
            self.jump_force += self.jump_acceleration
            if self.jump_force >= self.jump_peak:
                self.jump_force = self.jump_peak
                self.player_jumping = False

            self.rect.y -= self.jump_force
        else:
            self.jump_force = 0


