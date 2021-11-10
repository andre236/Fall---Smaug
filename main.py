import pygame
from pygame.locals import *

import main
import player
from player import Player
from object import Object
from boo import Boo
from time import sleep
from scene import Scene
import sys

# Inicializando os modulos do pygame
pygame.init()

# Configurações
font = pygame.font.SysFont('Montserrat', 48)
running_game = True
clock = pygame.time.Clock()

# Criando a janela do jogo
width = 1920
height = 1080
display_game = pygame.display.set_mode((width, height))
pygame.display.set_caption('Fall')

# Configurando o BGM
pygame.mixer.music.load('musics/bgm/mainmenu.ogg')
pygame.mixer.music.play(-1, 0.0)

# SFXs
selecting_sfx = pygame.mixer.Sound('musics/sfx/selecting.ogg')

# Keys temporarias
keys = pygame.key

# Group
draw_group = pygame.sprite.Group()

# Definindo Player
player = Player(draw_group)
# Definindo Box
box = Object(draw_group)
boo = Boo(draw_group)
# Definindo os Levels
scene = Scene()

# Variables Global
call_started = 1
scroll_speed = 0
scroll_max_speed = 10
scroll_acceleration = 0.9
force = 0

# Condicao para passar cutscene
running_initial_cutscene = True

#
#caixa = pygame.draw.rect(display_game, (22,22,22), (700 + scroll_speed, 700, 80, 80))


class GameState():
    main.call_started
    main.running_initial_cutscene
    draw_group.empty()

    def __init__(self):
        bg_main_menu = pygame.image.load('images/misc/Menu.png')
        bg_main_menu = pygame.transform.scale(bg_main_menu, [1920, 1080])
        for alpha in range(0, 300):
            bg_main_menu.set_alpha(alpha)
            display_game.blit(bg_main_menu, [120, 0])
            pygame.display.update()
            pygame.time.delay(5)
        self.state = 'menu_scene'
        self.substate = 'level_01a'

    def menu_scene(self):
        black_color = (0, 0, 0)
        fade_to_black = pygame.Surface((1920, 1080))
        fade_to_black.fill((0, 0, 0))

        # Definindo BG
        bg_main_menu = pygame.image.load('images/misc/Menu.png')
        bg_main_menu = pygame.transform.scale(bg_main_menu, [1920, 1080])
        display_game.blit(bg_main_menu, [120, 0])

        # Criando os botoes de Menu
        start_button = pygame.sprite.Sprite(draw_group)
        options_button = pygame.sprite.Sprite(draw_group)
        quit_button = pygame.sprite.Sprite(draw_group)
        start_button.image = pygame.image.load('images/menu/start_button.png')
        options_button.image = pygame.image.load('images/menu/options_button.png')
        quit_button.image = pygame.image.load('images/menu/quit_button.png')
        start_button.rect = pygame.Rect(1150, 400, 384, 63)
        options_button.rect = pygame.Rect(1150, 475, 384, 63)
        quit_button.rect = pygame.Rect(1150, 550, 384, 63)

        def draw_game():
            draw_group.draw(display_game)

        def set_buttons_fuctions():
            mouse_position = pygame.mouse.get_pos()
            if start_button.rect.collidepoint(mouse_position):
                if pygame.mouse.get_pressed(3)[0] == 1:
                    draw_group.empty()
                    pygame.mixer.music.fadeout(1000)
                    self.state = 'first_cutscene'

                if pygame.mouse.get_pressed(3)[0] == 1 and keys.get_pressed()[pygame.K_c]:
                    draw_group.empty()
                    pygame.mixer.music.fadeout(1000)
                    self.state = 'level_01'

            if options_button.rect.collidepoint(mouse_position):
                if pygame.mouse.get_pressed(3)[0] == 1:
                    print("Abrir opcoes")
            if quit_button.rect.collidepoint(mouse_position):
                if pygame.mouse.get_pressed(3)[0] == 1:
                    pygame.quit()
                    sys.exit()

        # checando eventos
        for event in pygame.event.get():
            # condicional para sair do loop
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        set_buttons_fuctions()
        draw_game()

        # Esc para fechar o jogo.
        if keys.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        # atualizando os dados na tela
        pygame.display.update()

    def first_cutscene(self):
        draw_group.empty()
        # Definindo Fadein Black
        black_color = (0, 0, 0)
        fade_to_black = pygame.Surface((1920, 1080))
        fade_to_black.fill((0, 0, 0))
        # Definindo BG
        scene_01 = pygame.image.load('images/bg/Cena-enterro-real.png')
        scene_01 = pygame.transform.scale(scene_01, [1920, 1080])
        alpha_scene_01 = 0
        pygame.Surface.set_alpha(scene_01, alpha_scene_01)
        display_game.blit(scene_01, [0, 30])
        # Definindo BG 2
        scene_02 = pygame.image.load('images/bg/carro2.png')
        scene_02 = pygame.transform.scale(scene_02, [1920, 1080])
        alpha_scene_02 = 0
        pygame.Surface.set_alpha(scene_02, alpha_scene_02)
        display_game.blit(scene_02, [0, 30])
        # Definindo BG 3
        scene_03 = pygame.image.load('images/bg/casa.png')
        scene_03 = pygame.transform.scale(scene_03, [1920, 1080])
        alpha_scene_03 = 0
        pygame.Surface.set_alpha(scene_03, alpha_scene_03)
        display_game.blit(scene_03, [0, 30])
        # Definindo BG 4
        scene_04 = pygame.image.load('images/bg/quarto.png')
        scene_04 = pygame.transform.scale(scene_04, [1920, 1080])
        alpha_scene_04 = 0
        pygame.Surface.set_alpha(scene_04, alpha_scene_04)
        display_game.blit(scene_04, [0, 30])
        pygame.mixer.music.fadeout(1000)

        def draw_game():
            bgm_narration = pygame.mixer.music.load('musics/bgm/narracaomaisbgm.ogg')
            bgm_narration = pygame.mixer.music.play(1, 0.0)

            if keys.get_pressed()[pygame.K_SPACE] or keys.get_pressed()[pygame.K_KP_ENTER] or keys.get_pressed()[pygame.KSCAN_KP_ENTER]:
                print('fui chamado')
                main.running_initial_cutscene = False
                self.state = 'level_01'

            for alpha in range(0, 300):
                fade_to_black.set_alpha(alpha)
                display_game.blit(fade_to_black, [0, 0])
                pygame.display.update()
                pygame.time.delay(5)

            for alpha_scene_01 in range(0, 300):
                pygame.Surface.set_alpha(scene_01, alpha_scene_01)
                display_game.blit(scene_01, [0, 30])
                pygame.display.update()
                pygame.time.delay(5)

            for alpha in range(0, 300):
                fade_to_black.set_alpha(alpha)
                display_game.blit(fade_to_black, [0, 0])
                pygame.display.update()
                pygame.time.delay(5)

            for alpha_scene_02 in range(0, 300):
                pygame.Surface.set_alpha(scene_02, alpha_scene_02)
                display_game.blit(scene_02, [0, 30])
                pygame.display.update()
                pygame.time.delay(5)

            for alpha in range(0, 300):
                fade_to_black.set_alpha(alpha)
                display_game.blit(fade_to_black, [0, 0])
                pygame.display.update()
                pygame.time.delay(5)

            for alpha_scene_03 in range(0, 300):
                pygame.Surface.set_alpha(scene_03, alpha_scene_03)
                display_game.blit(scene_03, [0, 30])
                pygame.display.update()
                pygame.time.delay(5)

            for alpha in range(0, 300):
                fade_to_black.set_alpha(alpha)
                display_game.blit(fade_to_black, [0, 0])
                pygame.display.update()
                pygame.time.delay(5)

            for alpha_scene_04 in range(0, 300):
                pygame.Surface.set_alpha(scene_04, alpha_scene_04)
                display_game.blit(scene_04, [0, 30])
                pygame.display.update()
                pygame.time.delay(10)

            for alpha in range(0, 298):
                fade_to_black.set_alpha(alpha)
                display_game.blit(fade_to_black, [0, 0])
                pygame.display.update()
                pygame.time.delay(10)
                for alpha in range(299, 300):
                    self.state = 'level_01'

            draw_group.draw(display_game)

        for event in pygame.event.get():
            # condicional para sair do loop
            if event.type == pygame.QUIT or keys.get_pressed()[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()

        draw_game()
        # atualizando os dados na tela
        pygame.display.update()

    def level_01(self):
        if self.state == 'level_01':
            display_game.blit(scene.bg_level, [scene.bg_level_pos_x + scroll_speed, scene.bg_level_pos_y])
            # Rects para passagem de mapa
            level_01b = pygame.draw.rect(display_game, (0, 0, 0), (2500 + main.scroll_speed, 600, 68, 147))
            #box = pygame.draw.rect(display_game, (22, 22, 22), (700 + main.scroll_speed + main.force, 700, 80, 80))
            #hitbox_player = pygame.draw.rect(display_game, (123, 123,123), (player.rect.x, player.rect.y, player.rect.width, player.rect.height))


            # Definindo BGS
            def draw_initial():
                pygame.mixer.music.load('musics/bgs/forest2.ogg')
                pygame.mixer.music.play(-1, 0.0)
                game_state.state = 'level_01'

            def draw_game():
                draw_group.draw(display_game)
                display_game.blit(player.image, [player.rect.x, player.rect.y])
                #display_game.blit(box.image, [box.rect.x + scroll_speed + force, box.rect.y])
                display_game.blit(boo.image, [boo.rect.x + scroll_speed, boo.rect.y])

            for event in pygame.event.get():
                # condicional para sair do loop
                if event.type == pygame.QUIT or keys.get_pressed()[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

                # atualizando os dados na tela
            if main.call_started == 1:
                main.call_started = 0
                draw_initial()

            if pygame.Rect.colliderect(player.rect, box.rect):
                if(player.rect.x < box.rect.x and player.rect.y < 700 and box.rect.x < 2440):
                    main.force += 3
                if(player.rect.x > box.rect.x + 40 and player.rect.y < 700 and box.rect.x > 359):
                    main.force -= 3

            if pygame.Rect.colliderect(player.rect, level_01b):
                level_01b.width = 0
                level_01b.height = 0
                main.scroll_speed = 0
                main.call_started = 1
                game_state.state = 'level_02'

            # Effect scrolling Left
            if keys.get_pressed()[pygame.K_RIGHT] and player.rect.x > 500 and player.rect.x < 912:
                main.scroll_speed -= 1
            elif keys.get_pressed()[pygame.K_LEFT] and player.rect.x > 500 and player.rect.x < 912:
                main.scroll_speed += 1

            if keys.get_pressed()[pygame.K_RIGHT] and player.rect.x > 913 and player.rect.x < 1551:
                main.scroll_speed -= 1
                player.movement_speed = 0

            elif keys.get_pressed()[pygame.K_LEFT] and player.rect.x > 913 and player.rect.x < 1551:
                main.scroll_speed += 1
                player.movement_speed = 0

            # = pygame.draw.rect(display_game, (22,22,22), (player.rect.x, player.rect.y, player.rect.width, player.rect.height))

            box.update()
            player.update()
            draw_group.update()
            draw_game()
            pygame.display.update()
        else:
            pass

    def level_02(self):
        if self.state == 'level_02':
            display_game.blit(scene.bg_level2, [scene.bg_level_pos_x + scroll_speed, scene.bg_level_pos_y])
            # Rects para passagem de mapa
            #hitbox_player = pygame.draw.rect(display_game, (123, 123,123), (player.rect.x, player.rect.y, player.rect.width, player.rect.height))
            level_03 = pygame.draw.rect(display_game, (0, 0, 0), (2500 + main.scroll_speed, 600, 68, 147))

            # Definindo BGS
            def draw_initial():
                draw_group.empty()
                pygame.mixer.music.load('musics/bgs/forest2.ogg')
                pygame.mixer.music.play(-1, 0.0)
                game_state.state = 'level_02'
                player.rect.x = 650

            def draw_game():
                draw_group.draw(display_game)
                display_game.blit(player.image, [player.rect.x, player.rect.y])

            for event in pygame.event.get():
                # condicional para sair do loop
                if event.type == pygame.QUIT or keys.get_pressed()[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

            # atualizando os dados na tela
            if main.call_started == 1:
                main.call_started = 0
                draw_initial()

            # Effect scrolling Left
            if keys.get_pressed()[pygame.K_RIGHT] and player.rect.x > 500:
                main.scroll_speed -= 1
            elif keys.get_pressed()[pygame.K_LEFT] and player.rect.x > 500:
                main.scroll_speed += 1

            if keys.get_pressed()[pygame.K_RIGHT] and player.rect.x > 913:
                main.scroll_speed -= 1
                player.movement_speed = 0

            elif keys.get_pressed()[pygame.K_LEFT] and player.rect.x > 913 :
                main.scroll_speed += 1
                player.movement_speed = 0


            player.update()
            draw_group.update()
            draw_game()
            pygame.display.update()

        else:
            pass

    def state_manager(self):
        if self.state == 'menu_scene':
            self.menu_scene()
        if self.state == 'first_cutscene':
            self.first_cutscene()
        if self.state == 'level_01':
            self.level_01()
        if self.state == 'level_02':
            self.level_02()

# Estado do jogo
game_state = GameState()

# Loop do jogo
while running_game:
    game_state.state_manager()

# encerrando os modulos do pygame
pygame.quit()
