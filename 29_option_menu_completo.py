import tkinter as tk
from tkinter import font

# Função chamada quando a opção for alterada
def opcao_selecionada(*args):
    print("Opção selecionada:", variavel_opcao.get())
    label_resultado.config(text=f"Você escolheu: {variavel_opcao.get()}")

# Função chamada ao clicar no botão
def mostrar_opcao():
    print("Opção atual:", variavel_opcao.get())

# Criando a janela principal
root = tk.Tk()
root.title("Exemplo Completo de OptionMenu")
root.geometry("400x250")
root.config(bg="#f0f0f0")

# Criando uma StringVar para armazenar a opção selecionada
variavel_opcao = tk.StringVar()
variavel_opcao.set("Selecione uma linguagem")  # Valor inicial
variavel_opcao.trace_add("write", opcao_selecionada)  # Detecta mudança automática

# Lista de opções
opcoes = ["Python", "Java", "C++", "JavaScript", "Ruby", "Go", "Kotlin"]

# Criando o OptionMenu
option_menu = tk.OptionMenu(root, variavel_opcao, *opcoes)
option_menu.pack(pady=20)

# Personalizando o botão principal do OptionMenu
option_menu.config(
    bg="#dff0d8",            # Cor de fundo do botão
    fg="black",              # Cor do texto do botão
    font=("Arial", 12, "bold"),
    width=25,                # Largura do botão (em caracteres)
    highlightthickness=2,    # Espessura da borda de foco
    highlightbackground="gray",
    relief="raised",         # Estilo da borda (flat, groove, raised, ridge, solid, sunken)
    borderwidth=2
)

# Personalizando o menu suspenso (acessando diretamente o submenu interno)
submenu = option_menu["menu"]
submenu.config(
    bg="white",              # Cor de fundo da lista suspensa
    fg="black",              # Cor do texto da lista
    font=("Arial", 10),
    activebackground="lightblue",  # Cor de fundo ao passar o mouse
    activeforeground="black"       # Cor do texto ao passar o mouse
)

# Label que mostra a escolha atual
label_resultado = tk.Label(root, text="Escolha algo acima...", font=("Arial", 14), bg="#f0f0f0")
label_resultado.pack(pady=10)

# Botão para mostrar a escolha atual
btn_ver = tk.Button(root, text="Mostrar Escolha", command=mostrar_opcao)
btn_ver.pack(pady=5)

# Exemplo extra: mudar a lista de opções dinamicamente
def atualizar_opcoes():
    nova_lista = ["HTML", "CSS", "SQL"]
    menu = option_menu["menu"]
    menu.delete(0, "end")  # Remove opções atuais
    for item in nova_lista:
        menu.add_command(label=item, command=lambda value=item: variavel_opcao.set(value))

btn_atualizar = tk.Button(root, text="Atualizar Opções", command=atualizar_opcoes)
btn_atualizar.pack(pady=5)

root.mainloop()
