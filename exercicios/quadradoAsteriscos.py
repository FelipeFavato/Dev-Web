def printAsteriscos(size: int) -> str:
    str = '*' * size + '\n'
    return str * size


print(printAsteriscos(10))


def draw_square(n):
    for row in range(n):
        print(n * '*')
