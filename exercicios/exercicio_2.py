# Em um jogo de baralho, as cartas estão representadas
# por um array numérico. Para iniciar o jogo, devemos
# embaralhar as cartas. Faremos isto dividindo uma porção
# de cartas em 2 e depois mesclando as duas porções. Por exemplo:
# Exemplo 1:
cartas = [2, 6, 4, 5]
# cartas por parte = 2

# resultado = [2, 4, 6, 5]

# Exemplo 2:
cartas_2 = [1, 4, 4, 7, 6, 6]
# cartas por parte = 3

# resultado = [1, 7, 4, 6, 4, 6]

# Processo
# cartas = [2, 6, 4, 5]
# separaçao => [2, 6]   [4, 5]
# junçao => [2, 4, 6, 5]


def first_array(array):
    index = 0
    first = []
    while index < int(len(array) / 2):
        first.append(array[index])
        index += 1
    return first


def second_array(array):
    index = int(len(array) / 2)
    second = []
    while index <= len(array) - 1:
        second.append(array[index])
        index += 1
    return second


def shuffle(array):
    first = first_array(array)
    second = second_array(array)
    shuffled_array = []
    index = 0
    while index < len(first):
        shuffled_array.append(first[index])
        shuffled_array.append(second[index])
        index += 1
    return shuffled_array


print(shuffle(cartas))
print(shuffle(cartas_2))
