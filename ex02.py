"""
2. Classe Carro
Crie uma classe Carro com os atributos marca, modelo e ano.
Crie um método exibir_dados() que imprime as informações do carro.
"""


class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_dados(self):
        print(f'Marca: {self.marca}\n'
              f'Modelo: {self.modelo}\n'
              f'Ano: {self.ano}')


latavelha_1 = Carro('Volkswagen', 'Gol', 1997)
latavelha_1.exibir_dados()
