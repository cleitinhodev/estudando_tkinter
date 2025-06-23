"""
4. Classe Pessoa
Crie uma classe Pessoa com os atributos nome e idade.
Crie um método maior_de_idade() que imprime:

"É maior de idade." se a idade for 18 ou mais

"É menor de idade." se for menor que 18
"""


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def maior_de_idade(self):
        if self.idade >= 18:
            print('É maior de idade.')
        else:
            print('É menor de idade.')


individuo_1 = Pessoa('Maria', 39)
individuo_1.maior_de_idade()

individuo_2 = Pessoa('João', 15)
individuo_2.maior_de_idade()


"""
Isso aqui funciona, mas não está correto:

individuo_1 = Pessoa('Maria', 39).maior_de_idade()
individuo_2 = Pessoa('João', 15).maior_de_idade()
"""
