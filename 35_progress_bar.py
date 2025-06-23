import tkinter as tk
from tkinter import ttk

import time  # usado para simular progresso

root = tk.Tk()
root.title("Progressbar Exemplo")
root.geometry("300x150")

pb = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
pb.pack(pady=20)

def iniciar_progresso():
    pb["maximum"] = 100
    for i in range(101):
        pb["value"] = i
        root.update_idletasks()
        time.sleep(0.01)  # simula tempo de processamento

btn = ttk.Button(root, text="Iniciar", command=iniciar_progresso)
btn.pack()

root.mainloop()