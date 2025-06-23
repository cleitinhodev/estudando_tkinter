import tkinter as tk

# Janela principal
root = tk.Tk()
root.title("Área de Desenho (Paint Simples)")
root.geometry("800x600")

# Canvas onde vamos desenhar
canvas = tk.Canvas(root, bg="white", width=780, height=550)
canvas.pack(pady=10)

# Variável para armazenar posição anterior do mouse
x_antigo, y_antigo = None, None

# Cor e espessura do traço
cor_atual = "black"
espessura = 3

# Função chamada quando o mouse é pressionado
def iniciar_desenho(event):
    global x_antigo, y_antigo
    x_antigo, y_antigo = event.x, event.y

# Função chamada quando o mouse se move com botão pressionado
def desenhar(event):
    global x_antigo, y_antigo
    if x_antigo and y_antigo:
        canvas.create_line(x_antigo, y_antigo, event.x, event.y,
                           fill=cor_atual, width=espessura, capstyle=tk.ROUND, smooth=True)
        x_antigo, y_antigo = event.x, event.y

# Quando o botão do mouse é solto
def parar_desenho(event):
    global x_antigo, y_antigo
    x_antigo, y_antigo = None, None

# Botões de cor
def mudar_cor(nova_cor):
    global cor_atual
    cor_atual = nova_cor

# Limpar a tela
def limpar_canvas():
    canvas.delete("all")

# Bind dos eventos do mouse
canvas.bind("<ButtonPress-1>", iniciar_desenho)
canvas.bind("<B1-Motion>", desenhar)
canvas.bind("<ButtonRelease-1>", parar_desenho)

# Botões de cor
frame_cores = tk.Frame(root)
frame_cores.pack()

cores = ["black", "red", "blue", "green", "purple", "orange"]
for cor in cores:
    btn = tk.Button(frame_cores, bg=cor, width=3, command=lambda c=cor: mudar_cor(c))
    btn.pack(side=tk.LEFT, padx=2)

# Botão de limpar
btn_limpar = tk.Button(root, text="Limpar Tela", command=limpar_canvas)
btn_limpar.pack(pady=5)

root.mainloop()
