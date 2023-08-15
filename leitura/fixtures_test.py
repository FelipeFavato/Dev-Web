# A fixture capsys é usada para capturar as saídas padrão
# e de erro em um teste.

# Sim, é só receber `capsys` como parâmetro em qualquer função de teste que o
# pytest faz o resto da magia acontecer
def test_print_to_stdout(capsys):
    print("Hello, world!")
    captured = capsys.readouterr()
    assert captured.out == "Hello, world!\n"  # print coloca \n automaticamente


def test_error_to_stderr(capsys):
    import sys
    sys.stderr.write("Error message\n")
    captured = capsys.readouterr()
    assert captured.err == "Error message\n"


# A fixture monkeypatch, do pytest, é usada para alterar o comportamento de
# funções ou métodos, permitindo a simulação de condições específicas para
# testes. Ela permite o acesso ao objeto “patch” que pode ser utilizado para
# modificar objetos ou módulos importados, bem como variáveis de ambiente,
# argumentos de linha de comando e outros.

def my_function():
    return f"Você digitou {input('Digite algo: ')}!"


def test_my_function(monkeypatch):
    # Input recebe um parâmetro que mock_input não usa, por isso o _
    def mock_input(_):
        return "Python"

    # Trocamos a input do sistema pela nossa mock_input
    monkeypatch.setattr("builtins.input", mock_input)
    output = my_function()

    assert output == "Você digitou Python!"


# Um bom caso de uso da fixture tmp_path pode ser para testar
# uma função que cria arquivos, por exemplo uma função que gera
# um arquivo de saída. O teste pode criar um diretório temporário
# com a fixture e chamar a função a ser testada, passando o
# diretório temporário como argumento. Então, o teste pode verificar
# se a função criou os arquivos corretamente dentro do diretório temporário.


import json
import os


def generate_output(content, path):
    with open(path, "w", encoding="utf-8") as file:
        file.write(json.dumps(content))


def test_generate_output(tmp_path):
    content = {"a": 1}
    output_path = tmp_path / "out.json"
    # O operador '/' funciona na linha anterior pois temp_path não é uma
    # string comum, mas sim um objeto Path

    generate_output(content, output_path)

    assert os.path.isfile(output_path)
    with open(output_path) as file:
        assert file.read() == '{"a": 1}'
