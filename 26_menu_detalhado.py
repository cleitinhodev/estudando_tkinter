import tkinter as tk
from tkinter import messagebox

# Funções para os comandos dos menus
def novo_arquivo():
    print("Novo arquivo criado")

def abrir_arquivo():
    print("Abrir arquivo existente")

def salvar_arquivo():
    print("Arquivo salvo")

def sair_do_programa():
    root.quit()  # Fecha a aplicação

def ajuda_sobre():
    messagebox.showinfo("Ajuda", "Este é um exemplo completo de menu no Tkinter.")

def sobre_autor():
    messagebox.showinfo("Sobre", "Criado por alguém apaixonado por Python!")

# Criação da janela principal
root = tk.Tk()
root.title("Exemplo Completo de Menu")
root.geometry("400x300")

# ============================
# INICIANDO O MENU PRINCIPAL
# ============================
menu_principal = tk.Menu(root)  # Menu principal que será aplicado ao root

# =============================
# MENU FILE (Arquivo)
# =============================
menu_arquivo = tk.Menu(menu_principal, tearoff=0)  # tearoff=0 impede a janelinha destacável
menu_arquivo.add_command(label="Novo", command=novo_arquivo, accelerator="Ctrl+N")
menu_arquivo.add_command(label="Abrir", command=abrir_arquivo, accelerator="Ctrl+O")
menu_arquivo.add_command(label="Salvar", command=salvar_arquivo, accelerator="Ctrl+S")
menu_arquivo.add_separator()  # Linha separadora
menu_arquivo.add_command(label="Sair", command=sair_do_programa, accelerator="Ctrl+Q")

menu_principal.add_cascade(label="Arquivo", menu=menu_arquivo)  # Adiciona o menu "Arquivo" à barra principal

# =============================
# MENU AJUDA
# =============================
menu_ajuda = tk.Menu(menu_principal, tearoff=0)
menu_ajuda.add_command(label="Ajuda sobre o Programa", command=ajuda_sobre)
menu_ajuda.add_command(label="Sobre o Autor", command=sobre_autor)

menu_principal.add_cascade(label="Ajuda", menu=menu_ajuda)

# =============================
# MENU EDITAR COM SUBMENU
# =============================
menu_editar = tk.Menu(menu_principal, tearoff=0)

# Submenu de opções
submenu_estilo = tk.Menu(menu_editar, tearoff=0)
submenu_estilo.add_command(label="Tema Claro")
submenu_estilo.add_command(label="Tema Escuro")
menu_editar.add_cascade(label="Temas", menu=submenu_estilo)

menu_editar.add_command(label="Desfazer", state="disabled")  # Item desabilitado

menu_principal.add_cascade(label="Editar", menu=menu_editar)

# =============================
# APLICANDO O MENU AO ROOT
# =============================
root.config(menu=menu_principal)  # Conecta o menu à janela principal

# =============================
# ATALHOS DE TECLADO (BINDINGS)
# =============================
root.bind('<Control-n>', lambda event: novo_arquivo())
root.bind('<Control-o>', lambda event: abrir_arquivo())
root.bind('<Control-s>', lambda event: salvar_arquivo())
root.bind('<Control-q>', lambda event: sair_do_programa())

# Inicia o loop principal da aplicação
root.mainloop()


"""
formas de personalização:

menu_arquivo = tk.Menu(menu_principal, tearoff=0,
                       font=("Arial", 10),
                       bg="black",
                       fg="white",
                       activebackground="green",
                       activeforeground="white",
                       bd=2,
                       relief="raised")
"""
