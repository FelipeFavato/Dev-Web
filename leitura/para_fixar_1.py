# Retorna um número que é o resultado da multiplicação dos elementos do array
def multiply_array(numbers):
    result = 1
    for number in numbers:
        result *= number

    return result


print(multiply_array([1, 2, 3, 4]))
# Complexidade de tempo? O(n)
# Complexidade de espaço? O(1)
