import json
import csv


# A função retrieve_books vai receber um file. Quem é esse file?
# Esse file é o json que vamos ler para poder gerar o CSV
# Essa função transforma esse file em um objeto Python que de para manipular
def retrieve_books(file):
    # Desserialização do arquivo JSON - Retorna o objeto Python
    return json.load(file)


# A função count_books_by_categories vai contar os livros pela catergoria
def count_books_by_categories(books):
    # Cria um dicionário vazio para armazenar as informações
    categories = {}
    # Vai pegar cada livro que esta dentro do 'books' (que é o objeto Python)
    for book in books:
        # Vai percorrer cada array que esta na chave 'categories' de cada livro
        for category in book["categories"]:
            # Se não existe a categoria especifica dentro do dict de categorias
            # Método array.get() -> Verifica se o valor existe, se não existir:
            if not categories.get(category):
                # A categoria será criada dentro do dict e ficar armazenada
                categories[category] = 0  # { category: 0 }
            # Caso ja tenha sido criada, vai somando 1 no dict por ocorrencia
            categories[category] += 1  # { category: 1 + ... }
    return categories


# A função calculate_percen... vai receber o dicionario criado na func
# count_books_by_categories e o total de books
def calculate_percentage_by_category(book_count_by_category, total_books):
    #  Ja faz um return direto de uma lista
    return [
        # A lista contem a categoria e o (número de livros / total de livros)
        [category, num_books / total_books]
        # Transforma o dict nums lista de tuplas => dict.items()
        for category, num_books in book_count_by_category.items()
    ]


#
def write_csv_report(file, header, rows):
    # Escreve o arquivo
    writer = csv.writer(file)
    # Cria o cabeçalho
    writer.writerow(header)  # writerow() => Escreve uma linha só
    # Cria as linhas com as informações
    writer.writerows(rows)


if __name__ == "__main__":
    # retrieve books
    with open("books.json") as file:
        books = retrieve_books(file)

    # count by category
    book_count_by_category = count_books_by_categories(books)

    # calculate percentage
    number_of_books = len(books)
    books_percentage_rows = calculate_percentage_by_category(
        book_count_by_category, number_of_books
    )

    # write csv
    header = ["categoria", "percentagem"]
    with open("report.csv", "w") as file:
        write_csv_report(file, header, books_percentage_rows)
