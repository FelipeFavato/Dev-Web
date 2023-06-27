name_list = ['José', 'Lucas', 'Nádia', 'Fernanda', 'Cairo', 'Joana']


def find_biggest_name(list: list) -> str:
    biggest_name = list[0]
    for name in list:
        if len(name) > len(biggest_name):
            biggest_name = name
    return biggest_name


print(find_biggest_name(name_list))
