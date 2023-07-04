def countdown(n):
    if n == 0:  # Condição de parada / caso base
        print('Fim!')
    else:
        print(n)
        countdown(n - 1)


countdown(5)

# Nome da função e parâmetro:
#     Condição de parada

#     Chamada de si mesma
