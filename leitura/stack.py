class Stack():
    def __init__(self):
        self._data = list()

    # Retorn o tamanho (len)
    def size(self):
        return len(self._data)

    # True = vazia /// False = não-vazia
    def is_empty(self):
        return not bool(self.size())

    # Insere um elemento ao topo da pilha
    def push(self, value):
        self._data.append(value)

    # Remove o elemento mais ao topo da pilha
    def pop(self):
        # Se a pilha estiver vazia, retorne None
        if self.is_empty():
            return None

        # -1 se refere ao último objeto da pilha.
        # Ou seja, o valor do topo da pilha
        value = self._data[-1]
        del self._data[-1]
        return value

    # Acessa o ultimo elemento da pilha
    def peek(self):
        if self.is_empty():
            return None
        value = self._data[-1]
        return value

    # Esvazia a pilha
    def clear(self):
        self._data.clear()

    def __str__(self):
        str_items = ""
        for i in range(self.size()):
            value = self._data[i]
            str_items += str(value)
            if i + 1 < self.size():
                str_items += ", "

        return "Stack(" + str_items + ")"


if __name__ == "__main__":
    elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    content_stack = Stack()

    for elem in elements:
        content_stack.push(elem)

    # saída: Stack(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(content_stack)
    # saída: 10
    print(content_stack.size())

    # saída: 10
    print(content_stack.peek())
    # saída: 10, pois a função retorna o elemento que está sendo retirado
    print(content_stack.pop())

    # saída: 9, pois, após o 10 ter sido removido, o 9 se tornou o elemento do topo da pilha
    print(content_stack.peek())
    # saída: 9
    print(content_stack.size())

    # saída: None, pois a função não retorna nada!
    print(content_stack.clear())
    # saída: 0
    print(content_stack.size())
