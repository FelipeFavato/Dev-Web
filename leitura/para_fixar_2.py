# Cria uma classe Carro e, depois, atribua
# valores aos atributos marca, modelo, ano e cor.


class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def info(self):
        return f"""meu carro é um {self.modelo} da marca {self.marca}.
        Ele é do {self.ano} e tem a cor {self.cor}"""


carro_1 = Carro('marca', 'modelo', 'ano', 'cor')


# Com base na classe Carro do exercício anterior, crie um
# método identificar que imprima “Meu carro é um modelo,
# da marca. Ele é do ano e tem a cor cor“.

print(carro_1.info())
