from stack import Stack


def solve_expression(expr):
    # Instancia a classe Stack
    stack = Stack()
    # Cria um array, separando os itens por espaço
    # ['5', '10', '+', '3', '*']
    tokens_list = expr.split(' ')

    for token in tokens_list:
        if token == '+':
            # Sum operation
            result = stack.pop() + stack.pop()
            print(result)
            stack.push(result)
        elif token == '*':
            # multiply operation
            result = stack.pop() * stack.pop()
            stack.push(result)
        else:
            # add the number operation
            stack.push(int(token))

    return stack.pop()


print(solve_expression("5 10 + 3 *"))
print(("5 10 + 3 *").split(' ').pop())
