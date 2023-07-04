def countdown(n):
    if n == 0:
        print('Fim!')
    else:
        print(n)
        countdown(n - 1)


countdown(5)
