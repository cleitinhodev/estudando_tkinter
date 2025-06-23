"""
TÍTULO: CLASSES COM TKINTER (GUI) — ESTRUTURA E EXPLICAÇÃO COMPLETA

Uma classe funciona como um 'Contêiner' que serve para armazenar
um conjunto de atributos, métodos e comportamentos. É um molde.

No caso do Tkinter, isso se aplica perfeitamente. Criamos um widget (como um Frame)
a partir de uma classe personalizada, e colocamos dentro dele os elementos
(Labels, Entry, Buttons, etc.) — tudo organizado e reutilizável.

Vamos criar uma tela de login com estrutura de classe, explicando cada etapa.
"""

from tkinter import *  # Importando tudo do Tkinter


# Criação da classe personalizada que representa uma "tela de login":
class JanelaDeLogin(Frame):  # Aqui estamos criando uma SUBCLASSE chamada JanelaDeLogin, que HERDA da SUPERCLASSE Frame.

    def __init__(self, mestre):
        """
        O método __init__ é o CONSTRUTOR da classe.
        Ele é chamado automaticamente quando criamos um objeto dessa classe.

        O parâmetro 'mestre' representa o widget pai (geralmente a janela principal).
        """

        # IMPORTANTE: Aqui usamos 'super().__init__(mestre)' para inicializar corretamente a superclasse Frame.
        # Isso transforma a instância (self) em um verdadeiro Frame funcional do Tkinter.
        # Sem isso, os atributos abaixo (como self['height']) causariam erro, pois self ainda não seria um Frame.
        super().__init__(mestre)

        # Atributos visuais do Frame (a "caixinha" onde ficarão os elementos):
        self['height'] = 150          # Altura do frame
        self['width'] = 200           # Largura do frame
        self['bd'] = 2                # Espessura da borda
        self['relief'] = 'solid'      # Tipo da borda (solid = linha sólida)

        # Widgets internos (rótulo e caixa de entrada):
        label_nome = Label(self, text='Nome: ')  # Label = texto fixo indicando o campo
        text_nome = Entry(self)                 # Entry = campo de entrada de texto

        # Posicionando os elementos na grade (layout em tabela):
        label_nome.grid(row=0, column=0)        # Posição: linha 0, coluna 0
        text_nome.grid(row=0, column=1)         # Posição: linha 0, coluna 1


# Criando a janela principal da aplicação:
root = Tk()  # Aqui criamos a janela principal do programa.

# Agora vamos criar múltiplos objetos da classe JanelaDeLogin:
# Isso mostra como a classe é reutilizável. Cada objeto é independente.

janela_de_login_1 = JanelaDeLogin(root)
janela_de_login_2 = JanelaDeLogin(root)
janela_de_login_3 = JanelaDeLogin(root)
janela_de_login_4 = JanelaDeLogin(root)
janela_de_login_5 = JanelaDeLogin(root)

# Exibindo os frames na tela:
# Usamos .pack() para posicionar os frames (um embaixo do outro, por padrão).
janela_de_login_1.pack()
janela_de_login_2.pack()
janela_de_login_3.pack()
janela_de_login_4.pack()
janela_de_login_5.pack()

# Mantém a janela aberta e esperando interação do usuário:
root.mainloop()
