# Lógica que percorre de 1 até o valor máximo de n e retorne ao final uma lista
# contendo os valores de 1 a n
def fizzbuzz(n):
    #  Cria uma lista vazia
    numbers = []
    # Faz um for dos numeros que estao dentro de 1 até N (dentro)
    for number in range(1, n + 1):
        #  Se o numero for divisivel por 15, vira FizzBuzz
        if number % 15 == 0:
            #  Adiciona FizzBuzz
            numbers.append('FizzBuzz')
        elif number % 3 == 0:
            numbers.append('Fizz')
        elif number % 5 == 0:
            numbers.append('Buzz')
        else:
            numbers.append(number)
    return numbers
