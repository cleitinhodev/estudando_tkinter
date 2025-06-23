import tkinter as tk

root = tk.Tk()
root.title("Exemplo de OptionMenu")
root.geometry("300x150")

def mostrar(*args):
    print("Você escolheu:", opcao.get())
    if opcao.get() == 'Java':
        print('Ainda não vi essa linguagem')
    elif opcao.get() == 'Python':
        print('Minha favorita!')

# Variável que guarda o valor selecionado
opcao = tk.StringVar()
opcao.set("Escolha uma opção")  # Valor padrão
opcao.trace_add("write", mostrar)

# Criando o OptionMenu com opções
menu_opcoes = tk.OptionMenu(root, opcao, "Python", "Java", "C++", "JavaScript")
menu_opcoes.pack(pady=20)

# Função para exibir a opção selecionada

botao = tk.Button(root, text="Mostrar Opção", command=mostrar)
botao.pack()

root.mainloop()
