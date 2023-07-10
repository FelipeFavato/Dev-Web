class Ventilador:
    def __init__(self, cor, voltagem):
        self.cor = cor
        self.voltagem = voltagem
        self.preco = 150
        self.velocidade = 0
        self.velocidade_maxima = 3
        self.ligado = False
