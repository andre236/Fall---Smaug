import pygame

class Player(pygame.sprite.Sprite):
    # O que carregar do player quando iniciar:
    def __init__(self, *groups):
        super().__init__(*groups)
        # Size and Sprite
        self.width = 68
        self.height = 147
        self.sprites_walking = []
        self.sprites_jumping = []
        self.sprites_walking.append(pygame.image.load('sprites/entities/player/luca-walk0000.png').convert_alpha())
        self.sprites_walking.append(pygame.image.load('sprites/entities/player/luca-walk0001.png').convert_alpha())
        self.sprites_walking.append(pygame.image.load('sprites/entities/player/luca-walk0002.png').convert_alpha())
        self.sprites_walking.append(pygame.image.load('sprites/entities/player/luca-walk0003.png').convert_alpha())
        self.sprites_jumping.append(pygame.image.load('sprites/entities/player/jumping/luca-jump-Frame 1.png').convert_alpha())
        self.sprites_jumping.append(pygame.image.load('sprites/entities/player/jumping/luca-jump-Frame 2.png').convert_alpha())
        self.sprites_jumping.append(pygame.image.load('sprites/entities/player/jumping/luca-jump-Frame 3.png').convert_alpha())
        self.sprites_jumping.append(pygame.image.load('sprites/entities/player/jumping/luca-jump-Frame 4.png').convert_alpha())
        self.sprites_jumping.append(pygame.image.load('sprites/entities/player/jumping/luca-jump-Frame 5.png').convert_alpha())
        self.sprites_jumping.append(pygame.image.load('sprites/entities/player/jumping/luca-jump-Frame 6.png').convert_alpha())
        # Current States
        self.state_animation = 'walking'
        # Sprites Walking
        self.current_sprite_walking = 0
        self.current_sprite_walking_speed = 0.0
        self.max_sprite_walking_speed = 1
        self.image = self.sprites_walking[self.current_sprite_walking]
        self.image_flipped = False
        # Sprites Jumping
        self.current_sprite_jumping = 0
        self.current_sprite_jump_speed = 0
        self.current_sprite_jump_acceleration = 0.05
        self.max_sprite_jumping_speed = 1

        # State position
        self.can_move = True
        self.moving = False
        self.initial_pos_x = 400
        self.initial_pos_y = 600
        self.movement_speed = 0
        self.movement_max_speed = 1
        self.movement_acceleration = 0.9
        # State Jumping
        self.gravity = 3
        self.player_on_ground = False
        self.player_jumping = False
        self.jump_force = 2 # Velocidade
        self.jump_peak = 7
        self.jump_acceleration = 0.2

        # Size box collider
        self.rect = pygame.Rect(self.initial_pos_x, self.initial_pos_y, self.width, self.height)
        self.new_rect_y = 0

    def update(self, *args):
        self.move_player()

        self.player_jump()

        if self.state_animation == 'walking':
            self.image = pygame.transform.scale(pygame.transform.flip(self.sprites_walking[self.current_sprite_walking],
                                                                  self.image_flipped, False), [self.width, self.height])
        if self.state_animation == "jumping":
            self.image = pygame.transform.scale(pygame.transform.flip(self.sprites_jumping[self.current_sprite_jumping],
                                                                  self.image_flipped, False), [self.width, self.height])


    def move_player(self):
        on_pressed_key = pygame.key.get_pressed()

        if on_pressed_key[pygame.K_RIGHT] or on_pressed_key[pygame.K_d]:
            self.moving = True
            self.image_flipped = False
            self.current_sprite_walking_speed += 0.1
            if self.current_sprite_walking_speed > 1:
                self.current_sprite_walking_speed = 0
                self.current_sprite_walking += 1

            # Voltar para sprite 0
            if self.current_sprite_walking >= len(self.sprites_walking):
                self.current_sprite_walking = 0

            self.rect.x += self.movement_speed
            self.movement_speed += self.movement_acceleration

            if self.movement_speed >= self.movement_max_speed:
                self.movement_speed = self.movement_max_speed

        elif on_pressed_key[pygame.K_LEFT] or on_pressed_key[pygame.K_a]:
            self.moving = True
            self.image_flipped = True
            self.current_sprite_walking_speed += 0.1
            if self.current_sprite_walking_speed > 1:
                self.current_sprite_walking_speed = 0
                self.current_sprite_walking += 1
            # Voltar para sprite 0
            if self.current_sprite_walking >= len(self.sprites_walking):
                self.current_sprite_walking = 0

            self.rect.x -= self.movement_speed
            self.movement_speed += self.movement_acceleration

            if self.movement_speed >= self.movement_max_speed:
                self.movement_speed = self.movement_max_speed

        else:
            self.movement_speed = 0
            self.moving = False
            self.current_sprite_walking = 0

    def player_jump(self):
        # Mudando a animacao para pulando
        if self.player_jumping:
            self.state_animation = "jumping"
        else:
            self.state_animation = "walking"

        on_pressed_key_space = pygame.key.get_pressed()[pygame.K_SPACE]
        height_ground = self.new_rect_y

        # se apertou Espaço e não está pulando e tocando no chão
        if on_pressed_key_space and not self.player_jumping and self.player_on_ground:
            self.player_jumping = True

        # Se estiver no alto
        if self.rect.y < height_ground:
            self.player_on_ground = False
        else:
            self.player_on_ground = True
            self.state_animation = 'walking'

        # Se tiver no alto e não está pulando apenas aplica a gravidade.
        if not self.player_on_ground and not self.player_jumping:
            self.current_sprite_jumping = 4
            self.rect.y += self.gravity

        # o Pulo
        if self.player_jumping:
            self.jump_force += self.jump_acceleration
            # Mudando a sprite do pulo com velocidade
            self.current_sprite_jump_speed += self.current_sprite_jump_acceleration
            if self.current_sprite_jump_speed >= self.max_sprite_jumping_speed:
                self.current_sprite_jump_speed = 0
                self.current_sprite_jumping += 1
            # Caso a index da sprite seja maior que a quantidade de sprites
            if self.current_sprite_jumping >= 3:
                self.current_sprite_jumping = 3

            # Controlando a força do pulo com pico
            if self.jump_force >= self.jump_peak:
                self.jump_force = self.jump_peak
                self.player_jumping = False

            self.rect.y -= self.jump_force
        else:
            self.jump_force = 0


