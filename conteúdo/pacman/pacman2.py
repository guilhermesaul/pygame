import pygame

pygame.init

screen = pygame.display.set_mode((800, 600), 0)
amarelo = (255, 255, 0)
preto = (0, 0, 0)

class Pacman:
    def __init__(self):
        self.coluna = 1
        self.linha = 1
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = 800 // 30
        self.raio = self.tamanho // 2
        self.vel_x = 1
        self.vel_y = 1
        
    def calcular_regras(self):
        self.coluna += self.vel_x
        self.linha += self.vel_y
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)
        
        if self.centro_x + self.raio > 800:
            self.vel_x = -1
        if self.centro_x - self.raio < 0:
            self.vel_x = 1 
        if self.centro_y + self.raio > 600:
            self.vel_y = -1
        if self.centro_y - self.raio < 0:
            self.vel_y = 1 
        
    def pintar(self, tela):
        # Desenhar corpo do pacman
        pygame.draw.circle(tela, amarelo, (self.centro_x, self.centro_y), self.raio)
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, preto, pontos, 0)
        
        olho_x = int(self.centro_x + self.raio / 3)
        olho_y = int(self.centro_y - self.raio * 0.70)
        olho_raio = int(self.raio / 10)
        pygame.draw.circle(tela, preto, (olho_x, olho_y), olho_raio, 0)
        
if __name__ == "__main__":
    pacman = Pacman()
    
    while True:
        # Calcular as regras
        pacman.calcular_regras()
        
        # Pintar a tela
        screen.fill(preto)
        pacman.pintar(screen)
        pygame.display.update()
        pygame.time.delay(50)
        
        # Captura os eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()