class Book:
    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    def info(self):
        return f"""Título: {self.title}
Autor: {self.author}
Páginas: {self.pages}"""


livro = Book('Titulo legal', 'Autor Gente Boa', 1000)
