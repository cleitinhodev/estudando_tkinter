import tkinter as tk

# Criando a janela principal (objeto da classe Tk)
root = tk.Tk()
root.title("Exemplo de Estudo")
root.geometry("300x200")  # Atributo: define o tamanho da janela

# ==== OBJETO ====
# Criamos um botão chamado btn_login, que é um OBJETO da classe Button
btn_login = tk.Button(
    root,                 # O botão está dentro da janela principal (root)
    text="Login",         # Atributo: define o texto que aparece no botão
    bg="lightblue",       # Atributo: define a cor de fundo do botão
    font=("Arial", 12),   # Atributo: define a fonte e o tamanho
    command=lambda: print("Você clicou no botão!")  # EVENTO: ação ao clicar
)

# ==== MÉTODO ====
# O método .pack() posiciona o botão na tela
btn_login.pack(pady=20)

# ==== OUTRO OBJETO ====
# Criamos um rótulo (label) para mostrar texto
lbl_info = tk.Label(
    root,
    text="Clique no botão para fazer login",  # Atributo
    fg="green",                               # Atributo: cor do texto
    font=("Helvetica", 10)                    # Atributo: fonte
)

# Método para posicionar o rótulo
lbl_info.pack(pady=10)

# ==== MÉTODO EXTRA ====
# Podemos mudar os atributos depois usando .config() (método)
lbl_info.config(text="Esperando ação do usuário...")

# ==== MÉTODO DE LOOP ====
# Mantém a janela aberta, esperando eventos do usuário
root.mainloop()