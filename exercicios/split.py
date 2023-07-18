def txt_importer(path_file):
    with open(path_file) as file:
        content = file.read()
        return content.split('\n')


print(txt_importer('exercicios/exemplo.txt'))
