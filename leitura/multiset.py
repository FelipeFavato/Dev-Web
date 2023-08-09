# python3 -m leitura.multiset
from multiset import Multiset

print(Multiset())
# {}
print(Multiset('aeiou'))
# {a, e, i, o, u}
print(Multiset({'a': 1, 'b': 2, 'c': 3, 'o': 4}))
# {a, b, b, c, c, c, o, o, o, o}
