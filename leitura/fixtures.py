import pytest


@pytest.fixture  # Criamos a fixture por meio do decorador pytest.fixture
def my_list():  # Por padrão, o nome da fixture será o nome da função
    return [1, 2, 3]  # Retorna o valor que a fixture possuirá


def test_a_simple_test():
    assert True


def test_sum(my_list):  # Recebemos a fixture como parâmetro da função de teste
    assert sum(my_list) == 6  # Usamos a lista retornada pela fixture


def test_list_item_multiply(my_list):  # Recebemos a mesma fixture aqui também
    assert [item * 3 for item in my_list] == [3, 6, 9]
