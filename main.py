import pygame

import sys

from player import Player

#inicializando os modulos do pygame
pygame.init()

#configurações
black_color = (22, 22, 22)
font = pygame.font.SysFont('Montserrat', 48)
background = pygame.image.load('images/misc/Menu.png')
background = pygame.transform.scale(background, (1920, 1080))
running_game = True

#criando a janela do jogo
width = 1920
height = 1080
display_game = pygame.display.set_mode((width, height))
pygame.display.set_caption('Fall')
display_game.fill(black_color) #preenchendo o fundo
#janela.blit() #mostrando na tela

#configurando o BGM
pygame.mixer.music.load('musics/bgm/fundo.ogg')
pygame.mixer.music.play(-1, 0.0)
bgm_on = True

#SFXs
selecting_sfx = pygame.mixer.Sound('musics/sfx/selecting.ogg')

#Keys temporarias
keys = pygame.key

#Group
draw_group = pygame.sprite.Group()

#objetos
player = Player()

def draw_game():
    # preenchendo o fundo da janela com o background
    display_game.blit(background, (120, 0))
    draw_group.draw(display_game)

def set_button_menu():
    mouse_position = pygame.mouse.get_pos()
    start_button = pygame.sprite.Sprite(draw_group)
    options_button = pygame.sprite.Sprite(draw_group)
    quit_button = pygame.sprite.Sprite(draw_group)
    start_button.image = pygame.image.load('images/menu/start_button.png')
    options_button.image = pygame.image.load('images/menu/options_button.png')
    quit_button.image = pygame.image.load('images/menu/quit_button.png')
    start_button.rect = pygame.Rect(1150, 400, 384, 63)
    options_button.rect = pygame.Rect(1150, 475, 384, 63)
    quit_button.rect = pygame.Rect(1150, 550, 384, 63)

    if start_button.rect.collidepoint(mouse_position):
        if pygame.mouse.get_pressed(3)[0] == 1:
            print("Iniciar jogo")
    if options_button.rect.collidepoint(mouse_position):
        if pygame.mouse.get_pressed(3)[0] == 1:
            print("Abrir opcoes")
    if quit_button.rect.collidepoint(mouse_position):
        if pygame.mouse.get_pressed(3)[0] == 1:
            pygame.event.get(quit())

# loop do jogo
while running_game:
    #checando eventos
    for event in pygame.event.get():
        #condicional para sair do loop
        if event.type == pygame.QUIT:
            running_game = False

        set_button_menu()
        draw_game()

        # Esc para fechar o jogo.
        if keys.get_pressed()[pygame.K_ESCAPE]:
            running_game = False

        # atualizando os dados na tela
        pygame.display.update()

#encerrando os modulos do pygame
pygame.quit()










