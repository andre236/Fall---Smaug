import pygame
from pygame.locals import*
from player import Player
import sys

#inicializando os modulos do pygame
pygame.init()

#configurações
black_color = (22, 22, 22)
font = pygame.font.SysFont('Montserrat', 48)
running_game = True

#criando a janela do jogo
width = 1920
height = 1080
display_game = pygame.display.set_mode((width, height))
pygame.display.set_caption('Fall')
display_game.fill(black_color)

# configurando o BGM
pygame.mixer.music.load('musics/bgm/mainmenu.ogg')
pygame.mixer.music.play(-1, 0.0)

#SFXs
selecting_sfx = pygame.mixer.Sound('musics/sfx/selecting.ogg')

#Keys temporarias
keys = pygame.key

#Group
draw_group = pygame.sprite.Group()

class GameState():
    def __init__(self):
        self.state = 'menu_scene'

    def menu_scene(self):
        # Definindo BG
        background = pygame.image.load('images/misc/Menu.png')
        background = pygame.transform.scale(background, (1920, 1080))
        display_game.blit(background, (120, 0))

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

        def draw_game():
            draw_group.draw(display_game)

        for event in pygame.event.get():
            # condicional para sair do loop
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            draw_game()
            # atualizando os dados na tela
            pygame.display.update()

    def level_01(self):
        # Definindo BG
        background_scenetest = pygame.image.load('images/bg/background1.png')
        background_scenetest = pygame.transform.scale(background_scenetest, (1920, 1200))
        display_game.blit(background_scenetest, (0, 0))
        pygame.mixer.music.stop()
        player = Player()

        def draw_game():
            draw_group.empty()
            display_game.blit(background_scenetest, (0, 0))
            player.add(draw_group)
            draw_group.draw(display_game)

        for event in pygame.event.get():
            # condicional para sair do loop
            if event.type == pygame.QUIT or keys.get_pressed()[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()

            draw_game()
            # atualizando os dados na tela
            pygame.display.update()

    def state_manager(self):
        if self.state == 'menu_scene':
            self.menu_scene()
        if self.state == 'first_cutscene':
            self.first_cutscene()
        if self.state == 'level_01':
            self.level_01()

# estado do jogo
game_state = GameState()

# loop do jogo
while running_game:
    game_state.state_manager()

#encerrando os modulos do pygame
pygame.quit()










