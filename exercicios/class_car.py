class Carro:
    def __init__(self, modelo: str, ano: int, velocidade: int) -> None:
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade

    def acelerar(self, value):
        self.velocidade += value

    def desacelerar(self, value):
        self.velocidade -= value

    def __str__(self):
        return f'{self.modelo} | {self.ano}'
