from tkinter import *

# Criação da janela principal
root = Tk()
root.title('Centralizar Janela')

# ------------------------------
# DIMENSIONAMENTO DA JANELA
# ------------------------------

# Tamanho da janela (largura x altura)
largura = 300
altura = 200

# ------------------------------
# RESOLUÇÃO DA TELA
# ------------------------------

# Captura a largura total da tela
largura_screen = root.winfo_screenwidth()

# Captura a altura total da tela
altura_screen = root.winfo_screenheight()

# Apenas para fins de verificação, imprime a resolução da tela
print(f'Resolução da tela: {largura_screen}x{altura_screen}')

# ------------------------------
# CÁLCULO DA POSIÇÃO CENTRAL
# ------------------------------

# Calcula a posição X e Y para centralizar a janela na tela
# Fórmula: (resolução / 2) - (tamanho da janela / 2)
posicao_x = int(largura_screen / 2 - largura / 2)
posicao_y = int(altura_screen / 2 - altura / 2)

# Exibe a posição calculada apenas para conferência
print(f'Posição da janela: x={posicao_x}, y={posicao_y}')

# ------------------------------
# APLICANDO TAMANHO E POSIÇÃO
# ------------------------------

# Define tamanho e posição da janela com o método geometry()
# Sintaxe: 'larguraxaltura+posição_x+posição_y'
root.geometry(f'{largura}x{altura}+{posicao_x}+{posicao_y}')

# Inicia o loop principal da aplicação
root.mainloop()
