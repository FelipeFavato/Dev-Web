class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.__altura = altura
        self.__peso = peso

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, nova_altura):
        self.__altura = nova_altura

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, novo_peso):
        self.__peso = novo_peso


Felipe = Pessoa('Felipe', 25, 1.83, 90)

print(Felipe.nome, Felipe.idade)

print(Felipe.altura, Felipe.peso)

Felipe.altura = 1.80

print(Felipe.altura)
