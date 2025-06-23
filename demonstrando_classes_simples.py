'''
🔹 O que é uma Classe em Python?

Uma classe em Python é como um molde (ou modelo) para criar objetos.
Ela define quais **atributos** (características) e **métodos** (ações) os objetos terão.

Usamos classes quando queremos organizar melhor o código e representar entidades do mundo real
(como pessoas, carros, contas bancárias, etc.) com suas próprias informações e comportamentos.

🧠 É um dos pilares da Programação Orientada a Objetos (POO).
'''

# 🔸 Criando uma classe simples chamada 'Pessoa'
class Pessoa:
    # Método especial chamado automaticamente ao criar o objeto
    def __init__(self, nome, idade):
        self.nome = nome     # Atributo: armazena o nome da pessoa
        self.idade = idade   # Atributo: armazena a idade da pessoa

    # Método: uma função que pertence à classe
    def apresentar(self):
        print(f'Olá, meu nome é {self.nome} e eu tenho {self.idade} anos!')

# 🔸 Criando objetos (instâncias da classe Pessoa)
humano1 = Pessoa('Ana', 25)
humano2 = Pessoa('Carlos', 30)

# Chamando o método 'apresentar' de cada objeto
humano1.apresentar()
humano2.apresentar()

'''
🧾 Explicação dos principais termos:

| Termo        | Significado                                                                 |
| ------------ | ---------------------------------------------------------------------------- |
| `class`      | Palavra-chave usada para definir uma classe.                               |
| `__init__`   | Método especial chamado automaticamente ao criar um objeto. É o construtor. |
| `self`       | Referência ao próprio objeto (instância). Necessário em todos os métodos.  |
| `atributo`   | Uma variável que pertence ao objeto. Ex: nome, idade.                      |
| `método`     | Uma função definida dentro da classe. Ex: apresentar().                    |
| `objeto`     | Uma instância da classe. Representa um exemplo real com dados próprios.    |

🎯 Exemplo da vida real:
Imagine uma **classe** chamada `Carro`. Cada `Carro` tem atributos como cor, modelo e ano.
Quando você cria um carro específico (ex: um carro vermelho de 2020), você está criando um **objeto**.
'''
