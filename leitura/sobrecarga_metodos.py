class Pessoa:
    # exemplo de classe com atributos opcionais, se não forem passados
    # serão inicializados como None
    def __init__(self, nome, idade=None, saldo_na_conta=None):
        self.nome = nome
        self.idade = idade
        self.saldo_na_conta = saldo_na_conta
        self.brinquedos = []


# Sobrescirta de metodos -> Apaga tudo e reescreve
class Liquidificador(Eletrodomestico):
    def esta_ligado(self):
        return False


# Super - Incrementa novas funcionalidades
class Liquidificador1(Eletrodomestico):
    def esta_ligado(self):
        return "Sim" if super().esta_ligado() else "Não"
