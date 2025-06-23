import tkinter as tk

"""
O after basicamente agente a função enquanto continua executando as outras normalmente.
"""

def mostrar_mensagem():
    print("Mensagem mostrada depois de 3 segundos!")
    label.config(text="3 segundos se passaram")

def clique_imediato():
    print("Botão clicado instantaneamente!")
    label.config(text="Você clicou!")

# Janela principal
root = tk.Tk()
root.geometry("300x150")

label = tk.Label(root, text="Aguardando...", font=("Arial", 14))
label.pack(pady=10)

# Botão que agenda uma ação para depois
btn_after = tk.Button(root, text="Esperar 3 segundos", command=lambda: root.after(3000, mostrar_mensagem))
btn_after.pack(pady=5)

# Botão que funciona imediatamente
btn_rapido = tk.Button(root, text="Clique instantâneo", command=clique_imediato)
btn_rapido.pack(pady=5)

root.mainloop()
