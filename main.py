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
font_puzzle = pygame.font.SysFont('Montserrat', 120)
# Primeiro diálogo
# Group
draw_group = pygame.sprite.Group()

white = (255,255,255)
black = (0, 0, 0)
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
texts_dialogue_level3.append(font.render("Boo: Estamos a um tempo andando, mas eu não perguntei qual era o seu nome", False, white))
texts_dialogue_level3.append(font.render("Lucca: Meu nome é Lucca", False, white))
texts_dialogue_level3.append(font.render("Boo: Olha Lucca, eu sei que é difícil entender,", False, white))
texts_dialogue_level3.append(font.render("Boo: Mas não acho que deveria acreditar na carta,", False, white))
texts_dialogue_level3.append(font.render("Boo: Eu nunca ouvi falar de Trickster", False, white))
texts_dialogue_level3.append(font.render("Lucca: Você não entende, eu sinto que vai dar certo,", False, white))
texts_dialogue_level3.append(font.render("Lucca: Vou trazer minha mãe de volta, e todos vão ficar felizes", False, white))
texts_dialogue_level3.append(font.render("Lucca: Se você não acredita em mim, por que continua me seguindo?", False, white))
texts_dialogue_level3.append(font.render("Boo: Lucca...eu não desacredito de você, mas há certas coisa que não podemos mudar", False, white))
texts_dialogue_level3.append(font.render("Lucca: Boo, você vai ver, tudo vai dar certo", False, white))
texts_dialogue_level3.append(font.render("Boo: ...", False, white))

dialogue_onlevel4 = False
texts_dialogue_level4 = []
current_text_dialogue_level4 = 0
texts_dialogue_level4.append(font.render("Boo: Certo Lucca, para que possamos continuar.", False, white))
texts_dialogue_level4.append(font.render("Boo: Você precisa resolver um puzzle simples.", False, white))
texts_dialogue_level4.append(font.render("Boo: Basta encaixar as coisas em seu devido lugar", False, white))

dialogue_onlevel5a = False
texts_dialogue_level5a = []
current_text_dialogue_level5a = 0
texts_dialogue_level5a.append(font.render("Boo: Viu? não foi difícil, Lucca", False, black))
texts_dialogue_level5a.append(font.render("Boo: Quando se deseja fortemente algo,", False, black))
texts_dialogue_level5a.append(font.render("Boo: Temos que enfrentar alguns obstáculos em nosso caminho.", False, black))

dialogue_onlevel5b = False
texts_dialogue_level5b = []
current_text_dialogue_level5b = 0
texts_dialogue_level5b.append(font.render("Boo: Olha, Lucca!", False, black))
texts_dialogue_level5b.append(font.render("Boo: Mais uma borboleta!", False, black))
texts_dialogue_level5b.append(font.render("Boo: Talvez você consiga mais alguma pista", False, black))

dialogue_onlevel5c = False
texts_dialogue_level5c = []
current_text_dialogue_level5c = 0
texts_dialogue_level5c.append(font.render("Oblis: Ha ha ha ha ha!", False, black))
texts_dialogue_level5c.append(font.render("Oblis: Você acreditou mesmo que trickster era real?", False, black))
texts_dialogue_level5c.append(font.render("Oblis: Garoto tolo, não há nada aqui", False, black))
texts_dialogue_level5c.append(font.render("Lucca: Oh não, você estava certo, Boo... ", False, black))
texts_dialogue_level5c.append(font.render("Lucca: E e agora?", False, black))

dialogue_onlevel5d = False
texts_dialogue_level5d = []
current_text_dialogue_level5d = 0
texts_dialogue_level5d.append(font.render("Boo: Olha Lucca, sei que nos momentos mais difíceis", False, black))
texts_dialogue_level5d.append(font.render("Boo: Confiamos em muitas pessoas,", False, black))
texts_dialogue_level5d.append(font.render("Boo: O processo de tristeza leva tempo para passar", False, black))
texts_dialogue_level5d.append(font.render("Boo: E é quando ficamos mais frágeis", False, black))
texts_dialogue_level5d.append(font.render("Lucca: O que devo fazer então? Continuar a procurar?", False, black))
texts_dialogue_level5d.append(font.render("Boo: Eu não posso respondê-lo... Infelizmente", False, black))
texts_dialogue_level5d.append(font.render("Boo: Você trilha seu caminho, a escolha é sua Lucca...", False, black))

dialogue_onlevel6a = False
texts_dialogue_level6a = []
current_text_dialogue_level6a = 0
texts_dialogue_level6a.append(font.render("Lucca: Ah tudo isso é tão frustrante!", False, black))
texts_dialogue_level6a.append(font.render("Lucca: Se o tempo ou a morte não existisse,", False, black))
texts_dialogue_level6a.append(font.render("Lucca: Eu poderia ter ficado com minha mãe...", False, black))
texts_dialogue_level6a.append(font.render("Boo: Lucca, se não houvesse tempo, não haveria começo e fim,", False, black))
texts_dialogue_level6a.append(font.render("Boo: Somente o infinito e a eternidade, isso quer dizer", False, black))
texts_dialogue_level6a.append(font.render("Boo: Que provavelmente não seria possível existir", False, black))
texts_dialogue_level6a.append(font.render("Lucca: Mas também, não seria possível perder", False, black))

dialogue_onlevel6b = False
texts_dialogue_level6b = []
current_text_dialogue_level6b = 0
texts_dialogue_level6b.append(font.render("Lucca: Oh, mas o que é isso?", False, black))
texts_dialogue_level6b.append(font.render("Tempo: Ola Lucca! ", False, black))
texts_dialogue_level6b.append(font.render("Tempo: Eu tenho te observado desde a sua chegada a esse mundo", False, black))
texts_dialogue_level6b.append(font.render("Tempo: Tenho compreendido teus objetivos e esperado para que me encontrasse.", False, black))
texts_dialogue_level6b.append(font.render("Lucca: Mas quem é você? Como isso é possível?", False, black))
texts_dialogue_level6b.append(font.render("Tempo: Eu sou o Tempo! Aquele que cura, o que não tem pressa", False, black))
texts_dialogue_level6b.append(font.render("Tempo: Sou um correio, e tudo que faço é parte do destino.", False, black))
texts_dialogue_level6b.append(font.render("Lucca: destino, como tirar alguém que amamos é parte do destino?", False, black))
texts_dialogue_level6b.append(font.render("Tempo: Lucca, há coisas que são inexplicáveis, o destino é um deles", False, black))
texts_dialogue_level6b.append(font.render("Tempo: O que você sente agora, a saudade, a raiva, a frustração,", False, black))
texts_dialogue_level6b.append(font.render("Tempo: o desejo de voltar ao passado, é comum", False, black))
texts_dialogue_level6b.append(font.render("Tempo: Pense na vida como uma grande escola,", False, black))
texts_dialogue_level6b.append(font.render("Tempo: Eu, sou apenas um professor,", False, black))
texts_dialogue_level6b.append(font.render("Tempo: todos esses sentimentos negativos são desafios", False, black))
texts_dialogue_level6b.append(font.render("Tempo: Eu como professor, te ensino a resolvê-los", False, black))
texts_dialogue_level6b.append(font.render("Tempo: Mas é você quem escolhe, se vai continuar a olhar para trás,", False, black))
texts_dialogue_level6b.append(font.render("Tempo: Viver no passado, ou vai seguir no presente para o futuro,", False, black))
texts_dialogue_level6b.append(font.render("Tempo: Você pode ter perdido sua mãe fisicamente,", False, black))
texts_dialogue_level6b.append(font.render("Tempo: mas há algo que ninguém pode tirar de você,", False, black))
texts_dialogue_level6b.append(font.render("Tempo: Nem mesmo eu", False, black))
texts_dialogue_level6b.append(font.render("Tempo: São as memórias.", False, black))
texts_dialogue_level6b.append(font.render("Tempo: Dentro do seu coração e da sua mente", False, black))
texts_dialogue_level6b.append(font.render("Tempo: Ela ainda existe, e isso é mais forte do que tudo", False, black))
texts_dialogue_level6b.append(font.render("Tempo: Agora, é você quem escolhe Lucca", False, black))

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
# Oblis
oblis = Object(draw_group)
oblis.image = pygame.image.load('sprites/entities/oblis/oblis - walk- frame7.png')
oblis.width = 60
oblis.height = 60

# Portal
portal = Object(draw_group)
portal.image = pygame.image.load('sprites/objects/portal.png')
portal.width = 68
portal.height = 147

fadescreen_on = False


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

# Puzzle level 5
# PUZZLE LVL 5
text_puzzle_level5_hint = []
text_puzzle_level5_hint.append(font.render("Faço pessoas felizes, algumas triste, junto a galera,", False, white))
text_puzzle_level5_hint.append(font.render("mas também posso estar sozinho, as pessoas costumam usar", False, white))
text_puzzle_level5_hint.append(font.render("uma grande imaginação comigo, arranco risadas, mas também", False, white))
text_puzzle_level5_hint.append(font.render("te dou alguns machucados, quem sou eu?", False, white))
current_text_puzzle_digit_2 = 0
current_text_puzzle_digit_3 = 0
current_text_puzzle_digit_4 = 0
current_text_puzzle_digit_6 = 0
current_text_puzzle_digit_7 = 0
current_text_puzzle_digit_8 = 0
current_text_puzzle_digit_9 = 0
current_text_puzzle_digit_10 = 0
text_puzzle_digit_1 = ["B"] # d2 R = 18; d3 I = 9; d4 = N = 14 ; d6 = 1; d7 D = 4 ; d8 = 5; d9 = 9; d10 R = 18  ( 18 9 14 1 4 5 9 18
text_puzzle_digit_1_render = font_puzzle.render(text_puzzle_digit_1[0], False, white)
text_puzzle_digit_2 = ["_", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
text_puzzle_digit_2_render = font_puzzle.render(text_puzzle_digit_2[current_text_puzzle_digit_2], False, white)
text_puzzle_digit_3 = ["_", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
text_puzzle_digit_3_render = font_puzzle.render(text_puzzle_digit_3[current_text_puzzle_digit_3], False, white)
text_puzzle_digit_4 = ["_", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
text_puzzle_digit_4_render = font_puzzle.render(text_puzzle_digit_4[current_text_puzzle_digit_4], False, white)
text_puzzle_digit_5 = ["C"]
text_puzzle_digit_5_render = font_puzzle.render(text_puzzle_digit_5[0], False, white)
text_puzzle_digit_6 = ["_", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
text_puzzle_digit_6_render = font_puzzle.render(text_puzzle_digit_6[current_text_puzzle_digit_6], False, white)
text_puzzle_digit_7 = ["_", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
text_puzzle_digit_7_render = font_puzzle.render(text_puzzle_digit_7[current_text_puzzle_digit_7], False, white)
text_puzzle_digit_8 = ["_", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
text_puzzle_digit_8_render = font_puzzle.render(text_puzzle_digit_8[current_text_puzzle_digit_8], False, white)
text_puzzle_digit_9 = ["_", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
text_puzzle_digit_9_render = font_puzzle.render(text_puzzle_digit_9[current_text_puzzle_digit_9], False, white)
text_puzzle_digit_10 = ["_", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
text_puzzle_digit_10_render = font_puzzle.render(text_puzzle_digit_10[current_text_puzzle_digit_10], False, white)
text_puzzle_digit_11 = ["A"]
text_puzzle_digit_11_render = font_puzzle.render(text_puzzle_digit_11[0], False, white)


arrow_up_digit_1 = pygame.image.load('images/misc/arrow_up.png')
arrow_up_digit_2 = pygame.image.load('images/misc/arrow_up.png')
arrow_up_digit_2_rect = pygame.Rect(500, 460, arrow_up_digit_2.get_rect().width, arrow_up_digit_2.get_rect().height)
arrow_up_digit_3 = pygame.image.load('images/misc/arrow_up.png')
arrow_up_digit_3_rect = pygame.Rect(580, 460, arrow_up_digit_3.get_rect().width, arrow_up_digit_3.get_rect().height)
arrow_up_digit_4 = pygame.image.load('images/misc/arrow_up.png')
arrow_up_digit_4_rect = pygame.Rect(665, 460, arrow_up_digit_4.get_rect().width, arrow_up_digit_4.get_rect().height)
arrow_up_digit_5 = pygame.image.load('images/misc/arrow_up.png')
arrow_up_digit_6 = pygame.image.load('images/misc/arrow_up.png')
arrow_up_digit_6_rect = pygame.Rect(815, 460, arrow_up_digit_6.get_rect().width, arrow_up_digit_6.get_rect().height)
arrow_up_digit_7 = pygame.image.load('images/misc/arrow_up.png')
arrow_up_digit_7_rect = pygame.Rect(890, 460, arrow_up_digit_7.get_rect().width, arrow_up_digit_7.get_rect().height)
arrow_up_digit_8 = pygame.image.load('images/misc/arrow_up.png')
arrow_up_digit_8_rect = pygame.Rect(965, 460, arrow_up_digit_8.get_rect().width, arrow_up_digit_8.get_rect().height)
arrow_up_digit_9 = pygame.image.load('images/misc/arrow_up.png')
arrow_up_digit_9_rect = pygame.Rect(1040, 460, arrow_up_digit_9.get_rect().width, arrow_up_digit_9.get_rect().height)
arrow_up_digit_10 = pygame.image.load('images/misc/arrow_up.png')
arrow_up_digit_10_rect = pygame.Rect(1115, 460, arrow_up_digit_10.get_rect().width, arrow_up_digit_10.get_rect().height)
arrow_up_digit_11 = pygame.image.load('images/misc/arrow_up.png')


arrow_down_digit_1 = pygame.image.load('images/misc/arrow_down.png') #
arrow_down_digit_2 = pygame.image.load('images/misc/arrow_down.png')
arrow_down_digit_2_rect = pygame.Rect(500, 620, arrow_down_digit_2.get_rect().width, arrow_down_digit_2.get_rect().height)
arrow_down_digit_3 = pygame.image.load('images/misc/arrow_down.png')
arrow_down_digit_3_rect = pygame.Rect(580, 620, arrow_down_digit_3.get_rect().width, arrow_down_digit_3.get_rect().height)
arrow_down_digit_4 = pygame.image.load('images/misc/arrow_down.png')
arrow_down_digit_4_rect = pygame.Rect(665, 620, arrow_down_digit_4.get_rect().width, arrow_down_digit_4.get_rect().height)
arrow_down_digit_5 = pygame.image.load('images/misc/arrow_down.png') #
arrow_down_digit_6 = pygame.image.load('images/misc/arrow_down.png')
arrow_down_digit_6_rect = pygame.Rect(815, 620, arrow_down_digit_6.get_rect().width, arrow_down_digit_6.get_rect().height)
arrow_down_digit_7 = pygame.image.load('images/misc/arrow_down.png')
arrow_down_digit_7_rect = pygame.Rect(890, 620, arrow_down_digit_7.get_rect().width, arrow_down_digit_7.get_rect().height)
arrow_down_digit_8 = pygame.image.load('images/misc/arrow_down.png')
arrow_down_digit_8_rect = pygame.Rect(965, 620, arrow_down_digit_8.get_rect().width, arrow_down_digit_8.get_rect().height)
arrow_down_digit_9 = pygame.image.load('images/misc/arrow_down.png')
arrow_down_digit_9_rect = pygame.Rect(1040, 620, arrow_down_digit_9.get_rect().width, arrow_down_digit_9.get_rect().height)
arrow_down_digit_10 = pygame.image.load('images/misc/arrow_down.png')
arrow_down_digit_10_rect = pygame.Rect(1115, 620, arrow_down_digit_10.get_rect().width, arrow_down_digit_10.get_rect().height)
arrow_down_digit_11 = pygame.image.load('images/misc/arrow_down.png') #

puzzle_level5_solved = False

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
                pygame.time.delay(15)
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
            level_01b = pygame.draw.rect(display_game, (0, 0, 0), (2920 + main.scroll_display_x, 635 + main.scroll_display_y, 34, 65))
            #hitbox_player = pygame.draw.rect(display_game, (123, 123,123), (player.rect.x, player.rect.y, player.rect.width, player.rect.height))
            fade_to_black = pygame.Surface((1920, 1080))
            if main.fadescreen_on:
                fade_to_black.fill((0, 0, 0))


            # Definindo BGS
            def draw_initial():
                pygame.mixer.music.load('musics/bgm/bgm_level1.ogg')
                pygame.mixer.music.play(-1, 0.0)
                game_state.state = 'level_01'
                player.rect.x = 925
                portal.rect.x = 2900
                portal.rect.y = 600

            def draw_game():
                draw_group.draw(display_game)
                display_game.blit(player.image, [player.rect.x, player.rect.y])
                display_game.blit(boo.image, [player.rect.x + main.boo_distance_x, player.rect.y - 15])
                display_game.blit(portal.image, [portal.rect.x + main.scroll_display_x, portal.rect.y])
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
                main.fadescreen_on = True
                for alpha in range(0, 300):
                    fade_to_black.set_alpha(alpha)
                    display_game.blit(fade_to_black, [0, 0])
                    pygame.display.update()
                    pygame.time.delay(5)
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
            #Fade
            fade_to_black = pygame.Surface((1920, 1080))
            if main.fadescreen_on:
                fade_to_black.fill((0, 0, 0))
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
                main.fadescreen_on = False
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




            if main.cutscene_onlevel and not main.butterfly_alive:
                display_game.blit(main.texts_dialogue_butterflyscene[main.current_text_dialogue_butterflyscene], [960 - (main.texts_dialogue_butterflyscene[main.current_text_dialogue_butterflyscene].get_rect().width / 2), 900])
                    # Passar diálogo
                if keys.get_pressed()[pygame.K_z] and main.cutscene_onlevel and main.current_text_dialogue_butterflyscene < len(main.texts_dialogue_butterflyscene):
                    pygame.time.delay(500)
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

            if pygame.Rect.colliderect(player.rect, portal_level_03):
                pygame.mixer.music.fadeout(1000)
                for alpha in range(0, 300):
                    fade_to_black.set_alpha(alpha)
                    display_game.blit(fade_to_black, [0, 0])
                    pygame.display.update()
                    pygame.time.delay(5)
                main.scroll_display_x = 0
                main.call_started = 1
                game_state.state = 'level_03'

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
             #Fade
            fade_to_black = pygame.Surface((1920, 1080))
            if main.fadescreen_on:
                fade_to_black.fill((0, 0, 0))
            # Rects para passagem de mapa
            portal_level_04 = pygame.draw.rect(display_game, (0, 0, 0), (4920 + main.scroll_display_x, 625, 34, 77))
            #hitbox_player = pygame.draw.rect(display_game, (123, 123,123), (player.rect.x, player.rect.y, player.rect.width, player.rect.height))

            # Definindo BGS
            def draw_initial():
                draw_group.empty()
                for alpha in reversed(range(0, 300)):
                    fade_to_black.set_alpha(alpha)
                    display_game.blit(fade_to_black, [0, 0])
                    pygame.display.update()
                    pygame.time.delay(5)
                pygame.mixer.music.stop()
                pygame.mixer.music.load('musics/bgm/bgm_level3b.ogg')
                pygame.mixer.music.play(-1, 0.0)
                player.rect.x = 925
                box.rect.x = 1200
                box.rect.y = 700
                main.dialogue_onlevel3 = True
                portal.rect.x = 4900
                portal.rect.y = 600
                player.current_height_ground = 650

            def draw_game():
                draw_group.draw(display_game)
                display_game.blit(player.image, [player.rect.x, player.rect.y])
                display_game.blit(portal.image, [4900 + main.scroll_display_x, 600])
                if not player.image_flipped:
                    display_game.blit(boo.image, [player.rect.x - 25, player.rect.y])
                else:
                    display_game.blit(boo.image, [player.rect.x + 20, player.rect.y])
                if dialogue_onlevel3:
                    display_game.blit(main.texts_dialogue_level3[main.current_text_dialogue_level3], [960 - (main.texts_dialogue_level3[main.current_text_dialogue_level3].get_rect().width / 2), 900])
                    # Passar diálogo
                if keys.get_pressed()[pygame.K_z] and main.dialogue_onlevel3 and main.current_text_dialogue_level3 < len(main.texts_dialogue_level3):
                    pygame.time.delay(500)
                    main.current_text_dialogue_level3 += 1
                    if main.current_text_dialogue_level3 >= len(main.texts_dialogue_level3):
                        main.current_text_dialogue_level3 = len(main.texts_dialogue_level3) - 1
                        main.dialogue_onlevel3 = False

            for event in pygame.event.get():
                # condicional para sair do loop
                if event.type == pygame.QUIT or keys.get_pressed()[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

            if main.call_started == 1:
                main.call_started = 0
                draw_initial()

            if pygame.Rect.colliderect(player.rect, portal_level_04):
                pygame.mixer.music.fadeout(1000)
                for alpha in range(0, 300):
                    fade_to_black.set_alpha(alpha)
                    display_game.blit(fade_to_black, [0, 0])
                    pygame.display.update()
                    pygame.time.delay(5)
                main.scroll_display_x = 0
                main.call_started = 1
                pygame.mixer.music.play(-1, 0.0)
                player.rect.x = 925
                game_state.state = 'level_04'

            # atualizando os dados na tela


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
            #Fade
            fade_to_black = pygame.Surface((1920, 1080))
            if main.fadescreen_on:
                fade_to_black.fill((0, 0, 0))
            # Rects para passagem de mapa
            #level_01b = pygame.draw.rect(display_game, (0, 0, 0), (2600 + main.scroll_display_x, 600, 68, 147))
            hitbox_box_time = pygame.draw.rect(display_game, (123, 123,123), (box_time.rect.x + main.scroll_display_x + main.force_box_time, box_time.rect.y, box_time.rect.width, box_time.rect.height))
            hitbox_box_love = pygame.draw.rect(display_game, (123, 123,123),(box_love.rect.x + main.scroll_display_x + main.force_box_love, box_love.rect.y, box_love.rect.width, box_love.rect.height))
            hitbox_box_death  = pygame.draw.rect(display_game, (123,123,123), (box_death.rect.x + main.scroll_display_x + main.force_box_death, box_death.rect.y, box_death.width, box_death.rect.height))

            #hitbox_player = pygame.draw.rect(display_game, (123, 123,123), (player.rect.x, player.rect.y, player.rect.width, player.rect.height))

            # Definindo BGS
            def draw_initial():
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
                if main.scroll_display_x <= -450 and not main.dialogue_onlevel4 and main.current_text_dialogue_level4 == 0:
                    main.dialogue_onlevel4 = True

                # Inicio do diálogo com Boo
                if main.dialogue_onlevel4:
                    display_game.blit(main.texts_dialogue_level4[main.current_text_dialogue_level4], [960 - (main.texts_dialogue_level4[main.current_text_dialogue_level4].get_rect().width / 2), 800])
                    # Passar diálogo
                if keys.get_pressed()[pygame.K_z] and main.dialogue_onlevel4 and main.current_text_dialogue_level4 < len(main.texts_dialogue_level4):
                    pygame.time.delay(500)
                    main.current_text_dialogue_level4 += 1
                    if main.current_text_dialogue_level4 >= len(main.texts_dialogue_level4):
                        main.current_text_dialogue_level4 = len(main.texts_dialogue_level4) - 1
                        main.dialogue_onlevel4 = False

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
                for alpha in range(0, 300):
                    fade_to_black.set_alpha(alpha)
                    display_game.blit(fade_to_black, [0, 0])
                    pygame.display.update()
                    pygame.time.delay(5)
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
            #Fade
            fade_to_black = pygame.Surface((1920, 1080))
            if main.fadescreen_on:
                fade_to_black.fill((0, 0, 0))

            # Rects para passagem de mapa
            portal_level_06 = pygame.draw.rect(display_game, (0, 0, 0), (2500 + main.scroll_display_x, 600, 68, 147))
            #hitbox_player = pygame.draw.rect(display_game, (123, 123,123), (player.rect.x, player.rect.y, player.rect.width, player.rect.height))

            # Definindo BGS
            def draw_initial():
                pygame.mixer.music.fadeout(1000)
                pygame.mixer.music.load('musics/bgm/bgm_level5.ogg')
                pygame.mixer.music.play(-1, 0.0)
                player.rect.x = 925
                butterfly.rect.x = 1600
                butterfly.rect.y = 650
                butterfly.width = 60
                butterfly.height = 60
                main.dialogue_onlevel5a = True

            def draw_game():
                draw_group.draw(display_game)
                display_game.blit(player.image, [player.rect.x, player.rect.y])
                if main.butterfly_alive:
                    display_game.blit(butterfly.image, [butterfly.rect.x + main.scroll_display_x, butterfly.rect.y])
                if not player.image_flipped:
                    display_game.blit(boo.image, [player.rect.x - 25, player.rect.y])
                else:
                    display_game.blit(boo.image, [player.rect.x + 20, player.rect.y])

                # Diálogo
                if main.dialogue_onlevel5a:
                    display_game.blit(main.texts_dialogue_level5a[main.current_text_dialogue_level5a], [960 - (main.texts_dialogue_level5a[main.current_text_dialogue_level5a].get_rect().width / 2), 800])
                    # Passar diálogo
                if keys.get_pressed()[pygame.K_z] and main.dialogue_onlevel5a and main.current_text_dialogue_level5a < len(main.texts_dialogue_level5a):
                    pygame.time.delay(500)
                    main.current_text_dialogue_level5a += 1
                    if main.current_text_dialogue_level5a >= len(main.texts_dialogue_level5a):
                        main.current_text_dialogue_level5a = len(main.texts_dialogue_level5a) - 1
                        main.dialogue_onlevel5a = False

                if main.scroll_display_x <= -450 and not main.dialogue_onlevel5b and current_text_dialogue_level5b == 0:
                    main.dialogue_onlevel5b = True

                if main.dialogue_onlevel5b:
                    display_game.blit(main.texts_dialogue_level5b[main.current_text_dialogue_level5b], [960 - (main.texts_dialogue_level5b[main.current_text_dialogue_level5b].get_rect().width / 2), 800])
                    # Passar diálogo
                if keys.get_pressed()[pygame.K_z] and main.dialogue_onlevel5b and main.current_text_dialogue_level5b < len(main.texts_dialogue_level5b):
                    pygame.time.delay(500)
                    main.current_text_dialogue_level5b += 1
                    if main.current_text_dialogue_level5b >= len(main.texts_dialogue_level5b):
                        main.current_text_dialogue_level5b = len(main.texts_dialogue_level5b) - 1
                        main.dialogue_onlevel5b = False

                if main.scroll_display_x <= -650 and main.butterfly_alive:
                    main.butterfly_alive = False
                    main.cutscene_onlevel = True

                if main.cutscene_onlevel and not main.puzzle_level5_solved:
                    mouse_position = pygame.mouse.get_pos()
                    backgroundrect = pygame.draw.rect(display_game, [0,0,0], [400, 250, 1060, 600])
                    display_game.blit(main.text_puzzle_level5_hint[0], [420, 250])
                    display_game.blit(main.text_puzzle_level5_hint[1], [420, 300])
                    display_game.blit(main.text_puzzle_level5_hint[2], [420, 350])
                    display_game.blit(main.text_puzzle_level5_hint[3], [420, 400])
                    display_game.blit(main.text_puzzle_digit_1_render, [420, 520])
                    display_game.blit(font_puzzle.render(main.text_puzzle_digit_2[current_text_puzzle_digit_2], False, white), [500, 520])
                    display_game.blit(font_puzzle.render(main.text_puzzle_digit_3[current_text_puzzle_digit_3], False, white), [580, 520])
                    display_game.blit(font_puzzle.render(main.text_puzzle_digit_4[current_text_puzzle_digit_4], False, white), [660, 520])
                    display_game.blit(main.text_puzzle_digit_5_render, [740, 520])
                    display_game.blit(font_puzzle.render(main.text_puzzle_digit_6[current_text_puzzle_digit_6], False, white), [820, 520])
                    display_game.blit(font_puzzle.render(main.text_puzzle_digit_7[current_text_puzzle_digit_7], False, white), [900, 520])
                    display_game.blit(font_puzzle.render(main.text_puzzle_digit_8[current_text_puzzle_digit_8], False, white), [980, 520])
                    display_game.blit(font_puzzle.render(main.text_puzzle_digit_9[current_text_puzzle_digit_9], False, white), [1040, 520])
                    display_game.blit(font_puzzle.render(main.text_puzzle_digit_10[current_text_puzzle_digit_10], False, white), [1120, 520])
                    display_game.blit(main.text_puzzle_digit_11_render, [1200, 520])
                    display_game.blit(main.arrow_up_digit_2, [500, 460])
                    display_game.blit(main.arrow_up_digit_3, [580, 460])
                    display_game.blit(main.arrow_up_digit_4, [665, 460])
                    display_game.blit(main.arrow_up_digit_6, [815, 460])
                    display_game.blit(main.arrow_up_digit_7, [890, 460])
                    display_game.blit(main.arrow_up_digit_8, [965, 460])
                    display_game.blit(main.arrow_up_digit_9, [1040, 460])
                    display_game.blit(main.arrow_up_digit_10, [1115, 460])
                    display_game.blit(main.arrow_down_digit_2, [500, 620])
                    display_game.blit(main.arrow_down_digit_3, [580, 620])
                    display_game.blit(main.arrow_down_digit_4, [665, 620])
                    display_game.blit(main.arrow_down_digit_6, [815, 620])
                    display_game.blit(main.arrow_down_digit_7, [890, 620])
                    display_game.blit(main.arrow_down_digit_8, [965, 620])
                    display_game.blit(main.arrow_down_digit_9, [1040, 620])
                    display_game.blit(main.arrow_down_digit_10, [1115, 620])

                    # UP
                    if main.arrow_up_digit_2_rect.collidepoint(mouse_position):
                        if pygame.mouse.get_pressed(3)[0] == 1:
                            pygame.time.delay(500)
                            main.current_text_puzzle_digit_2 += 1
                            if main.current_text_puzzle_digit_2 >= len(text_puzzle_digit_2):
                                main.current_text_puzzle_digit_2 = 0
                    # DOWN
                    if main.arrow_down_digit_2_rect.collidepoint(mouse_position):
                        if pygame.mouse.get_pressed(3)[0] == 1:
                            pygame.time.delay(500)
                            main.current_text_puzzle_digit_2 -= 1
                            if main.current_text_puzzle_digit_2 < 0:
                                main.current_text_puzzle_digit_2 = len(text_puzzle_digit_2) - 1

                    # UP
                    if main.arrow_up_digit_3_rect.collidepoint(mouse_position):
                        if pygame.mouse.get_pressed(3)[0] == 1:
                            pygame.time.delay(500)
                            main.current_text_puzzle_digit_3 += 1
                            if main.current_text_puzzle_digit_3 >= len(text_puzzle_digit_3):
                                main.current_text_puzzle_digit_3 = 0
                    # DOWN
                    if main.arrow_down_digit_3_rect.collidepoint(mouse_position):
                        if pygame.mouse.get_pressed(3)[0] == 1:
                            pygame.time.delay(500)
                            main.current_text_puzzle_digit_3 -= 1
                            if main.current_text_puzzle_digit_3 < 0:
                                main.current_text_puzzle_digit_3 = len(text_puzzle_digit_3) - 1

                    # UP
                    if main.arrow_up_digit_4_rect.collidepoint(mouse_position):
                        if pygame.mouse.get_pressed(3)[0] == 1:
                            pygame.time.delay(500)
                            main.current_text_puzzle_digit_4 += 1
                            if main.current_text_puzzle_digit_4 >= len(text_puzzle_digit_4):
                                main.current_text_puzzle_digit_4 = 0
                    # DOWN
                    if main.arrow_down_digit_4_rect.collidepoint(mouse_position):
                        if pygame.mouse.get_pressed(3)[0] == 1:
                            pygame.time.delay(500)
                            main.current_text_puzzle_digit_4 -= 1
                            if main.current_text_puzzle_digit_4 < 0:
                                main.current_text_puzzle_digit_4 = len(text_puzzle_digit_4) - 1

                    # UP
                    if main.arrow_up_digit_6_rect.collidepoint(mouse_position):
                        if pygame.mouse.get_pressed(3)[0] == 1:
                            pygame.time.delay(500)
                            main.current_text_puzzle_digit_6 += 1
                            if main.current_text_puzzle_digit_6 >= len(text_puzzle_digit_6):
                                main.current_text_puzzle_digit_6 = 0
                    # DOWN
                    if main.arrow_down_digit_6_rect.collidepoint(mouse_position):
                        if pygame.mouse.get_pressed(3)[0] == 1:
                            pygame.time.delay(500)
                            main.current_text_puzzle_digit_6 -= 1
                            if main.current_text_puzzle_digit_6 < 0:
                                main.current_text_puzzle_digit_6 = len(text_puzzle_digit_6) - 1

                    # UP
                    if main.arrow_up_digit_7_rect.collidepoint(mouse_position):
                        if pygame.mouse.get_pressed(3)[0] == 1:
                            pygame.time.delay(500)
                            main.current_text_puzzle_digit_7 += 1
                            if main.current_text_puzzle_digit_7 >= len(text_puzzle_digit_7):
                                main.current_text_puzzle_digit_7 = 0
                    # DOWN
                    if main.arrow_down_digit_7_rect.collidepoint(mouse_position):
                        if pygame.mouse.get_pressed(3)[0] == 1:
                            pygame.time.delay(500)
                            main.current_text_puzzle_digit_7 -= 1
                            if main.current_text_puzzle_digit_7 < 0:
                                main.current_text_puzzle_digit_7 = len(text_puzzle_digit_7) - 1

                    if main.arrow_up_digit_8_rect.collidepoint(mouse_position):
                        if pygame.mouse.get_pressed(3)[0] == 1:
                            pygame.time.delay(500)
                            main.current_text_puzzle_digit_8 += 1
                            if main.current_text_puzzle_digit_8 >= len(text_puzzle_digit_8):
                                main.current_text_puzzle_digit_8 = 0
                    # DOWN
                    if main.arrow_down_digit_8_rect.collidepoint(mouse_position):
                        if pygame.mouse.get_pressed(3)[0] == 1:
                            pygame.time.delay(500)
                            main.current_text_puzzle_digit_8 -= 1
                            if main.current_text_puzzle_digit_8 < 0:
                                main.current_text_puzzle_digit_8 = len(text_puzzle_digit_8) - 1

                    if main.arrow_up_digit_9_rect.collidepoint(mouse_position):
                        if pygame.mouse.get_pressed(3)[0] == 1:
                            pygame.time.delay(500)
                            main.current_text_puzzle_digit_9 += 1
                            if main.current_text_puzzle_digit_9 >= len(text_puzzle_digit_9):
                                main.current_text_puzzle_digit_9 = 0
                    # DOWN
                    if main.arrow_down_digit_9_rect.collidepoint(mouse_position):
                        if pygame.mouse.get_pressed(3)[0] == 1:
                            pygame.time.delay(500)
                            main.current_text_puzzle_digit_9 -= 1
                            if main.current_text_puzzle_digit_9 < 0:
                                main.current_text_puzzle_digit_9 = len(text_puzzle_digit_9) - 1

                    if main.arrow_up_digit_10_rect.collidepoint(mouse_position):
                        if pygame.mouse.get_pressed(3)[0] == 1:
                            pygame.time.delay(500)
                            main.current_text_puzzle_digit_10 += 1
                            if main.current_text_puzzle_digit_10 >= len(text_puzzle_digit_10):
                                main.current_text_puzzle_digit_10 = 0
                    # DOWN
                    if main.arrow_down_digit_10_rect.collidepoint(mouse_position):
                        if pygame.mouse.get_pressed(3)[0] == 1:
                            pygame.time.delay(500)
                            main.current_text_puzzle_digit_10 -= 1
                            if main.current_text_puzzle_digit_10 < 0:
                                main.current_text_puzzle_digit_10 = len(text_puzzle_digit_10) - 1
                         # 18 9 14 1 4 5 9 18
                    if current_text_puzzle_digit_2 == 18 and current_text_puzzle_digit_3 == 9 and current_text_puzzle_digit_4 ==  14 and current_text_puzzle_digit_6 == 1 and current_text_puzzle_digit_7 == 4 and current_text_puzzle_digit_8 == 5 and current_text_puzzle_digit_9 == 9 and current_text_puzzle_digit_10 == 18:
                        main.puzzle_level5_solved = True

                    if main.puzzle_level5_solved and main.cutscene_onlevel and not main.dialogue_onlevel5c:
                        main.dialogue_onlevel5c = True
                        if main.dialogue_onlevel5c:
                            display_game.blit(main.texts_dialogue_level5c[main.current_text_dialogue_level5c], [960 - (main.texts_dialogue_level5c[main.current_text_dialogue_level5c].get_rect().width / 2), 800])
                    # Passar diálogo
                    if keys.get_pressed()[pygame.K_z] and main.dialogue_onlevel5c and main.current_text_dialogue_level5c < len(main.texts_dialogue_level5c):
                        pygame.time.delay(500)
                        main.current_text_dialogue_level5c += 1
                        if main.current_text_dialogue_level5c >= len(main.texts_dialogue_level5c):
                            main.current_text_dialogue_level5c = len(main.texts_dialogue_level5c) - 1
                            main.dialogue_onlevel5c = False


                else:
                    pass

            for event in pygame.event.get():
                # condicional para sair do loop
                if event.type == pygame.QUIT or keys.get_pressed()[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

                # atualizando os dados na tela
            if main.call_started == 1:
                main.call_started = 0
                draw_initial()

            if pygame.Rect.colliderect(player.rect, portal_level_06):
                for alpha in range(0, 300):
                    fade_to_black.set_alpha(alpha)
                    display_game.blit(fade_to_black, [0, 0])
                    pygame.display.update()
                    pygame.time.delay(5)
                level_01b.width = 0
                level_01b.height = 0
                main.scroll_display_x = 0
                main.call_started = 1
                game_state.state = 'level_06'

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

            butterfly.update()
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
                player.rect.x = 925

            def draw_game():
                draw_group.draw(display_game)
                display_game.blit(player.image, [player.rect.x, player.rect.y])
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
