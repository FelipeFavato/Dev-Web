def fibonacci(num):  # nome da função e parâmetro
    if (num <= 1):  # condição de parada
        return num
    else:
        # chamada de si mesma com um novo valor
        return fibonacci(num - 2) + fibonacci(num - 1)
