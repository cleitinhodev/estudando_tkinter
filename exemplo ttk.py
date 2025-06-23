import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Comparação: tk vs ttk")
root.geometry("900x600")

# Frames de separação
frame_tk = tk.LabelFrame(root, text="tk (Tradicional)", padx=10, pady=10)
frame_ttk = tk.LabelFrame(root, text="ttk (Moderno)", padx=10, pady=10)
frame_tk.pack(side="left", fill="both", expand=True, padx=10, pady=10)
frame_ttk.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# Widgets tk tradicionais
tk.Label(frame_tk, text="Label").pack(pady=2)
tk.Entry(frame_tk).pack(pady=2)
tk.Button(frame_tk, text="Button").pack(pady=2)
tk.Checkbutton(frame_tk, text="Checkbutton").pack(pady=2)
tk.Radiobutton(frame_tk, text="Radiobutton").pack(pady=2)
tk.Scale(frame_tk, from_=0, to=10, orient="horizontal").pack(pady=2)
tk.Listbox(frame_tk, height=3).pack(pady=2)
tk.Text(frame_tk, height=3, width=20).pack(pady=2)

# Widgets ttk modernos
ttk.Label(frame_ttk, text="Label").pack(pady=2)
ttk.Entry(frame_ttk).pack(pady=2)
ttk.Button(frame_ttk, text="Button").pack(pady=2)
ttk.Checkbutton(frame_ttk, text="Checkbutton").pack(pady=2)
ttk.Radiobutton(frame_ttk, text="Radiobutton").pack(pady=2)
ttk.Scale(frame_ttk, from_=0, to=10, orient="horizontal").pack(pady=2)
ttk.Combobox(frame_ttk, values=["Opção 1", "Opção 2"]).pack(pady=2)
ttk.Progressbar(frame_ttk, length=100, mode='determinate').pack(pady=2)

root.mainloop()

