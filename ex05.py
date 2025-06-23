"""
5. Classe Retangulo
Crie uma classe Retangulo com os atributos largura e altura.
Crie dois métodos:

area() que retorna a área do retângulo ---> Area = altura x largura
perimetro() que retorna o perímetro do retângulo ---> 2 x (altura + largura)
"""


class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def area(self):
        return self.altura * self.largura

    def perimetro(self):
        return 2 * (self.altura + self.largura)


ret_1 = Retangulo(15, 13)
print(f'A área do retângulo é: {ret_1.area()} cm²')
print(f'O perímetro do retângulo é: {ret_1.perimetro()} cm')
