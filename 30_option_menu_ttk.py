import tkinter as tk
from tkinter import ttk

# Função chamada quando a opção muda (modo automático)
def ao_alterar(event):
    print("Alterado para:", combo.get())
    label.config(text=f"Selecionado: {combo.get()}")

# Função chamada por botão
def mostrar_escolha():
    print("Valor atual:", combo.get())

# Janela principal
root = tk.Tk()
root.title("Exemplo Completo de Combobox")
root.geometry("400x250")
root.config(bg="#f0f0f0")

# Estilo personalizado usando ttk.Style
style = ttk.Style()
style.theme_use('default')  # Outros temas: 'clam', 'alt', 'classic'
style.configure("TCombobox",
                fieldbackground="#ffffff",   # Fundo do campo selecionado
                background="#e6f2ff",        # Fundo da lista suspensa
                foreground="black",
                font=("Arial", 11))

# Lista de opções
opcoes = ["Python", "Java", "C++", "JavaScript", "Ruby", "Go", "Kotlin"]

# Criando a Combobox
combo = ttk.Combobox(root,
                     values=opcoes,
                     state="readonly",     # "normal", "readonly", ou "disabled"
                     font=("Arial", 11),
                     width=30)

combo.set("Selecione uma linguagem")  # Valor inicial (pode usar também current(0))
combo.pack(pady=20)

# Associando evento automático
combo.bind("<<ComboboxSelected>>", ao_alterar)

# Label para exibir escolha
label = tk.Label(root, text="Nada selecionado ainda", font=("Arial", 13), bg="#f0f0f0")
label.pack(pady=10)

# Botão para mostrar a opção atual
btn = tk.Button(root, text="Ver Seleção", command=mostrar_escolha)
btn.pack()

# Atualizar as opções dinamicamente
def atualizar_opcoes():
    nova_lista = ["HTML", "CSS", "SQL"]
    combo['values'] = nova_lista
    combo.set("Selecione novamente")

btn2 = tk.Button(root, text="Atualizar Opções", command=atualizar_opcoes)
btn2.pack(pady=5)

root.mainloop()
