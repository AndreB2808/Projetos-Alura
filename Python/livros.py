class Livro:

    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo.title()
        self.autor = autor.title()
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
    
    def __str__(self):
        return f"Livro: {self.titulo} | Autor: {self.autor} | Ano de Publicação: {self.ano_publicacao}"
    
    def emprestar(self):
        self.disponivel = False

    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis
    
livro1 = Livro("Aprendendo Python", "John Doe", 2016)
livro2 = Livro("Jeitos gostosos de dar a buceta", "Janeta Simpsin", 2023)
livro3 = Livro("Como se curar com o poder do relacionamento", "Samuel Carente", 1996)
print(f"Antes de emprestar: Livro disponível? {livro3.disponivel}")
livro3.emprestar()
print(f"Depois de emprestar: Livro disponível? {livro3.disponivel}")

print(livro1)
print(livro2)
print(livro3)
