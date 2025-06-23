from tkinter import *

# Criação da janela principal
root = Tk()
root.title("Comando com e sem argumentos")

# ======================== SEM ARGUMENTOS ========================
'''
Quando usamos uma função sem argumentos no botão, podemos passar **apenas o nome da função**
no parâmetro `command`, sem parênteses. Isso porque queremos que o botão chame 
essa função **somente quando for clicado**, e não ao criar o botão.
'''

def dizer_ola():
    print('Olá Mundo')

# Aqui o botão está configurado para chamar a função dizer_ola quando for clicado.
btn_sem_arg = Button(root, text='Executar (sem argumento)', command=dizer_ola)
btn_sem_arg.pack(pady=10)

# ======================== COM ARGUMENTOS ========================
'''
Quando queremos chamar uma função que **recebe argumentos**, não podemos simplesmente passar algo como:
    command=funcao(argumento)
porque isso faria a função ser executada **imediatamente** na criação do botão.

Para evitar isso, usamos o `lambda:` que cria uma **função anônima temporária**, chamada só quando o botão for clicado.
'''

def dizer_algo(texto):
    print(texto)

# Aqui usamos lambda para passar o argumento "Nova Mensagem"
btn_com_arg = Button(root, text='Executar (com argumento)', command=lambda: dizer_algo("Nova Mensagem"))
btn_com_arg.pack(pady=10)

# Também podemos usar lambda para funções simples diretamente, sem nem criar uma função separada:
btn_print_direto = Button(root, text='Imprimir Mensagem Direta', command=lambda: print("Mensagem Direta!"))
btn_print_direto.pack(pady=10)

# ======================== EXPLICAÇÃO EXTRA SOBRE LAMBDA ========================
'''
🧠 O que é `lambda`?
Lambda é uma forma de criar **funções curtas e anônimas**.
Ela funciona como uma mini função que você escreve direto no lugar onde precisa.

Exemplo:
lambda: print("Olá")         -> Cria uma função que imprime "Olá"
lambda x: x*2                -> Cria uma função que retorna o dobro de x
lambda nome: print(f"Oi {nome}")  -> Cria uma função que imprime algo com o nome

Usamos muito lambda em botões quando precisamos:
✔️ Passar argumentos para a função
✔️ Fazer pequenas ações sem criar uma função separada
✔️ Combinar várias funções
'''

# ======================== INICIAR A JANELA ========================
root.mainloop()
