# A abstração de dados é outro pilar da orientação a objetos,
# que oculta os detalhes da implementação mostrando apenas a
# funcionalidade para quem acessa os métodos, a fim de reduzir
# a complexidade do código.

class Animal:
    def __init__(self, nome, raca, pelagem) -> None:
        self.nome = nome
        self.raca = raca
        self.pelagem = pelagem

    def banho(self):
        pass

    def tosa(self):
        pass

    def unhas(self):
        pass


# Exercicio 5
class Retangulo:
    def __init__(self, base: int, altura: int):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return (self.base + self.altura) * 2


retang = Retangulo(5, 10)
print(retang.area())
print(retang.perimetro())
