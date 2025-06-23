"""
7. Classe Produto
Crie uma classe Produto com os atributos nome e preco.
Crie um método desconto(porcentagem) que calcula o preço com desconto e imprime o valor final.
"""


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, porcentagem):
        return self.preco - (self.preco * (porcentagem / 100))


mercadoria_1 = Produto('Game Resident Evil 4 Remake', 100)
valor_com_desconto = mercadoria_1.desconto(5)
print(f'Nome do Produto: {mercadoria_1.nome}')
print(f'Preço Original: R$ {mercadoria_1.preco:.2f}')
print(f'Preço com Desconto: R$ {valor_com_desconto:.2f}')
