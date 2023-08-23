from typing import Any


class Eletrodoméstico:
    def __init__(
        self,
        cor: str,
        potência: int,
        tensão: int,
        preço: float | int
    ) -> None:
        self.cor = cor
        self.preço = preço
        self.potência = potência
        self.tensão = tensão
        self.velocidade_máxima = 3

        # Inicia os valores de `corrente_atual_no_motor`, `velocidade` e
        # `ligado` chamando o método `desligar` direto no construtor
        self.desligar()

    def ligar(self, velocidade: int) -> None:
        if velocidade > self.velocidade_máxima or velocidade < 0:
            raise ValueError(
                f"Velocidade deve estar entre 0 e {self.velocidade_máxima}"
            )

        self.velocidade = velocidade
        self.ligado = True

        corrente_máxima = self.potência / self.tensão
        velocidade_percentual = velocidade / self.velocidade_máxima
        self.corrente_atual_no_motor = corrente_máxima * velocidade_percentual

    def desligar(self) -> None:
        self.ligado = False
        self.velocidade = 0
        self.corrente_atual_no_motor = 0


class Liquidificador(Eletrodoméstico):
    pass


# Exemplo


class Pai:
    def faz_algo(self, valor: Any) -> None:
        print(valor)


class Filha(Pai):
    def faz_outra_coisa(self) -> None:
        print("Método da classe Pai")

        # Chama o método da superclasse `Pai` passando o `self`
        # explicitamente
        # Chama a classe Pai.metodo() e passando self como parametro
        Pai.faz_algo(self, valor=1)
        # Não precisou chamar o self dentro dos parametros
        super().faz_algo(valor=1)


# Método da classe Pai
# 1


# Exemplo video
class Animal:
    def __init__(self, especie: str, cor: str):
        self.especie = especie
        self.coloracao = cor

    def comer(self, comida: str):
        return f'O animal da especie {self.especie} esta comendo {comida}'


class Gato(Animal):
    def __init__(self, cor: str, tem_bigode: bool, num_de_patas: int):
        super().__init__("Gato", cor)
        self.bigode = tem_bigode
        self.patas = num_de_patas

    def miar(self):
        return 'Miauu!!'


gato = Gato('Laranja', True, 4)


# Exercicio 1
class Vehicle:
    def __init__(self, name: str, capacity: int) -> None:
        self.name = name
        self.capacity = capacity

    def move(self, distance: int):
        return f"""{self.name} carried {self.capacity} people
        across {distance} kilometers."""


class Car(Vehicle):
    def __init__(self, capacity):
        super().__init__('Carro', capacity)

    def move(self, distance):
        print(super().move(distance))


# carro = Car(5)
# carro.move(100)


class Motorcycle(Vehicle):
    def __init__(self, capacity):
        super().__init__('Moto', capacity)

    def move(self, distance):
        print(super().move(distance))


# moto = Motorcycle(2)
# moto.move(20)


# exercicio 2
class Contact:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email


class ContactList:
    def __init__(self) -> None:
        self.contacts = []
        self.favorites = []

    def add_contact(self, contact: Contact):
        self.contacts.append(contact)

    def _find_contact(self, name: str, from_favorites=False) -> Contact:
        contact_list = self.favorites if from_favorites else self.contacts

        try:
            contact = [c for c in contact_list if c.name == name][0]
        except IndexError:
            raise LookupError(f"Contact named {name} not found")

        return contact

    def remove_contact(self, name: str) -> Contact:
        contact = self._find_contact(name)
        self.contacts.remove(contact)
        return contact

    def add_to_favorites(self, name: str) -> None:
        contact = self._find_contact(name)
        self.contacts.remove(contact)
        self.favorites.append(contact)

    def remove_from_favorites(self, name: str) -> None:
        contact = self._find_contact(name, from_favorites=True)
        self.favorites.remove(contact)
        self.contacts.append(contact)


# Exercicio 3
class Animal:
    def __init__(self, nome: str):
        self.nome = nome

    def fazer_som(self):
        return "Animal fazendo som"


class Mamifero(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def amamentar(self):
        return 'Glub Glub'


class MixinVelocidadeCorrida:
    def corrida(self):
        print('Correndo rapidao')


class Cachorro(Mamifero, MixinVelocidadeCorrida):
    def __init__(self, nome):
        super().__init__(nome)

    def latir(self):
        return 'Au au!'


dog = Cachorro('auau')
dog.corrida()
