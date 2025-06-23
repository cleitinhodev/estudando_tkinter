import tkinter as tk
from tkinter import ttk

# Criação da janela principal
root = tk.Tk()
root.title("Combobox Exemplo")       # Define o título da janela
root.geometry("300x200")             # Define o tamanho da janela

# Função chamada quando o botão é clicado
def ver_opcao():
    valor = combobox.get()           # Obtém o valor selecionado na Combobox
    print(f"Selecionado via botão: {valor}")
    label_resultado.config(text=f"Você escolheu: {valor}")

# Função chamada automaticamente ao mudar a seleção na Combobox
def ao_mudar_opcao(event):
    valor = combobox.get()
    print(f"Selecionado automaticamente: {valor}")
    label_resultado.config(text=f"Selecionado: {valor}")

# Criação da Combobox com quatro opções
combobox = ttk.Combobox(
    root,
    values=["Python", "Java", "C++", "JavaScript"],
    state="readonly"  # Impede digitação manual, permitindo apenas seleção
)
combobox.current(0)                  # Define a opção padrão (primeira da lista)
combobox.pack(pady=10)

# Vincula o evento de mudança de seleção à função ao_mudar_opcao
combobox.bind("<<ComboboxSelected>>", ao_mudar_opcao)

# Botão que exibe a opção selecionada quando clicado
btn = ttk.Button(root, text="Ver Opção", command=ver_opcao)
btn.pack(pady=5)

# Label que mostrará o resultado na própria janela
label_resultado = ttk.Label(root, text="Você escolheu: Python")
label_resultado.pack(pady=10)

# Inicia o loop da interface gráfica
root.mainloop()

"""
Ao contrário de widgets como Button (que têm o argumento command), 
a Combobox do ttk no Tkinter não possui um argumento command direto.

Para detectar quando o usuário muda a seleção da Combobox, 
você deve usar o método bind() com o evento especial <<ComboboxSelected>>.
"""
