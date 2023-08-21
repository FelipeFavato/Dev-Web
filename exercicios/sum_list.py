# Escreva uma função que recebe uma lista de inteiros
# e retorna a soma desses valores.


def list_sum(lista: list[int]) -> int:
    count = 0
    for num in lista:
        count += num

    return count


def list_sum_2(lista: list[int]) -> int:
    return sum(lista)


print(list_sum([1, 2, 3, 4, 5]))
print(list_sum_2([1, 2, 3, 4, 5]))
