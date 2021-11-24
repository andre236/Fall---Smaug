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
# Primeiro diálogo
white = (255,255,255)
dialogue = False
text_number_one = font.render("1", False, white)
text_number_two = font.render("2", False, white)
text_number_three = font.render("3", False, white)

texts_dialogue_firstscene = []
current_text_dialogue_firstscene = 0
texts_dialogue_firstscene.append(font.render("Lucca: Quem é você?", False, white))
texts_dialogue_firstscene.append(font.render("Boo: Boo... Boo...", False , white))
texts_dialogue_firstscene.append(font.render("Lucca: Boo ? Que tipo de língua é essa?", False , white))
texts_dialogue_firstscene.append(font.render("Boo: Boo.", False , white))
texts_dialogue_firstscene.append(font.render("Lucca: Ok, então vou te chamar de Boo.", False , white))
# Dialogo do level 2
texts_dialogue_butterflyscene = []
current_text_dialogue_butterflyscene = 0
texts_dialogue_butterflyscene.append(font.render("* Quer reviver alguém? Procure-me! Trickster * ", False, white))
texts_dialogue_butterflyscene.append(font.render("Lucca: Preciso achar esse Trickster logo!", False, white))
texts_dialogue_butterflyscene.append(font.render("Boo: Se eu fosse você, não acreditaria nesse tal de Trickster.", False, white))
texts_dialogue_butterflyscene.append(font.render("Lucca: Ah mas o papel diz... pera ai, VOCÊ FALA???", False, white))
texts_dialogue_butterflyscene.append(font.render("Boo: Claro que eu falo, poxa", False, white))
texts_dialogue_butterflyscene.append(font.render("Lucca: Então porque estava repetindo Boo, Boo?", False, white))
texts_dialogue_butterflyscene.append(font.render("Boo: Achei que você era um Oblis pregando alguma peça em mim.", False, white))
texts_dialogue_butterflyscene.append(font.render("Lucca: Oblis? O que são Oblis?", False, white))
texts_dialogue_butterflyscene.append(font.render("Boo: Ora hmmm, é complicado explicar, são coisas ruins e brincalhonas.", False, white))
texts_dialogue_butterflyscene.append(font.render("Lucca: E o que é você?", False, white))
texts_dialogue_butterflyscene.append(font.render("Boo: Eu sou Boo.", False, white))
texts_dialogue_butterflyscene.append(font.render("Lucca: Não, não. O que é você, não QUEM é você", False, white))
texts_dialogue_butterflyscene.append(font.render("Boo: Hmmmm, eu sou muitas coisas, mas você pode me chamar de Boo.", False, white))
texts_dialogue_butterflyscene.append(font.render("Lucca: Ahhh, ok. Ta mas porque você ta me seguindo?", False, white))
texts_dialogue_butterflyscene.append(font.render("Boo: Eu não sei, só estou te seguindo.", False, white))
texts_dialogue_butterflyscene.append(font.render("Lucca: Ah tanto faz então, vou seguir no meu objetivo, ta bom?", False, white))
# Dialogo level 3
dialogue_onlevel3 = False
texts_dialogue_level3 = []
current_text_dialogue_level3 = 0
texts_dialogue_level3.append(font.render("Boo: Qual seu nome? Estamos andando tanto tempo", False, white))
texts_dialogue_level3.append(font.render("Boo: E não perguntei seu nome.", False, white))
texts_dialogue_level3.append(font.render("Lucca: É Lucca.", False, white))
texts_dialogue_level3.append(font.render("Boo: Lucca... Não deve acreditar nessa carta desse jeito...", False, white))
texts_dialogue_level3.append(font.render("Lucca: Você não entende, Boo. Eu sinto que vai dar certo!", False, white))
texts_dialogue_level3.append(font.render("Lucca: Vou trazer minha mãe devolta e todo mundo vai me agradecer.", False, white))
texts_dialogue_level3.append(font.render("Lucca: Nós vamos poder voltar para casa e esquecer isso tudo...", False, white))
texts_dialogue_level3.append(font.render("Boo: Lucca...", False, white))
texts_dialogue_level3.append(font.render("Lucca: Mesmo você não me ajudando, eu deixo você vir com a gente.", False, white))
texts_dialogue_level3.append(font.render("Boo: ...", False, white))

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
# Definindo as boxs do puzzle
box_time = Object(draw_group)
box_time.image = pygame.image.load('sprites/objects/box_time.png')
box_time.width = 80
box_time.height = 80
time_symbol = Object(draw_group)
time_symbol.image = pygame.image.load('sprites/objects/time_symbol.png')
time_symbol.width = 40
time_symbol.height = 40
box_love = Object(draw_group)
box_love.image = pygame.image.load('sprites/objects/box_love.png')
box_love.width = 80
box_love.height = 80
love_symbol = Object(draw_group)
love_symbol.image = pygame.image.load('sprites/objects/love_symbol.png')
love_symbol.width = 40
love_symbol.height = 40
box_death = Object(draw_group)
box_death.image = pygame.image.load('sprites/objects/box_death.png')
box_death.width = 80
box_death.height = 80
death_symbol = Object(draw_group)
death_symbol.image = pygame.image.load('sprites/objects/death_symbol.png')
death_symbol.width = 40
death_symbol.height = 40

box_death_love_time_solved = False

# Definindo Boo
boo = Boo(draw_group)
# Carta
butterfly = Object(draw_group)
butterfly.image = pygame.image.load('sprites/entities/butterfly/butterfly_frame_1.png')
butterfly.width = 20
butterfly.height = 20
butterfly_alive = True
# Portal
portal = Object(draw_group)
portal.image = pygame.image.load('sprites/objects/portal.png')
portal.width = 68
portal.height = 147

# Definindo os Levels
scene = Scene()

# Variables Global
call_started = 1
scroll_display_x = 0
scroll_display_y = 0
scroll_speed_y = 2
scroll_speed_x = 2
blocking_player_right = False
blocking_player_left = False
cutscene_onlevel = False
scroll_max_speed = 10
scroll_acceleration = 0.9
force_box = 0
force_box_time = 0
force_box_death = 0
force_box_love = 0
boo_distance_x = 1300

# Condicao para passar cutscene
running_initial_cutscene = True

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

                if pygame.mouse.get_pressed(3)[0] == 1 and keys.get_pressed()[pygame.K_2]:
                    draw_group.empty()
                    pygame.mixer.music.fadeout(1000)
                    self.state = 'level_02'

                if pygame.mouse.get_pressed(3)[0] == 1 and keys.get_pressed()[pygame.K_3]:
                    draw_group.empty()
                    pygame.mixer.music.fadeout(1000)
                    self.state = 'level_03'

                if pygame.mouse.get_pressed(3)[0] == 1 and keys.get_pressed()[pygame.K_4]:
                    draw_group.empty()
                    pygame.mixer.music.fadeout(1000)
                    self.state = 'level_04'

                if pygame.mouse.get_pressed(3)[0] == 1 and keys.get_pressed()[pygame.K_5]:
                    draw_group.empty()
                    pygame.mixer.music.fadeout(1000)
                    self.state = 'level_05'

                if pygame.mouse.get_pressed(3)[0] == 1 and keys.get_pressed()[pygame.K_6]:
                    draw_group.empty()
                    pygame.mixer.music.fadeout(1000)
                    self.state = 'level_06'

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
            display_game.blit(scene.bg_level, [scene.bg_level_pos_x + main.scroll_display_x, scene.bg_level_pos_y + main.scroll_display_y])
            # Rects para passagem de mapa
            level_01b = pygame.draw.rect(display_game, (0, 0, 0), (2500 + main.scroll_display_x, 600 + main.scroll_display_y, 68, 147))
            #hitbox_player = pygame.draw.rect(display_game, (123, 123,123), (player.rect.x, player.rect.y, player.rect.width, player.rect.height))

            # Definindo BGS
            def draw_initial():
                pygame.mixer.music.load('musics/bgs/forest2.ogg')
                pygame.mixer.music.play(-1, 0.0)
                game_state.state = 'level_01'
                player.rect.x = 925

            def draw_game():
                draw_group.draw(display_game)
                display_game.blit(player.image, [player.rect.x, player.rect.y])
                display_game.blit(boo.image, [player.rect.x + main.boo_distance_x, player.rect.y - 15])
                if main.boo_distance_x > 30:
                    main.cutscene_onlevel = True
                    main.boo_distance_x -= 2
                else:
                    #
                    if main.cutscene_onlevel:
                        display_game.blit(main.texts_dialogue_firstscene[main.current_text_dialogue_firstscene], [960 - (main.texts_dialogue_firstscene[main.current_text_dialogue_firstscene].get_rect().width / 2), 900])
                    # Passar diálogo
                    if keys.get_pressed()[pygame.K_z] and main.cutscene_onlevel and main.current_text_dialogue_firstscene< len(main.texts_dialogue_firstscene):
                        pygame.time.delay(1000)
                        main.current_text_dialogue_firstscene += 1
                        if main.current_text_dialogue_firstscene >= len(main.texts_dialogue_firstscene):
                            main.current_text_dialogue_firstscene = len(main.texts_dialogue_firstscene) - 1
                            main.cutscene_onlevel = False

            for event in pygame.event.get():
                # condicional para sair do loop
                if event.type == pygame.QUIT or keys.get_pressed()[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

            # atualizando os dados na tela
            if main.call_started == 1:
                main.call_started = 0
                draw_initial()

            if pygame.Rect.colliderect(player.rect, level_01b):
                level_01b.width = 0
                level_01b.height = 0
                main.scroll_display_x = 0
                main.call_started = 1
                game_state.state = 'level_02'

            if main.scroll_display_x > 165:
                main.blocking_player_left = True
            else:
                main.blocking_player_left = False

            if main.scroll_display_x < -2086:
                main.blocking_player_right = True
            else:
                main.blocking_player_right = False

            # Effect scrolling Left
            if keys.get_pressed()[pygame.K_RIGHT] and not main.blocking_player_right and not main.cutscene_onlevel:
                main.scroll_display_x -= main.scroll_speed_x
            elif keys.get_pressed()[pygame.K_LEFT] and not main.blocking_player_left and not main.cutscene_onlevel:
                main.scroll_display_x += main.scroll_speed_x


            boo.update()
            player.update()
            draw_group.update()
            draw_game()
            pygame.display.update()
        else:
            pass

    def level_02(self):
        if self.state == 'level_02':
            display_game.blit(scene.bg_level2, [scene.bg_level2_pos_x + main.scroll_display_x, scene.bg_level2_pos_y])
            # Rects para passagem de mapa
            #hitbox_player = pygame.draw.rect(display_game, (123,123,123), (player.rect.x, player.rect.y, player.rect.width, player.rect.height))
            hitbox_box = pygame.draw.rect(display_game, (123, 123,123), (box.rect.x + main.scroll_display_x + main.force_box, box.rect.y, box.rect.width, box.rect.height))
            portal_level_03 = pygame.draw.rect(display_game, (0, 0, 0), (2620 + main.scroll_display_x, 265, 34, 77))
            plataform = pygame.draw.rect(display_game, (0 , 0, 0), ( 1600 + main.scroll_display_x, 520, 147, 80))
            plataform2 = pygame.draw.rect(display_game, (0 , 0, 0), ( 2000 + main.scroll_display_x, 450, 147, 80))
            plataform3 = pygame.draw.rect(display_game, (0 , 0, 0), ( 2400 + main.scroll_display_x, 380, 147, 80))


            # Definindo BGS
            def draw_initial():
                draw_group.empty()
                pygame.mixer.music.load('musics/bgs/forest2.ogg')
                pygame.mixer.music.play(-1, 0.0)
                player.rect.x = 925
                box.rect.x = 1200
                box.rect.y = 700
                butterfly.rect.x = 2430
                butterfly.rect.y = 340
                portal.rect.x = 2600
                portal.rect.y = 250
                player.current_height_ground = 625

            def draw_game():
                draw_group.draw(display_game)
                display_game.blit(player.image, [player.rect.x, player.rect.y])
                display_game.blit(box.image, [box.rect.x + main.scroll_display_x + main.force_box, box.rect.y])
                display_game.blit(portal.image, [portal.rect.x + main.scroll_display_x, portal.rect.y])
                if main.butterfly_alive:
                    display_game.blit(butterfly.image, [butterfly.rect.x + main.scroll_display_x, butterfly.rect.y])
                if not player.image_flipped:
                    display_game.blit(boo.image, [player.rect.x - 25, player.rect.y])
                else:
                    display_game.blit(boo.image, [player.rect.x + 20, player.rect.y])

            if pygame.Rect.colliderect(player.rect, portal_level_03):
                main.scroll_display_x = 0
                main.call_started = 1
                game_state.state = 'level_03'

            if main.cutscene_onlevel and not main.butterfly_alive:
                display_game.blit(main.texts_dialogue_butterflyscene[main.current_text_dialogue_butterflyscene], [960 - (main.texts_dialogue_butterflyscene[main.current_text_dialogue_butterflyscene].get_rect().width / 2), 900])
                    # Passar diálogo
                if keys.get_pressed()[pygame.K_z] and main.cutscene_onlevel and main.current_text_dialogue_butterflyscene < len(main.texts_dialogue_butterflyscene):
                    pygame.time.delay(1000)
                    main.current_text_dialogue_butterflyscene += 1
                    if main.current_text_dialogue_butterflyscene >= len(main.texts_dialogue_butterflyscene):
                        main.current_text_dialogue_butterflyscene = len(main.texts_dialogue_butterflyscene) - 1
                        main.cutscene_onlevel = False

            # empurrando a Caixa
            if pygame.Rect.colliderect(player.rect, hitbox_box):
                if player.rect.x > hitbox_box.x:
                    main.force_box -= 2
                if player.rect.x < hitbox_box.x + (hitbox_box.w/2):
                    main.force_box += 2



            # Poder ficar em cima da caixa
            if  player.rect.x > (hitbox_box.x - 70) and player.rect.x < (hitbox_box.x + 70):
                player.current_height_ground = box.rect.y - 150
            else:
                player.current_height_ground = 650

            # Se o rect X dp player está entre o x da plataforma
            if player.rect.x >= (plataform.x - (plataform.width/2)) and player.rect.x < plataform.x + plataform.width + 10 and (player.rect.y + player.rect.height) < plataform.y:
                player.current_height_ground = plataform.y - 150

            if player.rect.x >= (plataform2.x - (plataform2.width/2)) and player.rect.x < plataform2.x + plataform2.width + 10 and (player.rect.y + player.rect.height) < plataform2.y:
                player.current_height_ground = plataform2.y - 150

            if player.rect.x >= (plataform3.x - (plataform3.width/2)) and player.rect.x < plataform3.x + plataform3.width + 10 and (player.rect.y + player.rect.height) < plataform3.y:
                player.current_height_ground = plataform3.y - 150
                if main.butterfly_alive:
                    main.butterfly_alive = False
                    main.cutscene_onlevel = True

            for event in pygame.event.get():
                # condicional para sair do loop
                if event.type == pygame.QUIT or keys.get_pressed()[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

            # Atualizando os dados na tela
            if main.call_started == 1:
                main.call_started = 0
                draw_initial()

            # Effect scrolling Left
            if keys.get_pressed()[pygame.K_RIGHT] and not main.blocking_player_right and not main.cutscene_onlevel:
                main.scroll_display_x -= main.scroll_speed_x
            elif keys.get_pressed()[pygame.K_LEFT] and not main.blocking_player_left and not main.cutscene_onlevel:
                main.scroll_display_x += main.scroll_speed_x


            # Limitando o espaço do level
            if main.scroll_display_x > 165:
                main.blocking_player_left = True
            else:
                main.blocking_player_left = False

            if main.scroll_display_x < -2686:
                main.blocking_player_right = True
            else:
                main.blocking_player_right = False


            box.update()
            boo.update()
            portal.update()
            butterfly.update()
            player.update()
            draw_group.update()
            draw_game()
            pygame.display.update()

        else:
            pass

    def level_03(self):
        if self.state == 'level_03':
            display_game.blit(scene.bg_level3, [scene.bg_level3_pos_x + main.scroll_display_x, scene.bg_level3_pos_y])
            # Rects para passagem de mapa
            #hitbox_player = pygame.draw.rect(display_game, (123, 123,123), (player.rect.x, player.rect.y, player.rect.width, player.rect.height))

            # Definindo BGS
            def draw_initial():
                pygame.mixer.music.load('musics/bgs/forest2.ogg')
                pygame.mixer.music.play(-1, 0.0)
                player.rect.x = 925
                box.rect.x = 1200
                box.rect.y = 700
                main.dialogue_onlevel3 = True

            def draw_game():
                draw_group.draw(display_game)
                display_game.blit(player.image, [player.rect.x, player.rect.y])
                if not player.image_flipped:
                    display_game.blit(boo.image, [player.rect.x - 25, player.rect.y])
                else:
                    display_game.blit(boo.image, [player.rect.x + 20, player.rect.y])

                if dialogue_onlevel3:
                    display_game.blit(main.texts_dialogue_level3[main.current_text_dialogue_level3], [960 - (main.texts_dialogue_level3[main.current_text_dialogue_level3].get_rect().width / 2), 900])
                    # Passar diálogo
                if keys.get_pressed()[pygame.K_z] and main.dialogue_onlevel3 and main.current_text_dialogue_level3 < len(main.texts_dialogue_level3):
                    pygame.time.delay(1000)
                    main.current_text_dialogue_level3 += 1
                    if main.current_text_dialogue_level3 >= len(main.texts_dialogue_level3):
                        main.current_text_dialogue_level3 = len(main.texts_dialogue_level3) - 1
                        main.dialogue_onlevel3 = False



            for event in pygame.event.get():
                # condicional para sair do loop
                if event.type == pygame.QUIT or keys.get_pressed()[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

                # atualizando os dados na tela
            if main.call_started == 1:
                main.call_started = 0
                draw_initial()

            if main.scroll_display_x > 165:
                main.blocking_player_left = True
            else:
                main.blocking_player_left = False

            if main.scroll_display_x < -4000:
                main.blocking_player_right = True
            else:
                main.blocking_player_right = False

            # Effect scrolling Left
            if keys.get_pressed()[pygame.K_RIGHT] and not main.blocking_player_right and not main.cutscene_onlevel:
                main.scroll_display_x -= main.scroll_speed_x
            elif keys.get_pressed()[pygame.K_LEFT] and not main.blocking_player_left and not main.cutscene_onlevel:
                main.scroll_display_x += main.scroll_speed_x

            boo.update()
            butterfly.update()
            player.update()
            draw_group.update()
            draw_game()
            pygame.display.update()
        else:
            pass

    def level_04(self):
        if self.state == 'level_04':
            display_game.blit(scene.bg_level4, [scene.bg_level4_pos_x + main.scroll_display_x, scene.bg_level4_pos_y])
            # Rects para passagem de mapa
            #level_01b = pygame.draw.rect(display_game, (0, 0, 0), (2600 + main.scroll_display_x, 600, 68, 147))
            hitbox_box_time = pygame.draw.rect(display_game, (123, 123,123), (box_time.rect.x + main.scroll_display_x + main.force_box_time, box_time.rect.y, box_time.rect.width, box_time.rect.height))
            hitbox_box_love = pygame.draw.rect(display_game, (123, 123,123),(box_love.rect.x + main.scroll_display_x + main.force_box_love, box_love.rect.y, box_love.rect.width, box_love.rect.height))
            hitbox_box_death  = pygame.draw.rect(display_game, (123,123,123), (box_death.rect.x + main.scroll_display_x + main.force_box_death, box_death.rect.y, box_death.width, box_death.rect.height))

            #hitbox_player = pygame.draw.rect(display_game, (123, 123,123), (player.rect.x, player.rect.y, player.rect.width, player.rect.height))

            # Definindo BGS
            def draw_initial():
                pygame.mixer.music.load('musics/bgs/forest2.ogg')
                pygame.mixer.music.play(-1, 0.0)
                player.rect.x = 925
                box_death.rect.x = 1500
                box_death.rect.y = 700
                box_love.rect.x = 1780
                box_love.rect.y = 700
                box_time.rect.x = 1980
                box_time.rect.y = 700
                love_symbol.rect.y = 820
                love_symbol.rect.x = 2000
                death_symbol.rect.y = 820
                death_symbol.rect.x = 2600
                time_symbol.rect.y = 820
                time_symbol.rect.x = 2300
                portal.rect.x = 2890
                portal.rect.y = 600

            def draw_game():
                draw_group.draw(display_game)
                display_game.blit(player.image, [player.rect.x, player.rect.y])
                display_game.blit(box_time.image, [box_time.rect.x + main.scroll_display_x + main.force_box_time, box_time.rect.y])
                display_game.blit(box_death.image, [box_death.rect.x + main.scroll_display_x + main.force_box_death, box_death.rect.y])
                display_game.blit(box_love.image, [box_love.rect.x + main.scroll_display_x + main.force_box_love, box_love.rect.y])
                display_game.blit(love_symbol.image, [love_symbol.rect.x + main.scroll_display_x, love_symbol.rect.y])
                display_game.blit(time_symbol.image, [time_symbol.rect.x + main.scroll_display_x, time_symbol.rect.y])
                display_game.blit(death_symbol.image, [death_symbol.rect.x + main.scroll_display_x, death_symbol.rect.y])
                if main.box_death_love_time_solved:
                    display_game.blit(portal.image, [portal.rect.x + main.scroll_display_x, portal.rect.y])
                if not player.image_flipped:
                    display_game.blit(boo.image, [player.rect.x - 25, player.rect.y])
                else:
                    display_game.blit(boo.image, [player.rect.x + 20, player.rect.y])


            for event in pygame.event.get():
                # condicional para sair do loop
                if event.type == pygame.QUIT or keys.get_pressed()[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

                # atualizando os dados na tela
            if main.call_started == 1:
                main.call_started = 0
                draw_initial()

            #
            if pygame.Rect.colliderect(player.rect, hitbox_box_death):
                if player.rect.x > hitbox_box_death.x and not main.force_box_death >= 1080:
                    main.force_box_death -= 2
                if player.rect.x < hitbox_box_death.x + (hitbox_box_death.w/2) and not main.force_box_death >= 1080:
                    main.force_box_death += 2

            if pygame.Rect.colliderect(player.rect, hitbox_box_time):
                if player.rect.x < hitbox_box_time.x  and hitbox_box_time.x < 2600 and not main.force_box_time >= 300:
                    main.force_box_time += 2
                if player.rect.x < hitbox_box_time.x + (hitbox_box_time.w/2) and not main.force_box_time >= 300:
                    main.force_box_time += 2

            if pygame.Rect.colliderect(player.rect, hitbox_box_love):
                if player.rect.x > hitbox_box_love.x and not main.force_box_love >= 202:
                    main.force_box_love -= 2
                if player.rect.x < hitbox_box_love.x + (hitbox_box_love.w/2) and not main.force_box_love >= 202:
                    main.force_box_love += 2

            if main.force_box_love >= 202 and main.force_box_time >= 300 and main.force_box_death >= 1080:
                main.box_death_love_time_solved = True

            if main.scroll_display_x <= -1938 and main.box_death_love_time_solved:
                main.scroll_display_x = 0
                main.call_started = 1
                game_state.state = 'level_05'

            # if main.box_death_love_time_solved:
            # if pygame.Rect.colliderect(player.rect, portal_level_05):


            if main.scroll_display_x > 165:
                main.blocking_player_left = True
            else:
                main.blocking_player_left = False

            if main.scroll_display_x < -2086:
                main.blocking_player_right = True
            else:
                main.blocking_player_right = False

            # Effect scrolling Left
            if keys.get_pressed()[pygame.K_RIGHT] and not main.blocking_player_right and not main.cutscene_onlevel:
                main.scroll_display_x -= main.scroll_speed_x
            elif keys.get_pressed()[pygame.K_LEFT] and not main.blocking_player_left and not main.cutscene_onlevel:
                main.scroll_display_x += main.scroll_speed_x

            box_death.update()
            box_time.update()
            box_love.update()
            portal.update()
            death_symbol.update()
            time_symbol.update()
            love_symbol.update()
            boo.update()
            player.update()
            draw_group.update()
            draw_game()
            pygame.display.update()
        else:
            pass

    def level_05(self):
        if self.state == 'level_05':
            display_game.blit(scene.bg_level5, [scene.bg_level5_pos_x + main.scroll_display_x, scene.bg_level5_pos_y])
            # Rects para passagem de mapa
            level_01b = pygame.draw.rect(display_game, (0, 0, 0), (2500 + main.scroll_display_x, 600, 68, 147))
            #hitbox_player = pygame.draw.rect(display_game, (123, 123,123), (player.rect.x, player.rect.y, player.rect.width, player.rect.height))

            # Definindo BGS
            def draw_initial():
                pygame.mixer.music.load('musics/bgs/forest2.ogg')
                pygame.mixer.music.play(-1, 0.0)
                player.rect.x = 925

            def draw_game():
                draw_group.draw(display_game)
                display_game.blit(player.image, [player.rect.x, player.rect.y])
                display_game.blit(boo.image, [player.rect.x + main.boo_distance_x, player.rect.y - 15])


            for event in pygame.event.get():
                # condicional para sair do loop
                if event.type == pygame.QUIT or keys.get_pressed()[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

                # atualizando os dados na tela
            if main.call_started == 1:
                main.call_started = 0
                draw_initial()

            if pygame.Rect.colliderect(player.rect, level_01b):
                level_01b.width = 0
                level_01b.height = 0
                main.scroll_display_x = 0
                main.call_started = 1
                game_state.state = 'level_05'

            if main.scroll_display_x > 165:
                main.blocking_player_left = True
            else:
                main.blocking_player_left = False

            if main.scroll_display_x < -2086:
                main.blocking_player_right = True
            else:
                main.blocking_player_right = False

            # Effect scrolling Left
            if keys.get_pressed()[pygame.K_RIGHT] and not main.blocking_player_right and not main.cutscene_onlevel:
                main.scroll_display_x -= main.scroll_speed_x
            elif keys.get_pressed()[pygame.K_LEFT] and not main.blocking_player_left and not main.cutscene_onlevel:
                main.scroll_display_x += main.scroll_speed_x


            boo.update()
            player.update()
            draw_group.update()
            draw_game()
            pygame.display.update()
        else:
            pass

    def level_06(self):
        if self.state == 'level_06':
            display_game.blit(scene.bg_level6, [scene.bg_level6_pos_x + main.scroll_display_x, scene.bg_level6_pos_y])
            # Rects para passagem de mapa
            #level_01b = pygame.draw.rect(display_game, (0, 0, 0), (2500 + main.scroll_display_x, 600, 68, 147))
            #hitbox_player = pygame.draw.rect(display_game, (123, 123,123), (player.rect.x, player.rect.y, player.rect.width, player.rect.height))

            # Definindo BGS
            def draw_initial():
                pygame.mixer.music.load('musics/bgs/forest2.ogg')
                pygame.mixer.music.play(-1, 0.0)
                player.rect.x = 925

            def draw_game():
                draw_group.draw(display_game)
                display_game.blit(player.image, [player.rect.x, player.rect.y])
                display_game.blit(boo.image, [player.rect.x + main.boo_distance_x, player.rect.y - 15])


            for event in pygame.event.get():
                # condicional para sair do loop
                if event.type == pygame.QUIT or keys.get_pressed()[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

                # atualizando os dados na tela
            if main.call_started == 1:
                main.call_started = 0
                draw_initial()

            if main.scroll_display_x > 165:
                main.blocking_player_left = True
            else:
                main.blocking_player_left = False

            if main.scroll_display_x < -2086:
                main.blocking_player_right = True
            else:
                main.blocking_player_right = False

            # Effect scrolling Left
            if keys.get_pressed()[pygame.K_RIGHT] and not main.blocking_player_right and not main.cutscene_onlevel:
                main.scroll_display_x -= main.scroll_speed_x
            elif keys.get_pressed()[pygame.K_LEFT] and not main.blocking_player_left and not main.cutscene_onlevel:
                main.scroll_display_x += main.scroll_speed_x


            boo.update()
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
        if self.state == 'level_03':
            self.level_03()
        if self.state == 'level_04':
            self.level_04()
        if self.state == 'level_05':
            self.level_05()
        if self.state == 'level_06':
            self.level_06()


# Estado do jogo
game_state = GameState()

# Loop do jogo
while running_game:
    game_state.state_manager()

# encerrando os modulos do pygame
pygame.quit()
