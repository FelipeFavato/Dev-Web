name_list = ['José', 'Lucas', 'Nádia', 'Fernanda', 'Cairo', 'Joana']


def biggestName(list: list) -> str:
    biggestName = ''
    for name in list:
        if (len(name) > len(biggestName)):
            biggestName = name
    return biggestName


print(biggestName(name_list))
