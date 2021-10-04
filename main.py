import pygame
from pygame.locals import*

import main
import player
from player import Player
from object import Object
import sys

#Inicializando os modulos do pygame
pygame.init()

#Configurações
font = pygame.font.SysFont('Montserrat', 48)
running_game = True
clock = pygame.time.Clock()

#Criando a janela do jogo
width = 1920
height = 1080
display_game = pygame.display.set_mode((width, height))
pygame.display.set_caption('Fall')

# Configurando o BGM
pygame.mixer.music.load('musics/bgm/mainmenu.ogg')
pygame.mixer.music.play(-1, 0.0)

#SFXs
selecting_sfx = pygame.mixer.Sound('musics/sfx/selecting.ogg')

#Keys temporarias
keys = pygame.key

#Group
draw_group = pygame.sprite.Group()

# Definindo Player
player = Player(draw_group)
player_rect = player.rect

#
call_started = 1

class GameState():
    main.call_started
    draw_group.empty()

    def __init__(self):
        self.state = 'menu_scene'

    def menu_scene(self):
        # Definindo BG
        background = pygame.image.load('images/misc/Menu.png')
        background = pygame.transform.scale(background, [1920, 1080])
        display_game.blit(background, [120, 0])

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
                    self.state = 'first_cutscene'
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


        pygame.mixer.music.stop()
        for alpha_scene_01 in range(0, 300):
            pygame.Surface.set_alpha(scene_01, alpha_scene_01)
            display_game.blit(scene_01, [0, 30])
            pygame.display.update()
            pygame.time.delay(5)

        for alpha in range(0 , 300):
            fade_to_black.set_alpha(alpha)
            display_game.blit(fade_to_black, [0,0])
            pygame.display.update()
            pygame.time.delay(5)

        for alpha_scene_02 in range(0, 300):
            pygame.Surface.set_alpha(scene_02, alpha_scene_02)
            display_game.blit(scene_02, [0, 30])
            pygame.display.update()
            pygame.time.delay(5)

        for alpha in range(0 , 300):
            fade_to_black.set_alpha(alpha)
            display_game.blit(fade_to_black, [0,0])
            pygame.display.update()
            pygame.time.delay(5)

        for alpha_scene_03 in range(0, 300):
            pygame.Surface.set_alpha(scene_03, alpha_scene_03)
            display_game.blit(scene_03, [0, 30])
            pygame.display.update()
            pygame.time.delay(5)

        for alpha in range(0 , 300):
            fade_to_black.set_alpha(alpha)
            display_game.blit(fade_to_black, [0,0])
            pygame.display.update()
            pygame.time.delay(5)

        for alpha_scene_04 in range(0, 300):
            pygame.Surface.set_alpha(scene_04, alpha_scene_04)
            display_game.blit(scene_04, [0, 30])
            pygame.display.update()
            pygame.time.delay(5)

        for alpha in range(0 , 298):
            fade_to_black.set_alpha(alpha)
            display_game.blit(fade_to_black, [0,0])
            pygame.display.update()
            pygame.time.delay(5)
            for alpha in range( 299, 300):
                self.state = 'level_01'


        def draw_game():
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
        # Definindo BG
        background_forest = pygame.image.load('images/bg/background1.png')
        background_forest = pygame.transform.scale(background_forest, [1920, 1080])
        display_game.blit(background_forest, [0, 30])
        pygame.mixer.music.fadeout(1000)
        # Definindo BGS

        def draw_initial():
            player = Player(draw_group)
            # box = Object(draw_group)

        def draw_game():
            draw_group.draw(display_game)



        for event in pygame.event.get():
            # condicional para sair do loop
            if event.type == pygame.QUIT or keys.get_pressed()[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()

            # atualizando os dados na tela
        if main.call_started == 1:
            main.call_started = 0
            draw_initial()


        player.update()
        draw_group.update()
        draw_game()
        pygame.display.update()



    def state_manager(self):
        if self.state == 'menu_scene':
            self.menu_scene()
        if self.state == 'first_cutscene':
            self.first_cutscene()
        if self.state == 'level_01':
            self.level_01()

# Estado do jogo
game_state = GameState()

# Loop do jogo
while running_game:
    game_state.state_manager()

#encerrando os modulos do pygame
pygame.quit()










