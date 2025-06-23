import tkinter as tk

def mostrar_menu(event):
    try:
        menu_popup.tk_popup(event.x_root, event.y_root)
    finally:
        menu_popup.grab_release()

def copiar():
    try:
        area_de_texto.event_generate("<<Copy>>")
    except:
        pass

def colar():
    try:
        area_de_texto.event_generate("<<Paste>>")
    except:
        pass

def recortar():
    try:
        area_de_texto.event_generate("<<Cut>>")
    except:
        pass

def selecionar_tudo():
    area_de_texto.tag_add("sel", "1.0", "end")

# Janela principal
root = tk.Tk()
root.title("Exemplo com menu de contexto")

# Área de texto
area_de_texto = tk.Text(root, wrap="word", font=("Arial", 12))
area_de_texto.pack(expand=True, fill="both")

# Criar menu de contexto
menu_popup = tk.Menu(root, tearoff=0)
menu_popup.add_command(label="Copiar", command=copiar)
menu_popup.add_command(label="Colar", command=colar)
menu_popup.add_command(label="Recortar", command=recortar)
menu_popup.add_separator()
menu_popup.add_command(label="Selecionar Tudo", command=selecionar_tudo)

# Associar o menu ao botão direito do mouse
area_de_texto.bind("<Button-3>", mostrar_menu)  # Windows e Linux
area_de_texto.bind("<Button-2>", mostrar_menu)  # MacOS usa <Button-2>

root.mainloop()
