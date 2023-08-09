def get_repeated(nums):
    # Declara dois sets auxiliares
    seen_before = set()
    repeated = set()

    # Itera sobre a lista de INT passada no parametro
    for num in nums:
        # Se o numero estiver dentro de seen_before
        if num in seen_before:
            # Adiciona em repeated
            repeated.add(num)
        else:
            # Se ainda não estiver dentro de seen_before,
            # adiciona em seen_before
            seen_before.add(num)

    return repeated


if __name__ == '__main__':
    nums = [1, 6, 3, 9, 6, 6, 3, -1, 4, 5, 7, 1]

    print(f'{get_repeated(nums)}')
