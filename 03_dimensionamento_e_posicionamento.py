import tkinter as tk  # Importa a biblioteca tkinter com um apelido (tk)

# CRIAÇÃO DA JANELA PRINCIPAL
root = tk.Tk()
root.title('Redimensionamento e Posicionamento')  # Define o título da janela

# TAMANHO E POSIÇÃO INICIAL DA JANELA
'''
O método geometry() define o tamanho e a posição inicial da janela na tela.

Formato: 'largura x altura + pos_x + pos_y'
- largura e altura definem o tamanho da janela.
- pos_x e pos_y definem onde ela será posicionada na tela ao abrir.

Exemplo abaixo: 500x250 pixels, abrindo a 1000px da esquerda e 100px do topo da tela.
'''
root.geometry('500x250+1000+100')

# PERMITIR OU BLOQUEAR REDIMENSIONAMENTO DA JANELA
'''
O método resizable() controla se o usuário pode redimensionar a janela manualmente.

Argumentos:
- True: permite redimensionar
- False: impede redimensionar

resizable(width, height)
'''
root.resizable(True, True)  # Pode ser redimensionada tanto na largura quanto na altura

# LIMITES DE REDIMENSIONAMENTO
'''
Define os limites mínimo e máximo de redimensionamento da janela.

- minsize(width, height): tamanho mínimo permitido
- maxsize(width, height): tamanho máximo permitido

Essas configurações só fazem efeito se resizable estiver ativado.
'''
root.minsize(width=400, height=200)
root.maxsize(width=700, height=400)

# ESTADO INICIAL DA JANELA (opcional)
'''
Controla o estado da janela ao iniciar:

- 'normal' (padrão)
- 'iconic' (minimizada)
- 'zoomed' (maximizada - funciona no Windows)
'''
# root.state('iconic')   # Descomente para iniciar minimizada
# root.state('zoomed')   # Descomente para iniciar maximizada

# ÍCONE PERSONALIZADO DA JANELA
'''
O método iconbitmap() permite definir um ícone personalizado para a janela.

Importante:
- O arquivo deve estar no formato .ico
- Forneça o caminho correto para o arquivo

Exemplo:
root.iconbitmap('meu_icone.ico')
'''
# root.iconbitmap('caminho_para_o_icone.ico')  # Substitua pelo caminho do seu ícone

# INICIA O LOOP PRINCIPAL
'''
O mainloop() é o coração da interface. Ele mantém a janela aberta
e ativa para responder a eventos como cliques e teclas.
'''
root.mainloop()
