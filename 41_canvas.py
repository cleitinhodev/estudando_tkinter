import tkinter as tk

# Janela principal
root = tk.Tk()
root.title("Tutorial Completo do Canvas")
root.geometry("600x500")

# Criando o widget Canvas
canvas = tk.Canvas(
    root,
    width=500,          # Largura do canvas
    height=400,         # Altura do canvas
    bg="white",         # Cor de fundo
    bd=2,               # Espessura da borda
    relief="solid",     # Tipo de borda: flat, groove, ridge, solid
    highlightthickness=1,   # Espessura da borda de foco
    highlightbackground="gray",  # Cor da borda quando sem foco
)
canvas.pack(pady=10)

# =============================================
# FORMAS GEOMÉTRICAS
# =============================================

# Linha (x1, y1, x2, y2)
linha = canvas.create_line(10, 10, 200, 10, fill="blue", width=3, dash=(5, 2))

# Retângulo (x1, y1, x2, y2)
retangulo = canvas.create_rectangle(50, 30, 200, 100, fill="lightblue", outline="black", width=2)

# Óvalo (circunferência ou elipse) – insere dentro de um retângulo invisível
oval = canvas.create_oval(250, 30, 400, 100, fill="pink", outline="red")

# Polígono (vários pontos: x1, y1, x2, y2, ...)
poligono = canvas.create_polygon(100, 150, 150, 180, 120, 220, 80, 190,
                                 fill="yellow", outline="black")

# Arco (parte de círculo ou elipse)
arco = canvas.create_arc(250, 150, 400, 250, start=0, extent=150,
                         fill="orange", style=tk.PIESLICE)

# Texto
texto = canvas.create_text(300, 300, text="Olá, Canvas!", font=("Arial", 16), fill="black")

# =============================================
# IMAGEM (exemplo com imagem .gif ou .png)
# =============================================
# Obs: é preciso manter a referência da imagem para ela aparecer
img = tk.PhotoImage(file="Img/Monika_small.png")  # Coloque uma imagem válida no mesmo diretório
canvas.imagem_exemplo = img
# canvas.create_image(x, y, image=img, anchor=...)
# anchor define o ponto de ancoragem da imagem (center, nw, etc.)
# canvas.create_image(100, 300, image=img, anchor="nw")

# =============================================
# EVENTOS E MOVIMENTAÇÃO DE OBJETOS
# =============================================

# Função para mover o retângulo ao clicar
def mover_retangulo(event):
    canvas.move(retangulo, 10, 0)  # move(objeto, x, y)

canvas.bind("<Button-1>", mover_retangulo)  # Clique esquerdo no canvas

# =============================================
# TAGS – nomear objetos para manipulação em grupo
# =============================================

# Criando dois círculos com a mesma tag
bola1 = canvas.create_oval(50, 300, 80, 330, fill="green", tags="bolas")
bola2 = canvas.create_oval(100, 300, 130, 330, fill="green", tags="bolas")

def mover_bolas():
    canvas.move("bolas", 0, -10)  # move todos os objetos com a tag "bolas"

btn_mover = tk.Button(root, text="Mover Bolas", command=mover_bolas)
btn_mover.pack()

# =============================================
# OUTROS MÉTODOS ÚTEIS DO CANVAS
# =============================================

# canvas.delete(objeto ou tag ou "all") – apaga objetos
# canvas.itemconfig(objeto ou tag, opções...) – altera propriedades
# canvas.coords(objeto, novas coordenadas...) – redefine posição
# canvas.find_withtag("bolas") – retorna objetos com tag
# canvas.find_closest(x, y) – encontra o objeto mais próximo
# canvas.gettags(objeto) – retorna as tags associadas
# canvas.itemcget(objeto, "option") – pega o valor de uma opção
# canvas.move(obj, dx, dy) – move objeto
# canvas.scale(obj, x_orig, y_orig, sx, sy) – escala
# canvas.rotate() – não existe nativamente, teria que usar bibliotecas externas
# canvas.create_window() – para colocar widgets dentro do canvas

root.mainloop()

"""
Lista de Formas Suportadas:
| Função               | Descrição                       |
| -------------------- | ------------------------------- |
| `create_line()`      | Cria uma linha                  |
| `create_rectangle()` | Cria um retângulo               |
| `create_oval()`      | Cria um círculo/óvalo           |
| `create_arc()`       | Cria um arco                    |
| `create_polygon()`   | Cria um polígono (fechado)      |
| `create_text()`      | Exibe um texto                  |
| `create_image()`     | Exibe uma imagem                |
| `create_window()`    | Insere widgets dentro do canvas |

Métodos de Manipulação
| Método                        | Descrição                           |
| ----------------------------- | ----------------------------------- |
| `move(tag/obj, dx, dy)`       | Move objeto                         |
| `delete(tag/obj)`             | Remove objeto                       |
| `itemconfig(tag/obj, op=val)` | Altera propriedades do item         |
| `coords(tag/obj, ...)`        | Redefine coordenadas                |
| `scale(tag, ox, oy, sx, sy)`  | Escala objetos em torno de um ponto |
| `gettags(obj)`                | Retorna tags associadas             |
| `find_withtag(tag)`           | Retorna IDs com a tag               |
| `find_closest(x, y)`          | Objeto mais próximo                 |

⚠️ Dicas importantes
O Canvas não possui rotação nativa de objetos, mas é possível fazer manualmente com matemática ou bibliotecas externas.

Para usar scrollbars, é preciso conectar com canvas.configure(yscrollcommand=scrollbar.set) etc.

Sempre mantenha a referência de imagens (PhotoImage) em uma variável ou atributo, senão elas não aparecem.
"""