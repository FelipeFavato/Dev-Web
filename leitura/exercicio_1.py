class Conjunto:
    def __init__(self):
        # Inicializou uma lista com 1001 posições e todas com valor False
        # 0 --- 1000
        self.set = [False] * 1001
        # Inicializou uma variável que guarda a posição do maior
        # elemento inserido até o momento
        self.last_element = 0

    def __str__(self):
        # Inicia uma variável auxiliar começando com '{'
        string = '{'

        # Acessa o index e o valor do set
        for index, is_in_set in enumerate(self.set):
            # Se is_in_set for um valor diferente de False
            if is_in_set:
                # Adiciona na variavel string o index, transformando-o em STR
                string += str(index)
                # Se index for menor do que a posição do ultimo elemento:
                if index < self.last_element:
                    # Adiciona uma virgula logo após o index adicionado acima
                    string += ", "

        # Adiciona ao final dessa variável '}'
        string += '}'
        return string

    def add(self, item):
        # Se o valor na posição[item] dentro do set nao existir,
        # ou se for False: Transforma esse valor em True
        if not self.set[item]:
            self.set[item] = True
        # Se o item for maior do que o last_element, então atualiza
        # o valor do last_element com o valor do item
        if item > self.last_element:
            self.last_element = item

    def __contains__(self, item):
        # Retorna o valor na posição[item] - Vai ser True ou False
        return self.set[item]

    def union(self, conjunto_b):
        # Instancia um novo conjunto
        new_conjunto = Conjunto()

        # Cria um range do tamanho do set da classe e itera em seu indice
        for index in range(1001):
            # Se o valor for True ou pra UM ou pro OUTRO
            if self.set[index] or conjunto_b.set[index]:
                # Então adiciona esse valor no novo conjunto
                new_conjunto.add(index)

        return new_conjunto

    # Mesma ideia da uniao, mas agora ambos devem conter o valor True
    def intersection(self, conjunto_b):
        new_conjunto = Conjunto()

        for index in range(1001):
            if self.set[index] and conjunto_b.set[index]:
                new_conjunto.add(index)

        return new_conjunto

    def difference(self, conjunto_b):
        # Instancia um novo conjunto
        new_conjunto = Conjunto()

        # Itera sobre os indices de um range(1001) criado para auxiliar
        for index in range(1001):
            # Caso os valores sejam diferentes, adiciona no novo conjunto
            # Caso seja True em UM e False no OUTRO: adiciona
            if self.set[index] and not conjunto_b.set[index]:
                new_conjunto.add(index)

        return new_conjunto

    def issubset(self, conjunto_b):
        for index in range(1001):
            # Se tiver no conjunto_a e não tiver no conjunto_b
            # retorna False, pois CONJ_A não sera um subset de CONJ_B
            if self.set[index] and not conjunto_b[index]:
                return False

        return True

    def issuperset(self, conjunto_b):
        for index in range(1001):
            # Se tiver no CONJ_B e nao tiver no CONJ_A,
            # retorn False, pois CONJ_A não sera um superset de CONJ_B
            if conjunto_b.set[index] and not self.set[index]:
                return False

        return True


if __name__ == "__main__":

    conjunto = Conjunto()
    conjunto.add(0)
    conjunto.add(10)
    conjunto.add(100)
    conjunto.add(1000)
    print(conjunto)
