import tkinter as tk

# Função para mostrar o menu de contexto da caixa de texto
def mostrar_menu_texto(event):
    # Exibe o menu exatamente na posição do mouse
    menu_texto.tk_popup(event.x_root, event.y_root)

# Função para mostrar o menu de contexto da label
def mostrar_menu_label(event):
    menu_label.tk_popup(event.x_root, event.y_root)

# Função genérica que detecta onde foi o clique com botão direito
def clique_direito_geral(event):
    widget = event.widget  # Widget onde o clique aconteceu

    # Se clicou na caixa de texto, mostra o menu da caixa de texto
    if widget == caixa_texto:
        mostrar_menu_texto(event)

    # Se clicou na label, mostra o menu da label
    elif widget == label_info:
        mostrar_menu_label(event)

    # Caso contrário, não mostra nenhum menu
    else:
        print("Clique com botão direito fora dos widgets com menu. Nada será mostrado.")

# Cria a janela principal
root = tk.Tk()
root.title("Exemplo de Menus com Botão Direito")
root.geometry("500x300")

# ================================
# CRIANDO WIDGETS
# ================================

# Caixa de texto com rolagem
caixa_texto = tk.Text(root, height=10, wrap="word", font=("Arial", 12))
caixa_texto.pack(padx=10, pady=10, fill="both", expand=True)

# Label que também terá um menu diferente
label_info = tk.Label(root, text="Clique com o botão direito aqui também!", bg="lightgray", font=("Arial", 10))
label_info.pack(padx=10, pady=10, fill="x")

# Frame vazio só para mostrar que não faz nada ao clicar fora
frame_vazio = tk.Frame(root, height=50, bg="white")
frame_vazio.pack(fill="both", expand=True)

# ================================
# CRIANDO OS MENUS
# ================================

# Menu de contexto da caixa de texto
menu_texto = tk.Menu(root, tearoff=0)
menu_texto.add_command(label="Copiar", command=lambda: root.clipboard_append(caixa_texto.get("sel.first", "sel.last")))
menu_texto.add_command(label="Colar", command=lambda: caixa_texto.insert("insert", root.clipboard_get()))
menu_texto.add_command(label="Limpar", command=lambda: caixa_texto.delete("1.0", "end"))

# Menu de contexto da label
menu_label = tk.Menu(root, tearoff=0)
menu_label.add_command(label="Ação especial", command=lambda: print("Ação feita na label!"))

# ================================
# APLICANDO OS BINDS
# ================================

# Bind para o botão direito em toda a janela (detecta cliques em qualquer widget)
root.bind("<Button-3>", clique_direito_geral)

# Você também pode fazer binds específicos assim:
# caixa_texto.bind("<Button-3>", mostrar_menu_texto)
# label_info.bind("<Button-3>", mostrar_menu_label)

# Inicia a interface
root.mainloop()
