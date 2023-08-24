# interfaces como o subconjunto dos métodos públicos de um objeto.
class Funcionario:

    def calcular_salario(self):
        raise NotImplementedError(
            "Classes derivadas de Funcionario precisam implementar o cálculo de salário.")


# >>> class Analista(Funcionario):
# ...     pass
# ...
# >>> a = Analista()
# >>> a.calcular_salario()

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 3, in calcular_salario
# NotImplementedError: Classes derivadas de Funcionario precisam
# implementar o cálculo de salário.


# Exercicio 2
# Crie uma interface informal em Python chamada Produto, ela deve
# definir um método abstrato chamado imprimir_preco. Caso o método
# imprimir_preco não seja implementado, lance uma exceção
# NotImplementedError. Crie também uma subclasse Livro, que será o
# nosso exemplo de Produto nesse exercício e implemente o método
# imprimir_preco para mostrar o preço do livro na tela.

class Produto:

    def imprimir_preco(self):
        raise NotImplementedError('Metodo precisa ser implementado')


class Livro(Produto):

    def imprimir_preco(self):
        print('Preco do livro')
