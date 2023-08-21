# Em python, esta operação é dividida em dois métodos:

# __new__ (Construtor)
# __init__ (Inicializador)


class Liquidificador:
    def __init__(
        self,
        cor: str,
        potência: int,
        tensão: int,
        preço: float | int
    ) -> None:
        # Adiciona o valor do parâmetro `cor` a um
        # atributo de mesmo nome (homônimo)
        # do objeto que está sendo criado (`self.cor`).
        self.cor = cor
        self.preço = preço
        self.potência = potência
        self.tensão = tensão

        # Valores _hard coded_
        # São criados assim, nao da para passar por pametro
        # no momento de instanciação do objeto
        self.ligado = False
        self.velocidade = 0
        self.velocidade_máxima = 3
        self.corrente_atual_no_motor = 0

# Agora, podemos criar nossos primeiros liquidificadores.
# Os argumentos nos parênteses são passados para o `__init__`


meu_liquidificador = Liquidificador("Azul", 200, 127, 200)
seu_liquidificador = Liquidificador(
    cor="Vermelho", potência=250, tensão=220, preço=100
)
