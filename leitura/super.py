class A:
    def faz_algo(self, valor):
        print(valor)


class B(A):
    def faz_outra_coisa(self):
        print('Vou printar o valor pelo metodo criado em A')
        A.faz_algo(self, valor=1)
        # super().faz_algo(valor=1)


b = B()
b.faz_outra_coisa()
