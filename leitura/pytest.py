# Garanta que está com seu ambiente virtual devidamente criado e ativado.

# Crie o ambiente virtual com o comando
#           python -m venv .venv

# Ative o ambiente virtual com o comando
#           source .venv/bin/activate

# Instale o Pytest com o comando
#           pip install pytest==7.3.1

# Confirme que a instalação foi bem sucedida rodando o comando
#           pytest --version

# Comandos para testes:
#           pytest
#           pytest -vv    # Saída mais verbosa
#           pytest --doctest-modules -vv  # Adiciona os doctests aos pytest


# Para mudar o escopo, basta passar o escopo desejado como argumento
#  para o parâmetro scope do decorador pytest.fixture, por exemplo
# @pytest.fixture(scope="module").
