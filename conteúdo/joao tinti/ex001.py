import pygame
from pygame.locals import *
from sys import exit

pygame.init

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))

while True:
    # Calcular as regras:
    
    # Pintar
    tela.fill((0, 0, 0))
    pygame.display.set_caption("Jogo")
    pygame.draw.circle(tela, (255, 0, 255), (220, 265), 30, 0)
    pygame.draw.rect(tela, (255, 0, 0), (320, 240, 50, 50))
    pygame.draw.line(tela, (255, 255, 0), (390, 0), (390, 600), 5)
    pygame.display.update()
    
    # Eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()  