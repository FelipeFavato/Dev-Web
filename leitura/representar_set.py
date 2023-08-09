# Representando sets

# Vetores
# Inicia todos os vetores zerados, de 0 a N. Sendo tudo falso
# Só guarda valores pequenos
# Só guarda INT
# Se os numeros forem muitos esparsos, usa muita memória
# False True True True False
A = {1, 2, 3}

B = [False for i in range(5)]
B[1] = True
B[2] = True
B[3] = True

# Hashmaps - DICT

C = {1: True, 2: True, 3: True}
print(1 in C)  # Dentro do set C, eu tenho a chave 1?
