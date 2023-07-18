import sys
import os


def check_format(path_file):
    if not path_file.endswith('.txt'):
        return sys.stderr.write('Formato inválido')
    return True


def check_existance(path_file):
    if not os.path_file.exists():
        return sys.stderr.write(f'Arquivo {path_file} não encontrado')
    return True


def txt_importer(path_file):
    check_format(path_file)
    check_existance(path_file)
    return True


# print(txt_importer('exercicios/exemp.txt'))
# print(check_existance('exercicios/exemplo.csv'))
print(check_existance('exercicios/exemplo.txt'))
