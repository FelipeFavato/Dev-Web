class Node:
    def __init__(self, value):
        self.value = value  # 🎲 Dado a ser armazenado
        self.next = None  # 👉 Forma de apontar para outro nó

    def __str__(self):
        return f"""Node(value = {self.value}, next = {self.next})"""


class Lista:
    def __init__(self):
        # O head_value acaba sendo todo o encadeamento de nós
        self.head_value = None
        self.__length = 0

    def __str__(self):
        card = f"""
        ---------------------------
        |    Lista
        ---------------------------
        | Encadeamento - {self.head_value}
        | length - {self.__length}
        ---------------------------"""

        return card

    def __len__(self):
        return self.__length

    def insert_first(self, value):
        # O first_value instancia a classe Node
        first_value = Node(value)
        # O atributo next do objeto first_value recebe o valor None
        first_value.next = self.head_value
        # O atributo head_value desta classe recebe o objeto first_value
        self.head_value = first_value
        # Incrementa 1 no len do array
        self.__length += 1

    def insert_last(self, value):
        # O last_value instancia a classe Node
        last_value = Node(value)
        # Variável auxiliar armazena o valor de head_value
        current_value = self.head_value

        # Caso a lista esteja vazia, só chama a função insert_first
        if self.is_empty():
            return self.insert_first(value)

        # Enquanto existir current_value.next | self.head_value.next
        while current_value.next:
            # Não entendi essa passagem 100%
            current_value = current_value.next
        # Assim que o next for None, eu adiciono o ultimo valor nesse next
        current_value.next = last_value
        # Incrementa 1 no len do array
        self.__length += 1

    def insert_at(self, value, position):
        ...

    def remove_first(self):
        # Variável auxiliar que armazena o valor do head
        value_to_be_removed = self.head_value
        # Caso exista um value_to_be_removed
        if value_to_be_removed:
            # Atribui o próximo valor ao valor de head_value,
            # 'trazendo todos uma casa para tras'
            self.head_value = self.head_value.next
            # Transforma o next do value_to_be_removed em None,
            # para retornar apenas o valor
            value_to_be_removed.next = None
            # Decrementa 1 do len do array
            self.__length -= 1
        # Retorna o node removido | head_value
        return value_to_be_removed

    def remove_last(self):
        # Caso a length da Lista seja menor ou igual a 1
        if len(self) <= 1:
            # Chama a função de remover o primeiro
            return self.remove_first()

        # Variável auxiliar recebe o valor do encadeamento de nós
        previous_to_be_removed = self.head_value
        #  Enquanto existir 2 Nodes após o primeiro
        while previous_to_be_removed.next.next:
            # O encadeamento de nós armazenado aqui, receberá
            # o valor do próximo nó
            previous_to_be_removed = previous_to_be_removed.next

        # Assim que não tiver mais dois next's, o value_to_be_removed
        # receberá o valor do ultimo nó
        value_to_be_removed = previous_to_be_removed.next
        # Então esse ultimo nó terá seu .next = None
        previous_to_be_removed.next = None
        # Decrementa 1 do len da lista
        self.__length -= 1
        # Retorna o nó removido
        return value_to_be_removed

    def remove_at(self, position):
        # Caso a posição seja menor do que 1
        if position < 1:
            # Remove o primeiro
            return self.remove_first()
        # Caso a posição seja maior ou igual ao tamanho da lista
        if position >= len(self):
            # Remove o ultimo
            return self.remove_last()

        # Armazena o valor do encadeamento de nós na variável
        previous_to_be_removed = self.head_value

        # Enquanto a posição for maior do que 1
        while position > 1:
            # Atribui o valor do encadeamento de nós menos o
            # primeiro nó a variável auxiliar e assim vai indo até
            # chegar no nó escolhido
            previous_to_be_removed = previous_to_be_removed.next
            # Decrementa 1 na posição
            position -= 1

        # Aqui a variavel previous_to_be_removed vai ser a (posição
        # desejada - 1). Então pega o próximo nó e atribui a variável
        # value_to_be_removed
        value_to_be_removed = previous_to_be_removed.next
        # Faz com que o elemento que se quer deletar seja todos os
        # proximos nós dele
        previous_to_be_removed.next = value_to_be_removed.next
        value_to_be_removed.next = None

        # Decrementa 1 no len da lista
        self.__length -= 1

        return value_to_be_removed

    def get_element_at(self, position):
        # Declara variável value_returned
        value_returned = None
        # Armazena o encadeamento de nós
        value_to_be_returned = self.head_value
        # Caso exista o encadeamento de nós
        if value_to_be_returned:
            # Enquanto a posição for maior que 0 e existir o next
            while position > 0 and value_to_be_returned.next:
                # Vai pegando o proximo valor
                value_to_be_returned = value_to_be_returned.next
                position -= 1
            if value_to_be_returned:
                value_returned = Node(value_to_be_returned.value)
            return value_returned

    def __get_node_at(self, position):
        value_to_be_returned = self.head_value
        if value_to_be_returned:
            while position > 0 and value_to_be_returned.next:
                value_to_be_returned = value_to_be_returned.next
                position -= 1
        return value_to_be_returned

    def clear(self):
        # Enquanto nao estiver vazio
        while not self.is_empty():
            # Remova o primeiro
            self.remove_first()

    def is_empty(self):
        # Retorna True ou False condicionado pelo length
        return not self.__length


lista = Lista()
lista.insert_first(2)
lista.insert_last(5)
lista.insert_first(1)
lista.insert_first(3)

print('head_value: ', lista.head_value)
print(lista.remove_at(2))
print(lista)
lista.clear()
print(lista)
