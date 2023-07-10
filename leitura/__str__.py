class Pet:
    def __init__(self, nome, especie, idade, humano):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.humano = humano

    def __str__(self):
        return f"""
- Espécie: {self.especie}
- Nome: {self.nome}
- Dono: {self.humano}
        """


thor = Pet('Thor', 'Gato', 5, 'Felps')


print(thor)
