# Escreva uma função que recebe uma lista de strings e
# um caractere e retorna uma lista com as strings que
# começam com o caractere fornecido.

# Exemplo:
animais = ["cachorro", "gato", "elefante", "girafa"]
caractere = "g"

resultado = ["gato", "girafa"]


def filter_list(lista: list[str], char: str) -> list[str]:
    new_list = []
    for item in lista:
        if item[0] == char:
            new_list.append(item)

    return new_list
