from tkinter import *

'''
FRAME NO TKINTER – GUIA DEFINITIVO
-----------------------------------

O Frame é um contêiner usado para agrupar elementos gráficos (widgets) dentro de uma
janela (root) ou outro frame.

Ele é extremamente útil para:
✅ Organizar visualmente os elementos.
✅ Agrupar elementos por função (ex: área de login, menu, configurações).
✅ Personalizar seções da interface com estilo próprio.
✅ Trabalhar com layouts mais complexos.
✅ Criar seções reutilizáveis.

Principais atributos do Frame:
------------------------------
- master: O widget pai (geralmente root ou outro Frame).
- bg / background: Cor de fundo.
- bd / borderwidth: Largura da borda (padrão 0).
- relief: Estilo da borda: FLAT, SUNKEN, RAISED, GROOVE, RIDGE.
- width, height: Tamanho fixo do frame (usado com place() ou pack()).
- padx, pady: Espaçamento interno (dentro do frame).
- cursor: Tipo de cursor ao passar o mouse sobre o frame.
- highlightbackground: Cor da borda quando não está em foco.
- highlightcolor: Cor da borda quando está em foco.
- highlightthickness: Espessura da borda de destaque.
- takefocus: Se o frame pode receber foco ou não.

Você pode posicionar frames com:
- .grid() → organização em tabela (linhas e colunas)
- .pack() → empilhamento de cima pra baixo ou lado a lado
- .place() → posicionamento absoluto ou relativo

Exemplo completo a seguir:
'''

# Janela principal
root = Tk()
root.title("Exemplo Completo de Frame")
root.geometry("450x350")
root.config(bg="#1e1e1e")  # Fundo escuro para destacar o frame

# Frame personalizado
frame_login = Frame(
    root,
    bg="#e0f7fa",                # Cor de fundo do frame (azul claro)
    bd=4,                        # Borda de 4 pixels
    relief=RIDGE,                # Estilo da borda (RIDGE = cravado)
    width=300,
    height=180,
    padx=15,                     # Espaço interno horizontal
    pady=15,                     # Espaço interno vertical
    cursor="hand2",              # Cursor quando o mouse passa por cima
    highlightbackground="blue", # Cor da borda de destaque (fora de foco)
    highlightcolor="red",       # Cor da borda de destaque (com foco)
    highlightthickness=2        # Espessura da borda de destaque
)

# Posicionando o frame no centro da janela com place()
frame_login.place(relx=0.5, rely=0.5, anchor=CENTER)

# Widgets dentro do frame
Label(frame_login, text="Usuário:", bg="#e0f7fa", font=("Arial", 11)).grid(row=0, column=0, sticky=W)
Entry(frame_login).grid(row=0, column=1, padx=5, pady=5)

Label(frame_login, text="Senha:", bg="#e0f7fa", font=("Arial", 11)).grid(row=1, column=0, sticky=W)
Entry(frame_login, show="*").grid(row=1, column=1, padx=5, pady=5)

Button(frame_login, text="Login", width=10).grid(row=2, column=1, pady=(15, 0))

'''
DICAS AVANÇADAS:
----------------
1. É possível criar múltiplos frames para dividir visualmente a interface (ex: topo, centro, rodapé).
2. Você pode colocar Frames dentro de Frames (aninhados), criando estruturas mais complexas.
3. Também é possível usar ttk.Frame para aparência mais moderna, com tema nativo.
4. O uso de place() com relx, rely e anchor permite centralizar o frame com precisão.

'''

# Iniciando o loop da interface
root.mainloop()