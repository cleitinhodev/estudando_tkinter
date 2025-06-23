import tkinter as tk

root = tk.Tk()
root.geometry('300x200')

def iniciar_file():
    print('Ajuda sobre o Programa')


meu_menu = tk.Menu(root)                             # O menu é iniciado aqui, mas deve ser configurado lá embaixo

file_menu = tk.Menu(meu_menu, tearoff=0)             # Criamos o menu interno dentro do meu_menu tearoff é para
                                                     # não deixar a janela em cascada ser arrastada
file_menu.add_command(label="New")                   # Aqui criamos os itens desse menu file
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_command(label="Exit")
meu_menu.add_cascade(label="File", menu=file_menu)   # Aqui é onde os itens criados são adicionados ao file_menu

meu_menu.add_command(label="Help", command=iniciar_file)    # Esse aqui é um menu isolado com só um item e função.


root.config(menu=meu_menu)                        # Fazendo o root reconhecer o menu
root.mainloop()
