from tkinter import *

# Criando janela principal
root = Tk()
root.title("Gerenciadores de Layout")
root.geometry("600x400")
root.config(bg="lightgray")  # Cor de fundo para facilitar visualização

# ---------------------------------------
# MÉTODO 1: PACK
# ---------------------------------------
# O pack organiza os elementos de forma sequencial (de cima para baixo por padrão).

# Label superior usando PACK
lbl_pack = Label(root, text="PACK: de cima para baixo por padrão", bg="skyblue")
lbl_pack.pack(fill=X, padx=5, pady=5)  # fill=X faz o Label se expandir na horizontal

# Botões usando diferentes opções do pack
btn1 = Button(root, text="Top", bg="lightgreen")
btn1.pack(side=TOP, fill=X)

btn2 = Button(root, text="Left", bg="orange")
btn2.pack(side=LEFT, fill=Y)

btn3 = Button(root, text="Right", bg="red")
btn3.pack(side=RIGHT, fill=Y)

btn4 = Button(root, text="Bottom", bg="purple", fg="white")
btn4.pack(side=BOTTOM, fill=X)

'''
PROPRIEDADES DO pack():
- side=TOP, BOTTOM, LEFT, RIGHT → posição do widget
- fill=X, Y, BOTH → preenche horizontalmente, verticalmente ou ambos
- expand=True/False → permite expandir o espaço disponível
- padx, pady → margem externa (espaço entre widgets)
- ipadx, ipady → margem interna (espaço dentro do widget)
'''

# ---------------------------------------
# MÉTODO 2: GRID
# ---------------------------------------
# O grid organiza os elementos como uma tabela (linhas e colunas)

# Separador visual
Label(root, text="\n", bg="lightgray").pack()

frame_grid = Frame(root, bg="white", bd=2, relief="groove")
frame_grid.pack(pady=10)

Label(frame_grid, text="GRID: usa linha e coluna", bg="lightblue").grid(row=0, column=0, columnspan=2, sticky="we", padx=5, pady=5)

btn5 = Button(frame_grid, text="Linha 1 - Coluna 1", bg="lightyellow")
btn5.grid(row=1, column=0, padx=5, pady=5)

btn6 = Button(frame_grid, text="Linha 1 - Coluna 2", bg="lightyellow")
btn6.grid(row=1, column=1, padx=5, pady=5)

btn7 = Button(frame_grid, text="Linha 2 - Coluna 1 (ocupa 2 colunas)", bg="lightpink")
btn7.grid(row=2, column=0, columnspan=2, sticky="we", padx=5, pady=5)

'''
PROPRIEDADES DO grid():
- row / column → posição do widget
- rowspan / columnspan → ocupa várias linhas ou colunas
- sticky=N, S, E, W → "gruda" em direções específicas
- padx / pady → margem externa
- ipadx / ipady → margem interna
- sticky="nsew" → ocupa completamente a célula (Sem deixar aqueles "espaçinhos")
- sticky="ns" → ocupa completamente a parte de cima e de baixo da célula
- sticky="we" → ocupa completamente a parte da direita e esquerda da célula
'''

# ---------------------------------------
# MÉTODO 3: PLACE
# ---------------------------------------
# O place posiciona os widgets manualmente com coordenadas exatas.

# Separador visual
Label(root, text="\n", bg="lightgray").pack()

frame_place = Frame(root, bg="white", bd=2, relief="groove", height=100)
frame_place.pack(fill=X, padx=10, pady=10)
frame_place.pack_propagate(False)

Label(frame_place, text="PLACE: posicionamento absoluto", bg="lightblue").place(x=10, y=5)

btn8 = Button(frame_place, text="Botão em x=50 y=30", bg="lightcoral")
btn8.place(x=50, y=30)

btn9 = Button(frame_place, text="Botão 50% da largura", bg="lightgreen")
btn9.place(relx=0.5, rely=0.5, anchor="center")  # Relativo à largura e altura

'''
PROPRIEDADES DO place():
- x / y → posição absoluta em pixels
- relx / rely → posição relativa (0.0 a 1.0)
- width / height → tamanho fixo
- relwidth / relheight → tamanho relativo (0.0 a 1.0)
- anchor → define o ponto de ancoragem (center, nw, ne, etc.)
'''

# Inicia a aplicação
root.mainloop()

