import tkinter as tk

root = tk.Tk()
root.geometry('300x200')

'''
StringVar é um objeto do Tkinter que simula uma variável em tempo real,
muito útil para interações na nossa GUI. Aqui temos algumas formas de
mostrá-la na janela. Primeiro, criamos o objeto e usamos o método set()
para definir o valor inicial que será usado. Depois, em um Label ou 
qualquer outro widget compatível, podemos exibir esse valor de duas formas:
usando o método get() para obter o valor atual, ou diretamente com o 
atributo textvariable.
'''

texto = tk.StringVar()
texto.set('Abacaxi')

texto2 = tk.StringVar()
texto2.set('Batata')

label1 = tk.Label(root, text=texto.get(), font='Arial 20', bg='red', fg='white')
label1.pack()

label2 = tk.Label(root, textvariable=texto2, font='Arial 20', bg='red', fg='white')
label2.pack()

label3 = tk.Label(root, textvariable=texto2, font='Arial 20', bg='red', fg='white')
label3.pack()

'''
A vantagem de usar textvariable é que podemos alterar o valor em tempo real
e todos os widgets que usam essa mesma variável serão atualizados
automaticamente, sem precisar alterar um por um.
'''


def alterar_valores():
    texto2.set('Alface')


btn = tk.Button(root, text='Alterar Batata', command=alterar_valores)
btn.pack()

'''
Esse método também é ótimo para criar atualizações dinâmicas,
como medidores, relógios ou exibição de dados que mudam constantemente.
'''

root.mainloop()
