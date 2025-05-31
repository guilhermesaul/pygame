import pygame
import os

pygame.init()
class Sapo(pygame.sprite.Sprite):
    def __init__(self,):
        super().__init__()
        self.sprites = []
        self.caminhos = [
            os.path.join(os.path.dirname(__file__), "images", "attack_1.png"),
            os.path.join(os.path.dirname(__file__), "images", "attack_2.png"),
            os.path.join(os.path.dirname(__file__), "images", "attack_3.png"),
            os.path.join(os.path.dirname(__file__), "images", "attack_4.png"),
            os.path.join(os.path.dirname(__file__), "images", "attack_5.png"),
            os.path.join(os.path.dirname(__file__), "images", "attack_6.png"),
            os.path.join(os.path.dirname(__file__), "images", "attack_7.png"),
            os.path.join(os.path.dirname(__file__), "images", "attack_8.png"),
            os.path.join(os.path.dirname(__file__), "images", "attack_9.png"),
            os.path.join(os.path.dirname(__file__), "images", "attack_10.png"),
            ]
        
        self.sprites.append(pygame.image.load(self.caminhos[0]))
        self.sprites.append(pygame.image.load(self.caminhos[1]))
        self.sprites.append(pygame.image.load(self.caminhos[2]))
        self.sprites.append(pygame.image.load(self.caminhos[3]))
        self.sprites.append(pygame.image.load(self.caminhos[4]))
        self.sprites.append(pygame.image.load(self.caminhos[5]))
        self.sprites.append(pygame.image.load(self.caminhos[6]))
        self.sprites.append(pygame.image.load(self.caminhos[7]))
        self.sprites.append(pygame.image.load(self.caminhos[8]))
        self.sprites.append(pygame.image.load(self.caminhos[9]))
        
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (128*3, 64*3))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100
        
        self.animar = False
        
    def atacar(self):
        self.animar = True
        
    def update(self):
        if self.animar:
            self.atual += 0.5
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (128*3, 64*3))

largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))

todas_as_sprites = pygame.sprite.Group()
sapo = Sapo()
todas_as_sprites.add(sapo)
relogio = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            sapo.atacar()
            
    tela.fill((0, 0, 0))
    relogio.tick(30)
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    
    pygame.display.flip()