class Funcionario:
    def __init__(self, nome: str, projeto: str, salario: float) -> None:
        self.nome = nome  # Publico
        self._projeto = projeto  # Protegido: Acessivel classe e subclasses
        self.__salario = salario  # Privado: Acessivel dentro da classe
        # Como burlar o acesso a atributos privados = name mangling


class Liquidificador:
    def __init__(self, cor: str, potencia: str,
                 tensao: str, preco: str) -> None:
        self.preco = preco
        self.cor = cor
        self._potencia = potencia
        self._tensao = tensao
        self.__ligado = False
        self.__velocidade = 0
        self.__velocidade_maxima = 3
        self.__corrente_atual_no_motor = 0

    def ligar(self, velocidade: int) -> None:
        if velocidade > self.__velocidade_maxima or velocidade < 0:
            raise ValueError(
                f"Velocidade deve estar entre 0 e {self.__velocidade_maxima}"
            )

        self.__velocidade = velocidade
        self.__corrente_atual_no_motor = (
            (self._potencia / self._tensao) / self.__velocidade_maxima
        ) * velocidade
        self.__ligado = True

    def desligar(self):
        self.__ligado = False
        self.__velocidade = 0

    def esta_ligado(self):
        return self.__ligado


class LiquidificadorDaora:
    # Getter
    @property
    def cor(self):
        return self.__cor.upper()

    @cor.setter  # Repare que é @cor.setter, e não @property.setter
    def cor(self, nova_cor: str) -> str:
        if nova_cor.lower() == "turquesa":
            raise ValueError("Não existe liquidificador turquesa")

        self.__cor = nova_cor

    def __init__(self, cor: str, potencia: str,
                 tensao: str, preco: str) -> None:
        # Observe que usamos o setter para já validarmos o primeiro valor:
        # usamos self.cor, que chama o setter, e não self.__cor que manipula
        # o atributo diretamente
        self.cor = cor

        # Demais variáveis omitidas para este exemplo


liquidificador = Liquidificador("Rosa", "110", "127", "200")

print(liquidificador.cor)  # ROSA
liquidificador.cor = "Vermelho"
print(liquidificador.cor)  # VERMELHO


# exercicio 7
class GastoMensal:
    def __init__(self, internet, supermercado, luz, agua, aluguel):
        self.internet = internet
        self.supermercado = supermercado
        self._luz = luz
        self._agua = agua
        self.__aluguel = aluguel

    @property
    def luz(self):
        return self._luz.upper()

    @property
    def agua(self):
        return self._agua.upper()

    @luz.setter  # Repare que é @luz.setter, e não @property.setter
    def cor(self, nova_luz):
        self._luz = nova_luz

    @agua.setter
    def agua(self, nova_agua):
        self._agua = nova_agua
