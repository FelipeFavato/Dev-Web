class Liquidificador:
    def __init__(self, cor: str) -> None:
        self.cor = cor


class Geladeira:
    def __init__(self, cor: str) -> None:
        self.cor = cor


class Fogão:
    def __init__(self, quantidade_de_bocas: int) -> None:
        self.quantidade_de_bocas = quantidade_de_bocas


liq = Liquidificador("preto")
gel = Geladeira("branca")
fog = Fogão(4)
