# def txt_importer(path_file):
#     if not path_file.endswith('.txt'):
#         return False
#     else:
#         with open(path_file, 'r') as file:
#             content = file.read()
#             print(content)
import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        sys.stderr.write('Formato inválido')


# txt_importer('exercicios/exemplo.txt')
txt_importer('exercicios/exemplo')
