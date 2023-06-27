def mediaAritmetica(list: list) -> int:
    total = 0
    for value in list:
        total += value

    return total / len(list)


print(mediaAritmetica([5, 3, 4, 10]))
