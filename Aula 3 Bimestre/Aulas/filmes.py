class filmes:

    def __init__(self, titulo, ano, genero, classificaçao):
        self.titulo = titulo
        self.ano = ano
        self.genero = genero
        self.classificaçao = classificaçao


filme1 = filmes("Um Sonho de Liberdade", "1994", "Drama", "A16")
filme2 = filmes("O Poderoso Chefão", "1972", "Crime, Drama, Tragédia", "A14")
filme3 = filmes("Batman: O Cavaleiro das Trevas", "2008", "Super-herói, Ação, Drama", "A12")
filme4 = filmes("O Poderoso Chefão: Part II", "1974", "Crime, Drama, Tragédia", "A14")
filme5 = filmes("12 Homens e uma Set  ença", "1957", "Drama", "AL")
filme6 = filmes("O Senhor dos Anéis: O Retorno do Rei ", "2003", "Aventura, Tragédia, Missão", "A12")
filme7 = filmes("A Lista de Schindler", "1993", "Docudrama, Drama da Época", "A14")


print(f"Filme 1: {filme1.titulo}. Ano: {filme1.ano}. Gênero: {filme1.genero}. Classificação: {filme1.classificaçao}")
print(f"Filme 2: {filme2.titulo}. Ano: {filme2.ano}. Gênero: {filme2.genero}. Classificação: {filme2.classificaçao}")
print(f"Filme 3: {filme3.titulo}. Ano: {filme3.ano}. Gênero: {filme3.genero}. Classificação: {filme3.classificaçao}")
print(f"Filme 4: {filme4.titulo}. Ano: {filme4.ano}. Gênero: {filme4.genero}. Classificação: {filme4.classificaçao}")
print(f"Filme 5: {filme5.titulo}. Ano: {filme5.ano}. Gênero: {filme5.genero}. Classificação: {filme5.classificaçao}")
print(f"Filme 6: {filme6.titulo}. Ano: {filme6.ano}. Gênero: {filme6.genero}. Classificação: {filme6.classificaçao}")
print(f"Filme 7: {filme7.titulo}. Ano: {filme7.ano}. Gênero: {filme7.genero}. Classificação: {filme7.classificaçao}")