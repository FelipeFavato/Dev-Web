# Protocolos são classes que herdam de typing.Protocol –
# e foram introduzidos no Python 3.8
# Eles servem para possibilitar a tipagem estática na verificação estrutural

# Exercicio 3
# Crie um protocolo chamado CalculaPerimetro que contenha um método
# abstrato chamado calcular_perimetro. Crie uma classe chamada Quadrado
# que implemente o protocolo CalculaPerimetro e o método
# calcular_perimetro para calcular o perímetro do quadrado.


from typing import Protocol


class CalculaPerimetro(Protocol):
    def calcular_perimetro(self):
        pass


class Quadrado(CalculaPerimetro):
    def __init__(self, lado: int) -> None:
        self.lado = lado

    def calcular_perimetro(self):
        return f"O perímetro do quadrado é de {self.lado * 4} cm"


quadrado = Quadrado(5)
print(quadrado.calcular_perimetro())

# Quando executamos o mypy no código a seguir, recebemos o erro error:
# Cannot instantiate abstract class "Triangulo" with abstract attribute
# "calcular_perimetro" [abstract]. Corrija-o para que o mypy retorne
# a mensagem de sucesso.


class Triangulo(CalculaPerimetro):
    def __init__(self, lado1: int, lado2: int, lado3: int) -> None:
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_perimetro(self):
        return f"O perímetro do triângulo é de {self.lado1 + self.lado2 + self.lado3} cm"


triangulo = Triangulo(5, 5, 5)
print(triangulo.calcular_perimetro())
