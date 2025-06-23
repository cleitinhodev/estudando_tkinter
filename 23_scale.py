"""
Scale é um tipo de widget que é usado para capturar a escala de alguma coisa,
imagine uma barra de volume que ao movermos aumenta ou diminui de 0 a 100.
podemos definir vários detalhes.
"""

import tkinter as tk

# Função chamada automaticamente toda vez que o Scale é movido
def ver_valor(valor):
    print(f"Valor atual (ao mover): {valor}")

# Função chamada ao clicar no botão, pegando o valor atual do Scale manualmente
def ver_valor_pelo_botao():
    print(f"Valor atual (pelo botão): {volume.get()}")

# Criação da janela principal
root = tk.Tk()
root.title("Exemplo de Scale (barra deslizante)")

# Criação do Scale
volume = tk.Scale(
    root,                     # Janela onde o Scale será inserido
    from_=0,                  # Valor mínimo da escala
    to=100,                   # Valor máximo da escala
    orient=tk.HORIZONTAL,     # Orientação: HORIZONTAL ou VERTICAL
    resolution=0.5,           # Incremento dos valores (0.5 permite decimais)
    tickinterval=10,          # Mostra marcas de intervalo a cada 10 unidades
    length=300,               # Tamanho da barra em pixels
    label="Volume",           # Texto acima do Scale
    showvalue=True,           # Exibe o valor atual ao lado do cursor
    sliderlength=20,          # Tamanho do "botão" deslizante
    troughcolor='lightgray',  # Cor da trilha (barra de fundo)
    fg='blue',                # Cor do texto da label
    bg='white',               # Cor de fundo do widget
    font=('Arial', 10, 'bold'),  # Fonte do texto
    command=ver_valor         # Função chamada automaticamente ao mover
)
volume.set(50)  # Define valor inicial (opcional)
volume.pack(pady=10)

# Botão para exibir valor atual do Scale manualmente
btn = tk.Button(root, text='Mostrar Valor', command=ver_valor_pelo_botao)
btn.pack(pady=10)

# Inicia o loop da interface
root.mainloop()