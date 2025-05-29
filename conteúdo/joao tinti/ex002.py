class Cachorros:
    def __init__(self, nome,  cor, idade, tamanho):
        self.nome = nome
        self.cor = cor
        self.idade = idade
        self.tamanho = tamanho
    def latir(self):
        print("au au")
    def correr(self):
        print(f"{self.nome} está correndo")

cachorro1 = Cachorros("Gui", "Preto", 25, "Anão")
# print(cachorro1.nome, cachorro1.cor, cachorro1.idade, cachorro1.tamanho)
cachorro1.idade = 10
cachorro1.latir()
cachorro1.correr()