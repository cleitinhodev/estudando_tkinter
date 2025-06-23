
# ======================================
#        CLASSES EM PYTHON - GUIA
# ======================================

# 1. DEFININDO UMA CLASSE SIMPLES
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome  # atributo
        self.idade = idade  # atributo

    def apresentar(self):  # método
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Criando um objeto da classe Pessoa
p1 = Pessoa("Ana", 25)
p1.apresentar()

# --------------------------------------

# 2. HERANÇA (classe filha herda da classe mãe)
class Animal:
    def falar(self):
        print("Som genérico de animal.")

class Cachorro(Animal):
    def falar(self):
        print("Au au!")

dog = Cachorro()
dog.falar()

# --------------------------------------

# 3. MÉTODO ESPECIAL __str__ (exibido com print)
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} por {self.autor}"

livro1 = Livro("1984", "George Orwell")
print(livro1)

# --------------------------------------

# 4. MÉTODO ESTÁTICO (@staticmethod)
class Util:
    @staticmethod
    def saudacao():
        print("Olá! Isso é um método estático.")

Util.saudacao()

# --------------------------------------

# 5. MÉTODO DE CLASSE (@classmethod)
class Usuario:
    def __init__(self, nome):
        self.nome = nome

    @classmethod
    def criar_anonimo(cls):
        return cls("Anônimo")

user = Usuario.criar_anonimo()
print(user.nome)

# --------------------------------------

# 6. ENCAPSULAMENTO (protegido e privado)
class ContaBancaria:
    def __init__(self, saldo):
        self._saldo = saldo          # protegido
        self.__segredo = "123abc"    # privado

    def mostrar_saldo(self):
        print(f"Saldo: R${self._saldo}")

    def mostrar_segredo(self):
        print(f"Segredo: {self.__segredo}")

conta = ContaBancaria(1000)
conta.mostrar_saldo()
# conta.__segredo  # ERRO: atributo privado
conta.mostrar_segredo()

# --------------------------------------

# 7. PROPRIEDADES COM @property
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    @property
    def area(self):
        return self.largura * self.altura

r = Retangulo(4, 5)
print("Área:", r.area)  # Parece um atributo, mas é um método!

# FIM DO BLOCO DE ESTUDO
