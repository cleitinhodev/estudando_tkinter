"""
TopLevel é uma forma prática de abrir uma nova janela junto
com a já existente.
"""

import tkinter as tk

root = tk.Tk()
root.title('Janela Principal')
root.geometry('400x200')


def abrir():
    """Basta colocar a janela nova em uma função ou classe"""
    nova_janela = tk.Toplevel()
    nova_janela.title('Nova Janela')
    nova_janela.geometry('300x150')

    lbn = tk.Label(nova_janela, text='Texto Demonstrativo')
    lbn.pack()


btn = tk.Button(root, text='Abrir Janela', command=abrir)
btn.pack()

root.mainloop()
