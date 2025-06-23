import tkinter as tk

"""
Basicamente o Message no sentido geral é muito parecido com o label a primeira vista,
porém, ele tem uma espécie de 'quebra de linha' automática da qual você define o tamanho.
Ideal para textos mais longos, mas ainda é situacional.
"""

# Cria a janela principal
root = tk.Tk()
root.title("Exemplo com Label e Message")

# Label: texto curto ou simples (não quebra automaticamente)
label = tk.Label(
    text='Jogos são minha paixão. ' * 10,  # Texto longo repetido
    bg='lightblue'                         # Cor de fundo do rótulo
)
label.pack(pady=10)  # Espaço vertical ao redor do label

# Message: ideal para texto longo, quebra automaticamente com base no 'width'
message = tk.Message(
    text='Jogos são minha paixão. ' * 10,  # Texto longo repetido
    width=200,             # Largura máxima antes de quebrar a linha (em pixels)
    bg='lightgreen',       # Cor de fundo
    fg='black',            # Cor do texto (foreground)
    font=('Arial', 12, 'italic'),  # Fonte (nome, tamanho, estilo)
    padx=10,               # Espaço interno horizontal
    pady=10,               # Espaço interno vertical
    anchor='w',            # Alinhamento do texto (n, s, e, w, center, etc.)
    justify='left',        # Justificação do texto (left, center, right)
    relief='raised',       # Tipo de borda (flat, groove, raised, ridge, solid, sunken)
    bd=2,                  # Espessura da borda (border width)
    cursor='arrow',        # Tipo de cursor ao passar por cima
    aspect=100             # Proporção largura/altura (100 = 1:1, 200 = 2:1, etc.)
)
message.pack(pady=10)

# Inicia o loop principal da interface
root.mainloop()