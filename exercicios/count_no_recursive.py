def evenInt(n: list[int]):
    total = 0
    for number in n:
        if number % 2 == 0:
            total += 1
    return total


print(evenInt([1, 2, 3, 4, 5, 6, 7, 8, 9]))
