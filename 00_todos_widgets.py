import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Exemplo com 25 Widgets Tkinter e ttk")
root.geometry("900x700")

# Canvas com barra de rolagem vertical para comportar muitos widgets
canvas = tk.Canvas(root)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Função para facilitar a criação dos labels de título
def add_title(text):
    label = ttk.Label(scrollable_frame, text=text, font=('Arial', 12, 'bold'))
    label.pack(pady=(15, 5), anchor='w')

def add_desc(text):
    label = ttk.Label(scrollable_frame, text=text, font=('Arial', 9, 'italic'))
    label.pack(pady=(0, 5), anchor='w')

# 1. Button (tkinter)
add_title("1. Button (Tkinter)")
btn_tk = tk.Button(scrollable_frame, text="Botão Tkinter")
btn_tk.pack()

# 2. Button (ttk)
add_title("2. Button (ttk)")
btn_ttk = ttk.Button(scrollable_frame, text="Botão ttk")
btn_ttk.pack()

# 3. Canvas (tkinter) - área para desenho
add_title("3. Canvas (Tkinter)")
canvas_widget = tk.Canvas(scrollable_frame, width=150, height=60, bg="white", relief="sunken", borderwidth=1)
canvas_widget.create_line(0,0,150,60, fill="blue", width=3)
canvas_widget.pack()

# 4. Checkbutton (tkinter)
add_title("4. Checkbutton (Tkinter)")
var_check = tk.IntVar()
chk_tk = tk.Checkbutton(scrollable_frame, text="Checkbutton Tkinter", variable=var_check)
chk_tk.pack()

# 5. Checkbutton (ttk)
add_title("5. Checkbutton (ttk)")
var_chk_ttk = tk.IntVar()
chk_ttk = ttk.Checkbutton(scrollable_frame, text="Checkbutton ttk", variable=var_chk_ttk)
chk_ttk.pack()

# 6. Entry (tkinter)
add_title("6. Entry (Tkinter)")
entry_tk = tk.Entry(scrollable_frame)
entry_tk.insert(0, "Entrada Tkinter")
entry_tk.pack()

# 7. Entry (ttk)
add_title("7. Entry (ttk)")
entry_ttk = ttk.Entry(scrollable_frame)
entry_ttk.insert(0, "Entrada ttk")
entry_ttk.pack()

# 8. Frame (tkinter)
add_title("8. Frame (Tkinter)")
frame_tk = tk.Frame(scrollable_frame, bg="lightgray", width=150, height=50, relief="sunken", borderwidth=1)
frame_tk.pack_propagate(False)
tk.Label(frame_tk, text="Frame Tkinter").pack()
frame_tk.pack()

# 9. Frame (ttk)
add_title("9. Frame (ttk)")
frame_ttk = ttk.Frame(scrollable_frame, width=150, height=50)
frame_ttk.pack_propagate(False)
ttk.Label(frame_ttk, text="Frame ttk").pack()
frame_ttk.pack()

# 10. Label (tkinter)
add_title("10. Label (Tkinter)")
label_tk = tk.Label(scrollable_frame, text="Label Tkinter")
label_tk.pack()

# 11. Label (ttk)
add_title("11. Label (ttk)")
label_ttk = ttk.Label(scrollable_frame, text="Label ttk")
label_ttk.pack()

# 12. LabelFrame (tkinter)
add_title("12. LabelFrame (Tkinter)")
lf_tk = tk.LabelFrame(scrollable_frame, text="LabelFrame Tkinter")
tk.Label(lf_tk, text="Conteúdo aqui").pack()
lf_tk.pack(pady=5, fill="x")

# 13. LabelFrame (ttk)
add_title("13. LabelFrame (ttk)")
lf_ttk = ttk.Labelframe(scrollable_frame, text="LabelFrame ttk")
ttk.Label(lf_ttk, text="Conteúdo aqui").pack()
lf_ttk.pack(pady=5, fill="x")

# 14. Listbox (tkinter)
add_title("14. Listbox (Tkinter)")
listbox = tk.Listbox(scrollable_frame, height=4)
for item in ["Item 1", "Item 2", "Item 3"]:
    listbox.insert("end", item)
listbox.pack()

# 15. Menu (tkinter) - só aparece na barra de menus da janela, por isso só texto explicativo
add_title("15. Menu (Tkinter)")
add_desc("O widget Menu cria menus na barra de janelas, não é mostrado aqui.")

# 16. Menubutton (tkinter)
add_title("16. Menubutton (Tkinter)")
menubtn = tk.Menubutton(scrollable_frame, text="Menubutton")
menu = tk.Menu(menubtn, tearoff=0)
menu.add_command(label="Opção 1")
menu.add_command(label="Opção 2")
menubtn.config(menu=menu)
menubtn.pack()

# 17. Message (tkinter)
add_title("17. Message (Tkinter)")
message = tk.Message(scrollable_frame, text="Message widget para texto longo e quebrado automaticamente.", width=200)
message.pack()

# 18. Radiobutton (tkinter)
add_title("18. Radiobutton (Tkinter)")
var_radio = tk.StringVar()
rb1 = tk.Radiobutton(scrollable_frame, text="Opção A", variable=var_radio, value="A")
rb2 = tk.Radiobutton(scrollable_frame, text="Opção B", variable=var_radio, value="B")
rb1.pack()
rb2.pack()

# 19. Scale (tkinter)
add_title("19. Scale (Tkinter)")
scale = tk.Scale(scrollable_frame, from_=0, to=10, orient="horizontal")
scale.pack()

# 20. Scrollbar (tkinter)
add_title("20. Scrollbar (Tkinter)")
# Para scrollbar funcionar precisa estar associada a algo, usaremos uma Listbox
listbox2 = tk.Listbox(scrollable_frame, height=4)
for i in range(20):
    listbox2.insert("end", f"Item {i+1}")
scrollbar2 = tk.Scrollbar(scrollable_frame, orient="vertical", command=listbox2.yview)
listbox2.config(yscrollcommand=scrollbar2.set)
listbox2.pack(side="left", fill="y")
scrollbar2.pack(side="left", fill="y")

# 21. Text (tkinter)
add_title("21. Text (Tkinter)")
text = tk.Text(scrollable_frame, height=4, width=30)
text.insert("end", "Este é um widget de texto multilinha.")
text.pack()

# 22. Spinbox (tkinter)
add_title("22. Spinbox (Tkinter)")
spin = tk.Spinbox(scrollable_frame, from_=0, to=5)
spin.pack()

# 23. Combobox (ttk)
add_title("23. Combobox (ttk)")
combo = ttk.Combobox(scrollable_frame, values=["Opção 1", "Opção 2", "Opção 3"])
combo.current(0)
combo.pack()

# 24. Notebook (ttk)
add_title("24. Notebook (ttk)")

notebook = ttk.Notebook(scrollable_frame)
aba1 = ttk.Frame(notebook)
aba2 = ttk.Frame(notebook)
notebook.add(aba1, text="Aba 1")
notebook.add(aba2, text="Aba 2")
notebook.pack(fill="x", pady=5)
ttk.Label(aba1, text="Conteúdo da Aba 1").pack()
ttk.Label(aba2, text="Conteúdo da Aba 2").pack()

# 25. Progressbar (ttk)
add_title("25. Progressbar (ttk)")
progress = ttk.Progressbar(scrollable_frame, orient="horizontal", length=150, mode="determinate")
progress["value"] = 40
progress.pack(pady=5)

root.mainloop()
