# Importa o Tkinter padrão e a versão 'ttk' com widgets modernos
import tkinter as tk
from tkinter import ttk

# Cria a janela principal
root = tk.Tk()
root.title("Notebook Exemplo")    # Define o título da janela
root.geometry("300x200")          # Define o tamanho da janela (largura x altura)

# Cria o widget Notebook (as abas)
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')
# expand=True permite que o notebook cresça com a janela
# fill='both' faz com que o notebook preencha horizontal e verticalmente o espaço disponível

# Cria duas abas (são Frames que serão "páginas" do notebook)
aba1 = ttk.Frame(notebook)
aba2 = ttk.Frame(notebook)

# Adiciona as abas ao notebook com rótulos/texto visíveis
notebook.add(aba1, text='Página 1')
notebook.add(aba2, text='Página 2')

# Conteúdo da primeira aba
label1 = ttk.Label(aba1, text="Conteúdo da Aba 1")
label1.pack(pady=20)  # Espaçamento vertical para afastar do topo

# Conteúdo da segunda aba
label2 = ttk.Label(aba2, text="Conteúdo da Aba 2")
label2.pack(pady=20)

# Inicia o loop principal da interface gráfica
root.mainloop()


"""
Estrutura básica:
ttk.Notebook(): Cria o widget de abas.

ttk.Frame(): Cada aba é um Frame, que é uma "área" onde você pode colocar outros widgets.

notebook.add(frame, text="Nome da Aba"): Adiciona uma aba ao notebook.

pack(expand=True, fill='both'): Faz com que o notebook cresça e se ajuste com a janela.






Você pode adicionar qualquer coisa dentro das abas:
Botões, campos de texto, labels, gráficos, listas etc.

Exemplo:

ttk.Button(aba1, text="Clique aqui").pack(pady=10)






Detectar mudança de aba (opcional avançado):
Você pode detectar quando o usuário muda de aba assim:

def ao_mudar_aba(event):
    indice = notebook.index(notebook.select())  # índice da aba selecionada
    print(f"Aba atual: {indice + 1}")

notebook.bind("<<NotebookTabChanged>>", ao_mudar_aba)






Para criar muitas abas dinamicamente:

for i in range(5):
    aba = ttk.Frame(notebook)
    notebook.add(aba, text=f"Aba {i+1}")
    ttk.Label(aba, text=f"Conteúdo da Aba {i+1}").pack(pady=10)
"""