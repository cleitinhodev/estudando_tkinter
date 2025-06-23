import tkinter as tk
from tkinter import font

root = tk.Tk()
root.title("Label - Demonstração Completa")
root.geometry("800x600")
root.configure(bg="#222")  # Cor de fundo da janela

# Fontes personalizadas
fonte_padrao = font.Font(family="Arial", size=14)
fonte_negrito = font.Font(family="Arial", size=14, weight="bold")
fonte_italico = font.Font(family="Arial", size=14, slant="italic")
fonte_custom = font.Font(family="Courier", size=16, weight="bold", slant="italic", underline=1, overstrike=0)

# LABEL COMPLETO COM TODAS OPÇÕES
label = tk.Label(
    root,

    # Texto
    text="Texto do Label Completo",

    # Cor e fundo
    fg="white",  # Cor da fonte (foreground)
    bg="#444",  # Cor do fundo (background)

    # Fonte
    font=fonte_custom,  # Fonte personalizada com negrito, itálico, sublinhado, etc.

    # Tamanho e espaçamento
    padx=20,  # Espaçamento interno na horizontal (Em pixels)
    pady=10,  # Espaçamento interno na vertical (Em pixels)

    # Alinhamento e posicionamento do texto
    anchor="center",  # Posição do texto dentro da Label: n, ne, e, se, s, sw, w, nw, center
    justify="center",  # Alinhamento do texto se houver várias linhas: left, center, right

    # Largura e altura (em caracteres, não pixels)
    width=30,
    height=3,

    # Bordas
    bd=5,  # Espessura da borda
    relief="ridge",  # Estilo da borda: flat, raised, sunken, groove, ridge, solid

    # Outros
    wraplength=300,  # Quebra automática de linha a cada X pixels
    cursor="hand2",  # Cursor do mouse ao passar por cima
    underline=0,  # Sublinha o caractere na posição indicada
    takefocus=True,  # Pode receber foco ao usar Tab
    textvariable=None  # Pode usar uma variável associada (StringVar)
)

# Posicionamento do label (exemplo com pack, pode trocar por grid/place)
label.pack(pady=20)

# Outro exemplo com texto variável
mensagem = tk.StringVar()
mensagem.set("Texto controlado por StringVar")
label2 = tk.Label(root, textvariable=mensagem, fg="black", bg="lightyellow", font=fonte_padrao)
label2.pack(pady=10)

# Exemplo de texto justificado com várias linhas
label3 = tk.Label(
    root,
    text="Essa é uma frase longa\ne com várias linhas\nde exemplo para mostrar\njustificação e quebra de texto.",
    justify="left",
    bg="white",
    fg="black",
    font=fonte_padrao,
    width=40,
    height=6,
    wraplength=250,
    relief="groove",
    bd=3
)
label3.pack(pady=10)

# Exemplo com imagens (comentado pois requer imagem válida)
'''
imagem = tk.PhotoImage(file="imagem.png")
label_img = tk.Label(root, image=imagem)
label_img.pack()
'''

"""
Podemos ver os valores como se fosse um dicionário comum, inclusive mudálos, ex:
print(label3.keys())
ou
label3['font'] = "Novo texto"
"""

root.mainloop()
