import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init
pygame.font.init()
pygame.mixer.init()

musica_de_fundo = pygame.mixer.music.load("joao tinti\musicas\BoxCat Games - CPU Talk.mp3")
pygame.mixer.music.play(-1)

largura = 640
altura = 480
x = largura/2
y = largura/2

x_azul = randint(50, 590)
y_azul = randint(50, 430)
pontos = 0
fonte = pygame.font.SysFont("arial", 40, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo")
relogio = pygame.time.Clock() # função para conseguir definir o FPS

while True:
    # Pintar
    tela.fill((0, 0, 0))
    mensagem = f"Pontos: {pontos}"
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
    ret_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, 50, 50))
    ret_azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 50, 50))
    tela.blit(texto_formatado, (450, 40))
    pygame.display.update()
    
    # Calcular as regras
    relogio.tick(30) # define o FPS
    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(50, 590)
        y_azul = randint(50, 430)
        pontos += 1
    
    # Eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        # if event.type == KEYDOWN:
        #     if event.key == K_a:
        #         x -= 20
        #     if event.key == K_d:
        #         x += 20
        #     if event.key == K_w:
        #         y -= 20
        #     if event.key == K_s:
        #         y += 20
    if pygame.key.get_pressed()[K_a]:
        x -= 20
    if pygame.key.get_pressed()[K_d]:
        x += 20
    if pygame.key.get_pressed()[K_w]:
        y -= 20
    if pygame.key.get_pressed()[K_s]:
        y += 20