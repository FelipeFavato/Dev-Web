# Crie as classes Motocicleta e Caminhao e inicialize
# as duas com o atributo velocidade_maxima.

class Motocicleta:
    def __init__(self, velocidade_maxima: int) -> None:
        self.velocidade_maxima = velocidade_maxima


class Caminhao:
    def __init__(self, velocidade_maxima: int) -> None:
        self.velocidade_maxima = velocidade_maxima


#  Utilize as classes criadas no exercício anterior para
# criar uma função print_velocidade_maxima que recebe um
# objeto e imprime a velocidade máxima dele. Retorne uma
# mensagem de erro com um TypeError caso o veículo passado
# como argumento não seja uma motocicleta.


def print_velocidade_maxima(veiculo: int) -> None:
    if isinstance(veiculo, Motocicleta):
        print(f"A velocidade máx do veículo é de {veiculo.velocidade_maxima}")
    else:
        raise TypeError("O objeto precisa ser uma motocicleta")
