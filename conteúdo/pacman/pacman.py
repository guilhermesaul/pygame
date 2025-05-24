import pygame

pygame.init

tela = pygame.display.set_mode((640, 480)) # cria a tela
x = 10 # Definindo eixo x que a bolinha vai aparecer
y = 10 # Definindo eixo y que a bolinha vai aparecer
raio = 30
velocidade = 0.1
vel_x = velocidade
vel_y = velocidade
amarelo = (255, 255, 0) # Definindo cor
preto = (0, 0, 0) # Definindo cor
while True:
    
    # Calcula as regras
    x += vel_x
    y += vel_y
    if x + raio> 640:
        vel_x = -velocidade # Fazendo a bolinha percorrer a tela toda sem ultrapassar a tela
    if x - raio < 0:
        vel_x = velocidade # Fazendo a bolinha percorrer a tela toda sem ultrapassar a tela
    if y + raio > 480:
        vel_y = -velocidade # Fazendo a bolinha percorrer a tela toda sem ultrapassar a tela
    if y - raio < 0:
        vel_y = velocidade # Fazendo a bolinha percorrer a tela toda sem ultrapassar a tela
    
    # Pinta
    tela.fill(preto) # Colocando o fundo preto
    pygame.draw.circle(tela, amarelo, (int(x), int(y)), raio, 0) # Desenhando um circulo na tela
    pygame.display.update() # Atualizando a tela para aparecer o desenho
    
    # Eventos
    for e in pygame.event.get(): # Botando a opção de fechar a janela
        if e.type == pygame.QUIT: # Botando a opção de fechar a janela
            exit() # Botando a opção de fechar a janela