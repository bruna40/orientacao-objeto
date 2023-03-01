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


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
        self.duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
        self.temporadas = temporadas


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(f'{vingadores.nome} - {vingadores.ano} - {vingadores.duracao} min - {vingadores.likes} likes')


atlanta = Serie('Atlanta', 2018, 2)
atlanta.dar_likes()


print(f'{atlanta.nome} - {atlanta.temporadas} temporadas - {atlanta.likes} likes')
