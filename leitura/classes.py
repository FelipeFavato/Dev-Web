class Pessoa:
    def diz_nome_e_idade(self, idade: int) -> None:
        print(f"{self.nome} tem {idade} anos.")


maria = Pessoa()
maria.nome = "Maria"
maria.diz_nome_e_idade(20)  # saída: Maria tem 20 anos.

jorge = Pessoa()
jorge.nome = "Jorge"
jorge.diz_nome_e_idade(28)  # saída: Jorge tem 28 anos.


joao = Pessoa()

# Atribuo o valor "João" a um atributo chamado `nome` dentro do objeto `joao`
joao.nome = "João"
print(joao.nome)  # saída: joao
