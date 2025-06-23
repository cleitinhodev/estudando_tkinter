# Importa a biblioteca Tkinter com o apelido 'tk'
import tkinter as tk

'''
1. Criar a janela principal:
   - A janela principal é o "container" onde todos os widgets (botões, labels, etc.) serão colocados.
   - É comum dar o nome 'root' para essa janela, pois ela é a "raiz" da interface.
'''

root = tk.Tk()  # Cria a janela principal (objeto da classe Tk)

# Define o título da janela, que aparece na barra superior
root.title('Título Simples')

'''
2. Iniciar o loop principal da interface:
   - O método mainloop() mantém a janela aberta e escutando eventos (cliques, teclado, etc.).
   - Sem ele, a janela abriria e fecharia imediatamente.
'''

root.mainloop()



