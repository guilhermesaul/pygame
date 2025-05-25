import pygame
from pygame.locals import *
from sys import exit

pygame.init

largura = 640
altura = 480
x = largura/2
y = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo")
relogio = pygame.time.Clock() # função para conseguir definir o FPS

while True:
    # Calcular as regras
    relogio.tick(30) # define o FPS
    if y - 50 >= altura:
        y = 0
    y += 5
    # Pintar
    tela.fill((0, 0, 0))
    pygame.draw.rect(tela, (255, 0, 0), (x, y, 50, 50))
    pygame.display.update()
    
    # Eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()  