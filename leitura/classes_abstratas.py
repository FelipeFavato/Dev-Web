from abc import ABC, abstractmethod
import abc


class InterfaceFormal(abc.ABC):
    @abc.abstractmethod
    def exemplo(self):
        pass


# class Pessoa(ABC):
#     @abstractmethod
#     def nome(self):
#         pass


# class Vendedor(Pessoa):
#     def __init__(self, seu_nome):
#         self.seu_nome = seu_nome

#     def nome(self):
#         print(f"Seu nome é: {self.seu_nome}")


class X(ABC):
    @abstractmethod
    def exemplo(self):
        print("Classe-base abstrata")


class Y(X):
    def exemplo(self):
        super().exemplo()
        print("Subclasse")


# Exercicio 1
# Crie uma classe abstrata base chamada Pessoa que contenha um método
# abstrato chamado imprimir_cargo. Além disso, crie duas subclasses
# que terão implementações concretas da classe base abstrata. São elas:
# Vendedor e Gerente. O método imprimir_cargo deverá imprimir
# “Meu cargo é de vendedor” e “Meu cargo é de gerente” respectivamente.

class Pessoa(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def imprimir_cargo(self):
        ...


class Vendedor(Pessoa):
    def __init__(self, name):
        super().__init__(name)

    def imprimir_cargo(self):
        print('Meu cargo é vendedor')


class Gerente(Pessoa):
    def __init__(self, name):
        super().__init__(name)

    def imprimir_cargo(self):
        print('Meu cargo é Gerente')
