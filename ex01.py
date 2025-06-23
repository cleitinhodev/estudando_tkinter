"""
1. Classe Cachorro
Crie uma classe Cachorro com os atributos nome e raça, e um método latir() que imprime:

"{nome} está latindo!"
"""

# Versão simples


class Cachorro:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def latir(self):
        print(f'{self.nome} está latindo!')


doguinho1 = Cachorro('Jubileu', 'Viralata')
doguinho1.latir()

# Versão Melhorada
'''class Cachorro:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def latir(self, quantidade):
        print(f'{self.nome} está latindo {quantidade} vezes!')


doguinho_1 = Cachorro('Jubileu', 'Viralata')
doguinho_1.latir(4)'''
