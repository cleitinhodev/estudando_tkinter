import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Treeview Exemplo")
root.geometry("400x250")

# Criando o Treeview
tree = ttk.Treeview(root, columns=("Nome", "Idade"), show="headings")
tree.heading("Nome", text="Nome")
tree.heading("Idade", text="Idade")

# Inserindo dados
tree.insert("", "end", values=("João", 25))
tree.insert("", "end", values=("Maria", 30))
tree.insert("", "end", values=("Carlos", 22))

tree.pack(expand=True, fill='both')

root.mainloop()
