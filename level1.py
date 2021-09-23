import pygame
from pygame.locals import*
import sys

#inicializando os modulos do pygame
pygame.init()

#configurações
black_color = (22, 22, 22)
font = pygame.font.SysFont('Montserrat', 48)
background = pygame.image.load('images/bg/background1.png')
running_game = True

#criando a janela do jogo
width = 1200
height = 720
display_game = pygame.display.set_mode((width, height))
pygame.display.set_caption('Fall')
display_game.fill(black_color) #preenchendo o fundo
#janela.blit() #mostrando na tela

#configurando o BGM
pygame.mixer.music.load('musics/bgm/mainmenu.ogg')
pygame.mixer.music.play(-1, 0.0)
bgm_on = True

#SFXs
selecting_sfx = pygame.mixer.Sound('musics/sfx/selecting.ogg')

#Keys temporarias
keys = pygame.key

#Group
draw_group = pygame.sprite.Group()

#Criando os botoes de Menu
start_button = pygame.sprite.Sprite(draw_group)
options_button = pygame.sprite.Sprite(draw_group)
quit_button = pygame.sprite.Sprite(draw_group)
start_button.image = pygame.image.load('images/menu/start_button.png')
options_button.image = pygame.image.load('images/menu/options_button.png')
quit_button.image = pygame.image.load('images/menu/quit_button.png')
start_button.rect = pygame.Rect(1150, 400, 384, 63)
options_button.rect = pygame.Rect(1150, 475, 384, 63)
quit_button.rect = pygame.Rect(1150, 550, 384, 63)

#starting scene
display_game.blit(background_menu, (0, 0))

def draw_game():
    draw_group.draw(display_game)

def changing_scene():
    pygame.mixer.music.stop()
    draw_group.empty()
    display_game.fill(black_color)
    menu_scene = False

def set_buttons_fuctions():
    mouse_position = pygame.mouse.get_pos()
    if start_button.rect.collidepoint(mouse_position):
        if pygame.mouse.get_pressed(3)[0] == 1:
            changing_scene()

    if options_button.rect.collidepoint(mouse_position):
        if pygame.mouse.get_pressed(3)[0] == 1:
            print("Abrir opcoes")
    if quit_button.rect.collidepoint(mouse_position):
        if pygame.mouse.get_pressed(3)[0] == 1:
            main.running_game = False

# loop do jogo
while running_game:
    #checando eventos
    for event in pygame.event.get():
        #condicional para sair do loop
        if event.type == pygame.QUIT:
            running_game = False

        set_buttons_fuctions()
        draw_game()

        # Esc para fechar o jogo.
        if keys.get_pressed()[pygame.K_ESCAPE]:
            running_game = False

        # atualizando os dados na tela
        pygame.display.update()

#encerrando os modulos do pygame
pygame.quit()
