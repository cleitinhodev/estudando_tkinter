"""
6. Classe Aluno
Crie uma classe Aluno com os atributos nome, nota1 e nota2.
Crie um método media() que calcule a média e diga se foi aprovado (média ≥ 7).
"""


class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        media = (self.nota1 + self.nota2) / 2
        if media >= 7:
            return 'Aprovado'
        else:
            return 'Reprovado'


estudante_1 = Aluno('Joaquim', 9.6, 8.1)
estudante_2 = Aluno('Renata', 3.6, 4.1)
print(f'{estudante_1.media()}\n'
      f'{estudante_2.media()}')
