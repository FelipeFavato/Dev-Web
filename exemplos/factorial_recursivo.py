def factorial(n):
    if n <= 1:  # caso base
        return 1
    else:
        return n * factorial(n - 1)  # caso recursivo


factorial(3)
