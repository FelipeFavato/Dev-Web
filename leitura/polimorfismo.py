import functools
# Polimorfismo é mais um pilar da orientação a objetos,
# que ocorre quando diferentes métodos são chamados pelo mesmo nome.


# Parametros opcionais, escrevendo desse jeitinho nomeado, o segundo parametro
# se torna opcional na hora de chamar a função, pois ele ja tem um
# valor default
def produto(num, other_num=1):
    return num * other_num


# Essa barra no meio dos parametros separa pra gente, onde a gente esta
# obrigando que nossos parametros sejam passados de maneira posicional
# Parametros antes da barra => Não podem ser nomeados
# Parametros depois da barra => Podem ser nomeados
def produtorio(lista, /, inicio=1):
    total = inicio or 1
    for item in lista:
        total *= item
    return total


# O asterisco obriga que eu chame a função com o parametro option de maneira
# nomeada
# Tudo depois do asterisco precisa ser chamado de maneira nomeada
def outra_funcao(a, b, *, option):
    print(option)


outra_funcao(1, 2, option='a')
outra_funcao(1, 2, 'a')


class Pessoa:
    def __init__(self, nome: str, idade=None, saldo_na_conta=None) -> None:
        self.idade = idade
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.brinquedos = []


pessoa_1 = Pessoa("Marcelo", 22, 700)
pessoa_2 = Pessoa("Matheus")
pessoa_3 = Pessoa("Maria", 33)
pessoa_4 = Pessoa("Márcia", saldo_na_conta=100)


# Na verdade, Python até suporta sobrecarga de funções e métodos,
# mas não de maneira transparente e simplificada, e sim por meio
# dos decoradores singledispatch e singledispatchmethod, respectivamente.


@functools.singledispatch  # decorando a função para criar um dispatcher
def func(parâmetro):
    print(parâmetro)


@func.register(int)  # passando um tipo para o registrador do dispatcher
def _(parâmetro):  # observe que o nome da função é irrelevante
    print(parâmetro * 2)


@func.register  # NÃO passando o tipo para o registrador
def _(parâmetro: float):  # mas passando o tipo como type hint
    print(parâmetro * 5)


func(4)  # saída: 8
func(4.0)  # saída: 20.0
func("4")  # saída: 4


# Sobrescrita de metodos
class Eletrodomestico:
    pass


class LiquidificadorLegal(Eletrodomestico):
    def esta_ligado(self):
        return "Sim" if super().esta_ligado() else "Não"


class Liquidificador(Eletrodomestico):
    pass


class Ventilador(Eletrodomestico):
    def __init__(self, cor: str, potencia: str, tensao: str,
                 preco: str, quantidade_de_portas=1) -> None:
        # Chamada ao construtor da superclasse
        super().__init__(cor, potencia, tensao, preco)

        # Faz outras coisas específicas dessa subclasse
        self.quantidade_de_portas = quantidade_de_portas


class Pessoa:
    def __init__(self, nome, saldo_na_conta):
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.eletrodomesticos = []

    # Permite a aquisição de qualquer eletrodoméstico
    def comprar_eletrodomestico(self, eletrodomestico):
        if eletrodomestico.preco <= self.saldo_na_conta:
            self.saldo_na_conta -= eletrodomestico.preco
            self.eletrodomestico.append(eletrodomestico)


# Exercicio 9
class Produto:
    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco

    def descrever(self):
        pass

    def preço(self):
        pass


class Livro(Produto):
    def __init__(self, nome: str, autor: str, preco: float) -> None:
        super().__init__(nome, preco)
        self.autor = autor

    def descrever(self):
        return f"{self.nome} por {self.autor}"

    def preço(self):
        return self.preco


class DVD(Produto):
    def __init__(self, nome: str, diretor: str, preco: float) -> None:
        super().__init__(nome, preco)
        self.diretor = diretor

    def descrever(self):
        return f"{self.nome} dirigido por {self.diretor}"

    def preço(self):
        return self.preco
