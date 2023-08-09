# A função enumerate itera sobe estrutura de dados
# como listas, tuplas ou objetos iteraveis
# O retorno: é um objeto enumerado, dando indices aos valores

my_list = ['apples', 'pears', 'oranges', 'fruits']

# Consigo acessar tanto o indices como o valor
for x, element in enumerate(my_list):
    print(x, element)
