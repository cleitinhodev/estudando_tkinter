"""
9. Classe Funcionario
Crie uma classe Funcionario com os atributos nome, cargo, salario.
Crie um método aumentar_salario(porcentagem) que aumenta o salário e imprime o novo valor.
"""


class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def aumentar_salario(self, porcentagem):
        return self.salario + (self.salario * (porcentagem / 100))


colaborador_1 = Funcionario('Ricardo Soares', 'Eletricista', 2780)

print(f'Nome do Colaborador: {colaborador_1.nome}\n'
      f'Salário anterior: R$ {colaborador_1.salario:.2f}\n'
      f'Novo salário: R$ {colaborador_1.aumentar_salario(15):.2f}')
