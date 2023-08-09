list_a = [1, 3, 4, 3, 5, 1]
list_b = [2, 9, 4, 5, 9, 2]

# Criar um conjunto
set_a = {}
# print(type(set_a)) -> saida <class 'dict'>
set_b = set()
# print(type(set_b)) -> saida <class 'set'>


# Transformar lista em conjunto
set_a = set(list_a)
set_b = set(list_b)
# print(set_a)  # -> saida {1, 3, 4, 5}
# print(set_b)  # -> saida {9, 2, 4, 5}


# Operações com conjuntos
print(set_a.union(set_b))  # {1, 2, 3, 4, 5, 9}
print(set_b.union(set_a, {10, 11, 12}))  # {1, 2, 3, 4, 5, 9, 10, 11, 12}
print(set_a.intersection(set_b))  # {4, 5}
print(set_a.difference(set_b))  # {1, 3}
print(set_b.difference(set_a))  # {2, 9}


# Operações de comparação
print(set_a == set_b)  # False
print({1, 2, 3, 4} > {2, 3})  # True => testa se é subset
