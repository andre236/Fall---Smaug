import pygame

import main
from object import Object
from boo import Boo
from time import sleep
from scene import Scene
import sys

class Player(pygame.sprite.Sprite):
    # O que carregar do player quando iniciar:
    def __init__(self, *groups):
        super().__init__(*groups)
        # Size and Sprite
        self.width = 68
        self.height = 147
        self.sprites_walking = []
        self.sprites_jumping = []
        self.sprites_walking.append(pygame.image.load('sprites/entities/player/68 147/walking0.png').convert_alpha())
        self.sprites_walking.append(pygame.image.load('sprites/entities/player/68 147/walking1.png').convert_alpha())
        self.sprites_walking.append(pygame.image.load('sprites/entities/player/68 147/walking2.png').convert_alpha())
        self.sprites_walking.append(pygame.image.load('sprites/entities/player/68 147/walking3.png').convert_alpha())
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
        self.can_move_right = True
        self.can_move_left = True
        self.can_move = True
        self.moving = False
        self.initial_pos_x = 400
        self.initial_pos_y = 600
        self.movement_speed = 0
        self.movement_max_speed = 1
        self.movement_acceleration = 0.9
        self.blocking_right = False
        self.blocking_left = False

        # State Jumping
        self.gravity = 3
        self.current_height_ground = 0
        self.player_on_ground = False
        self.player_jumping = False
        self.number_jump = 1
        self.jump_force = 0 # Velocidade
        self.jump_peak = 8
        self.jump_acceleration = 0.2

        if self.state_animation == 'walking':
            self.image = pygame.transform.flip(self.sprites_walking[self.current_sprite_walking],
                                                                  self.image_flipped, False)
            self.image.fill((217, 15, 139))

        # Size box collider
        self.rect = pygame.rect.Rect(self.initial_pos_x, self.initial_pos_y, self.width, self.height)
        self.current_height_ground = 650

    def update(self, *args):
        if self.can_move == True:
            self.move_player()

        self.player_jump()



    def move_player(self):
        on_pressed_key = pygame.key.get_pressed()

        if on_pressed_key[pygame.K_RIGHT] and not on_pressed_key[pygame.K_LEFT]:
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

        elif on_pressed_key[pygame.K_LEFT] and not on_pressed_key[pygame.K_RIGHT]:
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

        if self.state_animation == 'walking':
            self.image = pygame.transform.flip(self.sprites_walking[self.current_sprite_walking],
                                                                  self.image_flipped, False)
        if self.state_animation == "jumping":
            self.image = pygame.transform.scale(pygame.transform.flip(self.sprites_jumping[self.current_sprite_jumping],
                                                                  self.image_flipped, False), [self.width, self.height])

    def player_jump(self):
        # Mudando a animacao para pulando
        if self.player_jumping:
            self.state_animation = "jumping"
        else:
            self.state_animation = "walking"

        on_pressed_key_space = pygame.key.get_pressed()[pygame.K_SPACE]


        # se apertou Espaço e não está pulando e tocando no chão
        if on_pressed_key_space and self.number_jump == 1:
            self.number_jump = 0
            self.player_jumping = True

        # Se não está na altura do chão e não está pulando
        if not self.rect.y >= self.current_height_ground and not self.player_jumping:
            self.rect.y += self.gravity

        # Se pulando, aplicar a força
        if self.player_jumping:
            self.rect.y -= self.jump_force
            self.jump_force += self.jump_acceleration
            if self.jump_force > self.jump_peak and self.player_jumping:
                self.player_jumping = False
                self.jump_force = 0


        # Se estiver no alto
        if self.rect.y < self.current_height_ground:
            self.player_on_ground = False
        elif self.rect.y >= self.current_height_ground:
            self.player_on_ground = True
            self.state_animation = 'walking'
            self.number_jump = 1

    def update_height_ground(self, current_height_ground):
        if not self.current_height_ground == 650:
            self.current_height_ground = current_height_ground
        else:
            self.current_height_ground = 650
