import tkinter as tk
from tkinter import ttk

# Cria a janela principal
janela = tk.Tk()
janela.title("Exemplo básico de Separator")
janela.geometry("400x300")

# Label antes do separador horizontal
label1 = tk.Label(janela, text="Texto acima do separador horizontal")
label1.pack(pady=10)

# Separador horizontal
separator_h = ttk.Separator(janela, orient=tk.HORIZONTAL)
separator_h.pack(fill=tk.X, padx=20, pady=5)  # Preenche horizontalmente com espaço lateral

# Label depois do separador horizontal
label2 = tk.Label(janela, text="Texto abaixo do separador horizontal")
label2.pack(pady=10)

# Frame para demonstrar separador vertical
frame = tk.Frame(janela)
frame.pack(pady=20, fill=tk.BOTH, expand=True)

# Label esquerda no frame
label_esquerda = tk.Label(frame, text="Lado esquerdo")
label_esquerda.pack(side=tk.LEFT, padx=10)

# Separador vertical
separator_v = ttk.Separator(frame, orient=tk.VERTICAL)
separator_v.pack(side=tk.LEFT, fill=tk.Y, padx=10)

# Label direita no frame
label_direita = tk.Label(frame, text="Lado direito")
label_direita.pack(side=tk.LEFT, padx=10)

# Inicia a janela
janela.mainloop()
