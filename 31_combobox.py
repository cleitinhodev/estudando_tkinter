import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Combobox Exemplo")
root.geometry("300x150")

def ver_opcao():
    print(combobox.get())

# Combobox com opções
combobox = ttk.Combobox(root, values=["Python", "Java", "C++", "JavaScript"])
combobox.current(0)  # Define valor padrão
combobox.pack(pady=10)

btn = ttk.Button(root, text="Ver Opção", command=ver_opcao)
btn.pack()

root.mainloop()
