"""
3. Classe Livro
Crie uma classe Livro com os atributos titulo, autor e paginas.
Crie um método resumo() que diga:

"O livro {titulo}, de {autor}, tem {paginas} páginas."
"""


class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def resumo(self):
        return f'O livro {self.titulo}, de {self.autor}, tem {self.paginas} páginas.'


leitura_1 = Livro('Harry Potter - E a Pedra Filosofal', 'J.K. Rowling', 208)
print(leitura_1.resumo())
