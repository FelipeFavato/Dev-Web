try:
    # Código que pode gerar exceções
    resultado = 10 / 0  # Exemplo de divisão por zero
except ZeroDivisionError:
    # Trecho de tratamento específico para a exceção ZeroDivisionError
    print("Erro: Divisão por zero não é permitida.")
except Exception as e:
    # [opcional] Trecho de tratamento genérico para todas as outras exceções
    print("Erro: ", str(e))
else:
    # [opcional] Trecho executado se nenhuma exceção for levantada
    print("Resultado:", resultado)
finally:
    # [opcional] Trecho sempre executado, independentemente de exceções
    print("Fim do programa.")


x = -1
if x < 0:
    raise ValueError("O valor de x não pode ser negativo.")
