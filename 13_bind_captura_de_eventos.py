import tkinter as tk

"""
.bind() é um método usado em widgets do Tkinter para ligar eventos do usuário 
(como cliques, teclas, movimentos do mouse etc.) a funções que você define.

widget.bind("<evento>", funcao)

widget: janela (root) ou qualquer outro widget (label, botão, etc.).

<evento>: evento do usuário (como <Button-1>, <Key>, etc.).

funcao: função que será executada quando o evento acontecer.

A função deve aceitar um argumento (o evento em si).
________________________________________________________________________________________
Quando um evento ocorre, o Tkinter envia um objeto de evento com informações úteis:

def funcao(event):
    print(event.keysym)  # Tecla pressionada
    print(event.x, event.y)  # Posição do mouse (se aplicável)
                                         
                      TECLADO
Evento                                     	       Descrição
<Key> ou <KeyPress>                          Qualquer tecla pressionada
<KeyRelease>                                 Quando a tecla é solta
<Return>	                                 Tecla Enter
<Escape>                                     Tecla Esc
<space>	                                     Barra de espaço
<BackSpace>                                  Tecla backspace
<Delete>	                                 Tecla Delete
<Up> <Down> <Left> <Right>                   Setas do teclado
<Control-Key-a>                              Ctrl + A
<Shift-Key-A>	                             Shift + A

                       MOUSE
Evento	                                          Descrição
<Button-1>	                                 Clique botão esquerdo
<Button-2>	                                 Clique botão do meio
<Button-3>	                                 Clique botão direito
<Double-Button-1>	                         Clique duplo (botão esquerdo)
<Triple-Button-1>	                         Clique triplo
<B1-Motion>	                                 Movimento com botão 1 pressionado
<Motion>                           	         Movimento do mouse
<MouseWheel>	                             Rolagem (pode variar no Mac/Linux)        

                  MOVIMENTO/FOCO

Evento                      	                  Descrição
<Enter>	                                     Mouse entrou no widget
<Leave>	                                     Mouse saiu do widget
<FocusIn>	                                 Widget ganhou foco
<FocusOut>	                                 Widget perdeu o foco                            
________________________________________________________________________________________
EXEMPLOS PRÁTICOS:
________________________________________________________________________________________
 1. Detectar tecla pressionada:
 
 from tkinter import *

def tecla(event):
    print("Tecla pressionada:", event.keysym)

root = Tk()
root.bind("<KeyPress>", tecla)
root.mainloop()
________________________________________________________________________________________
 2. Detectar clique do mouse:
 
 def clique(event):
    print(f"Você clicou nas coordenadas: {event.x}, {event.y}")

root.bind("<Button-1>", clique)
________________________________________________________________________________________
3. Detectar seta do teclado:

def mover(event):
    if event.keysym == "Up":
        print("Para cima!")
    elif event.keysym == "Down":
        print("Para baixo!")

root.bind("<Key>", mover)
________________________________________________________________________________________
4. Detectar rolagem do mouse:

def scroll(event):
    print("Scroll delta:", event.delta) # event.delta indica a direção da rolagem: positivo (cima), negativo (baixo)

root.bind("<MouseWheel>", scroll) # No Linux, o scroll pode ser <Button-4> (cima) e <Button-5> (baixo)
________________________________________________________________________________________
5. Evento em widget específico:

entrada = Entry(root)
entrada.pack()

def entrou(event):
    print("Cursor entrou na caixa de texto")

entrada.bind("<Enter>", entrou)
________________________________________________________________________________________
Adicionar um exemplo com Entry (campo de digitação) detectando tecla dentro do campo:

entrada = tk.Entry(root)
entrada.pack()

def tecla_na_entry(event):
    texto.set(f"Tecla na Entry: {event.char}")

entrada.bind("<Key>", tecla_na_entry)
________________________________________________________________________________________
Dicas Importantes
O evento é sempre passado como argumento para sua função, mesmo que você não use.

O foco do teclado precisa estar na janela ou widget para capturar eventos de tecla.

Para usar várias combinações (Ctrl, Shift, etc.) use:

root.bind("<Control-Key-a>", funcao)
root.bind("<Shift-Key-A>", funcao)

Combinações de Teclas

<Control-Key-x>     Ctrl + X
<Shift-Key-Up>      Shift + Seta cima
<Alt-Key-Return>    Alt + Enter
<Control-Alt-s>     Ctrl + Alt + S
________________________________________________________________________________________

"""

# =========================================
# INÍCIO DA INTERFACE
# =========================================
root = tk.Tk()
root.title("Exemplos do .bind() no Tkinter")
root.geometry("400x350")

# =========================================
# VARIÁVEL DINÂMICA PARA MOSTRAR RESULTADOS
# =========================================
texto = tk.StringVar()
texto.set("Aguardando interação...")

# =========================================
# LABEL DE INSTRUÇÕES
# =========================================
instrucoes = tk.Label(
    root,
    text="Interaja com o TECLADO e o MOUSE para ver os eventos capturados",
    font="Arial 10", fg="blue"
)
instrucoes.pack(pady=5)

# =========================================
# LABEL QUE EXIBE RESULTADOS DOS EVENTOS
# =========================================
label_dinamico = tk.Label(
    root,
    textvariable=texto,
    font="Arial 14",
    bg="white",
    width=40,
    height=4,
    relief="solid"
)
label_dinamico.pack(pady=10)

# =========================================
# WIDGET PARA DETECTAR ENTRADA E SAÍDA DO MOUSE
# =========================================
caixa = tk.Label(
    root,
    text="Passe o mouse aqui",
    bg="lightgray",
    width=25,
    height=3,
    relief="groove"
)
caixa.pack(pady=10)

# =========================================
# FUNÇÕES PARA CADA EVENTO
# =========================================

# ▶ Detecta qualquer tecla pressionada
def tecla_pressionada(event):
    texto.set(f"Tecla pressionada: {event.keysym}")

# ▶ Detecta as setas do teclado e mostra direção
def seta_direcional(event):
    direcao = {
        'Up': '↑ CIMA',
        'Down': '↓ BAIXO',
        'Left': '← ESQUERDA',
        'Right': '→ DIREITA'
    }
    if event.keysym in direcao:
        texto.set(f"Seta pressionada: {direcao[event.keysym]}")

# ▶ Detecta clique do botão esquerdo do mouse
def clique_mouse(event):
    texto.set(f"Clique com o botão ESQUERDO em: ({event.x}, {event.y})")

# ▶ Detecta movimentação do mouse sobre a janela
def movimento_mouse(event):
    texto.set(f"Mouse movendo-se em: ({event.x}, {event.y})")

# ▶ Detecta rolagem com a rodinha do mouse
def scroll_mouse(event):
    if event.delta > 0:
        texto.set("Rolando para CIMA")
    else:
        texto.set("Rolando para BAIXO")

# ▶ Detecta quando o mouse entra no widget
def entrar_widget(event):
    texto.set("Mouse entrou na CAIXA!")

# ▶ Detecta quando o mouse sai do widget
def sair_widget(event):
    texto.set("Mouse saiu da CAIXA!")

# =========================================
# .BIND — VINCULANDO EVENTOS ÀS FUNÇÕES
# =========================================

# --- Eventos gerais de teclado ---
root.bind("<Key>", tecla_pressionada)

# --- Setas direcionais ---
root.bind("<Up>", seta_direcional)
root.bind("<Down>", seta_direcional)
root.bind("<Left>", seta_direcional)
root.bind("<Right>", seta_direcional)

# --- Clique com o botão esquerdo do mouse ---
root.bind("<Button-1>", clique_mouse)

# --- Movimento do mouse sobre a janela ---
root.bind("<Motion>", movimento_mouse)

# --- Scroll do mouse (rodinha) ---
root.bind("<MouseWheel>", scroll_mouse)

# --- Entrar e sair do widget "caixa" ---
caixa.bind("<Enter>", entrar_widget)
caixa.bind("<Leave>", sair_widget)

# =========================================
# LOOP PRINCIPAL DA JANELA
# =========================================
root.mainloop()
