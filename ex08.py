"""
8. Classe Relogio
Crie uma classe Relogio com os atributos hora, minuto, segundo.
Crie um método mostrar_hora() que imprime no formato HH:MM:SS.
"""


class Relogio:
    def __init__(self, hora, minuto, segundo):
        self.hora = str(hora)
        self.minuto = str(minuto)
        self.segundo = str(segundo)

    def mostrar_hora(self):
        horario = []
        if len(self.hora) == 1:
            horario.append(f'0{self.hora}')
        else:
            horario.append(str(self.hora))
        if len(self.minuto) == 1:
            horario.append(f'0{self.minuto}')
        else:
            horario.append(str(self.minuto))
        if len(self.segundo) == 1:
            horario.append(f'0{self.segundo}')
        else:
            horario.append(str(self.segundo))
        return horario


dia_1 = Relogio(14, 28, 35)
dia_2 = Relogio(1, 14, 3)
dia_3 = Relogio(17, 8, 0)
dia_4 = Relogio(23, 2, 45)
dia_5 = Relogio(3, 2, 9)

todos_horarios = [dia_1.mostrar_hora(),
                  dia_2.mostrar_hora(),
                  dia_3.mostrar_hora(),
                  dia_4.mostrar_hora(),
                  dia_5.mostrar_hora()]

for pos, dias in enumerate(todos_horarios):
    print(f'{pos + 1}º Dia: - ', end='')
    for p, t in enumerate(dias):
        print(f'{t}:' if p < 2 else f'{t}', end='')
    print(f'')

"""
Correção mais legível:

class Relogio:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def mostrar_hora(self):
        return f'{self.hora:02}:{self.minuto:02}:{self.segundo:02}'


dias = [
    Relogio(14, 28, 35),
    Relogio(1, 14, 3),
    Relogio(17, 8, 0),
    Relogio(23, 2, 45),
    Relogio(3, 2, 9)
]

for i, dia in enumerate(dias, start=1):
    print(f'{i}º Dia: - {dia.mostrar_hora()}')
"""