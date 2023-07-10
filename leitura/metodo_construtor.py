# O método construtor é um metodo especial que roda automaticamente
# quando o objeto é instanciado - Sendo dividido em duas etapas:
# __new__ - construtor => Cria e retorna uma nova instancia de classe
# __init__ - inicializador
# __qualquerNome__ => Permite que instancias da classe interajam
# com as funções nativas do python


class Exemplo:
    def __init__(self):
        print('Inicializando Exemplo')
        self._privado = 'Eu sou privado'

    # Asterisco => Permite passar um numero variável de argumentos
    # *args => Argumentos sao passados como TUPLA
    # **kwargs => Argumentos sao passados como DICT
    def __new__(cls, *args, **kwargs):
        print('Criando uma nova instancia de Exemplo')
        instance = super().__new__(cls)
        return instance

    def __metodo_privado(self):
        print('Este é um metodo privado')

    def metodo_publico(self):
        print('Este é um metodo publico')
        self.__metodo_privado()


exemplo = Exemplo()
exemplo.__metodo_privado()
