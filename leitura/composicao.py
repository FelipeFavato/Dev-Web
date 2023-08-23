# Composição é atribuir o objeto de uma classe a um atributo
# da outra, gerando, assim, um relacionamento de pertencimento entre elas.
class Liquidificador:
    pass


class Pessoa:
    def __init__(self, nome: str, saldo_na_conta: float) -> None:
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.liquidificador: Liquidificador | None = None

    def comprar_liquidificador(self, liquidificador: Liquidificador) -> None:
        if liquidificador.preço <= self.saldo_na_conta:
            self.saldo_na_conta -= liquidificador.preço
            self.liquidificador = liquidificador

# É importante chamar a atenção para, quando possível, prefira utilizar
# composição ao invés de herança. Usamos herança quando queremos criar
# um subtipo de algo e composição em qualquer outra situação (por exemplo,
# expandir alguma funcionalidade sem haver uma relação de especialização).
