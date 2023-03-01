class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
    
    def imprime(self):
        print(f'Nome: {self.nome} - Ano: {self.ano} - Likes: {self.likes}')


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def imprime(self):
        print(f'Nome: {self.nome} - Ano: {self.ano} - Duração: {self.duracao} min- Likes: {self.likes}')


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def imprime(self):
        print(f'Nome: {self.nome} - Ano: {self.ano} - Temporadas: {self.temporadas}- Likes: {self.likes}')


vingadores = Filme('vingadores - guerra infinita', 2018, 160)

atlanta = Serie('Atlanta', 2018, 2)
atlanta.dar_likes()

filme_e_serie = [vingadores, atlanta]

for programa in filme_e_serie:
    detalhes = programa.imprime()