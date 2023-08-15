# Doctests se baseiam na capacidade de criar exemplos em docstrings
# Doctests são melhores em funções simples e que tenham entradas e saidas
# bem definidas


# Corrigimos nossa função para verificar o tamanho da lista e retornar
# 0 caso seja uma lista vazia (mais recomendável nesse caso).
def mean(numbers):
    """
    Calcula a média de uma lista de números.

    >>> my_list = [1, 2, 3, 4, 5]
    >>> mean(my_list)
    3.0
    >>> mean([2.5, 3.75, 1.25, 4])
    2.875
    >>> mean([])
    0

    """
    # Adicionamos as duas linhas abaixo. O resto continua igual.
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        return 0


# Ajustamos nosso exemplo na docstring para esperar um erro
# (menos recomendável nesse caso, mas será mostrado como fica
# para quando você precisar verificar erros em outros cenários).
def mean_2(numbers):
    """
    Calcula a média de uma lista de números.

    >>> my_list = [1, 2, 3, 4, 5]
    >>> mean_2(my_list)
    3.0
    >>> mean_2([2.5, 3.75, 1.25, 4])
    2.875
    >>> mean_2([])
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero

    """
    return sum(numbers) / len(numbers)
