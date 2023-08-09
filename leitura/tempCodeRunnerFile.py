# Podemos instanciar um set vazio ou inicializar com valores de um objeto
# iterável, como uma lista
conjunto_a = set()

# Ao inicializar com valores de uma lista, os valores duplicados serão
# desconsiderados e a ordem de inserção será perdida.
conjunto_b = set([1, 1, 2, 3, 3, 3])
# print(conjunto_b) -> saída {1, 2, 3}

# Add - adiciona o elemento ao conjunto
conjunto_a.add(5)
conjunto_a.add(3)
conjunto_a.add(0)
# print(conjunto_a) saida {0, 3, 5}

# sets admitem objetos mistos. Ou seja, admitem ter _strings_ com _ints_
# dentro de um mesmo objeto, por exemplo.
conjunto_a.add('elemento')
print(conjunto_a)