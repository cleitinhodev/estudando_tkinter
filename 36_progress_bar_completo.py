# Importa o Tkinter e os widgets modernos do ttk
import tkinter as tk
from tkinter import ttk

# Importa a biblioteca time para simular o tempo de processamento
import time

# Criação da janela principal
root = tk.Tk()
root.title("Progressbar Exemplo")   # Título da janela
root.geometry("300x150")            # Tamanho da janela (largura x altura)

# -------------------------------------------
# 🌟 Criando a barra de progresso (Progressbar)
# -------------------------------------------

pb = ttk.Progressbar(
    root,              # Janela ou frame onde a barra será exibida
    orient="horizontal",  # Orientação da barra: "horizontal" ou "vertical"
    length=200,        # Comprimento da barra em pixels
    mode="determinate" # Modo da barra: "determinate" ou "indeterminate"
)
pb.pack(pady=20)  # Adiciona a barra à janela com espaçamento vertical

# Explicação dos principais atributos:
# - orient: Direção da barra. "horizontal" (padrão) ou "vertical"
# - length: Tamanho da barra em pixels
# - mode:
#   - "determinate": valor controlado, você define o progresso
#   - "indeterminate": uso contínuo sem valor definido (ex: carregando...)

# ---------------------------------------------------
# 📦 Função que simula um processo com barra de progresso
# ---------------------------------------------------

def iniciar_progresso():
    pb["maximum"] = 100   # Define o valor máximo da barra
    pb["value"] = 0       # Reinicia a barra no começo
    for i in range(101):  # Vai de 0 até 100
        pb["value"] = i   # Atualiza o valor atual
        root.update_idletasks()  # Atualiza a interface gráfica
        time.sleep(0.01)         # Simula tempo de espera (10ms)

# ------------------------------------------
# 🔘 Botão que inicia o processo
# ------------------------------------------

btn = ttk.Button(root, text="Iniciar", command=iniciar_progresso)
btn.pack()

# ------------------------------------------
# 🚀 Inicia o loop principal da interface
# ------------------------------------------
root.mainloop()


"""
Exemplo com modo "indeterminate" (sem valor definido):

pb = ttk.Progressbar(root, orient="horizontal", length=200, mode="indeterminate")
pb.pack(pady=20)

def carregar_indefinido():
    pb.start(10)  # Inicia animação (10 = velocidade)
    root.after(3000, pb.stop)  # Para após 3 segundos

ttk.Button(root, text="Carregar", command=carregar_indefinido).pack()






Personalizando a aparência (avançado):
Você pode mudar a cor da barra com ttk.Style:

style = ttk.Style()
style.configure("custom.Horizontal.TProgressbar", foreground='blue', background='green')

pb = ttk.Progressbar(root, style="custom.Horizontal.TProgressbar", ...)
"""