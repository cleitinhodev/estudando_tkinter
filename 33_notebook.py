import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Notebook Exemplo")
root.geometry("300x200")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# Abas
aba1 = ttk.Frame(notebook)
aba2 = ttk.Frame(notebook)

notebook.add(aba1, text='Página 1')
notebook.add(aba2, text='Página 2')

ttk.Label(aba1, text="Conteúdo da Aba 1").pack(pady=20)
ttk.Label(aba2, text="Conteúdo da Aba 2").pack(pady=20)

root.mainloop()
