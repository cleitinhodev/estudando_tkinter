import tkinter as tk

# Criando a janela principal
root = tk.Tk()
root.title("Exemplo completo de Variáveis Tkinter")
root.geometry("400x500")

'''
No Tkinter, usamos "variáveis especiais" chamadas StringVar, IntVar, DoubleVar e BooleanVar
para criar dados que podem ser conectados diretamente aos widgets da interface.

Essas variáveis são úteis quando queremos que os widgets atualizem automaticamente seus valores
sem precisarmos reconfigurá-los manualmente.
'''

# VARIÁVEIS
texto = tk.StringVar()
numero_inteiro = tk.IntVar()
numero_decimal = tk.DoubleVar()
valor_booleano = tk.BooleanVar()

# DEFININDO VALORES INICIAIS
texto.set("Olá, mundo!")
numero_inteiro.set(10)
numero_decimal.set(3.14)
valor_booleano.set(True)

# LABELS
tk.Label(root, text="Texto (StringVar):", font=("Arial", 12)).pack()
label_texto = tk.Label(root, textvariable=texto, font=("Arial", 14), fg="blue")
label_texto.pack()

tk.Label(root, text="Número Inteiro (IntVar):", font=("Arial", 12)).pack()
label_int = tk.Label(root, textvariable=numero_inteiro, font=("Arial", 14), fg="green")
label_int.pack()

tk.Label(root, text="Número Decimal (DoubleVar):", font=("Arial", 12)).pack()
label_float = tk.Label(root, textvariable=numero_decimal, font=("Arial", 14), fg="purple")
label_float.pack()

tk.Label(root, text="Valor Booleano (BooleanVar):", font=("Arial", 12)).pack()
label_bool = tk.Label(root, textvariable=valor_booleano, font=("Arial", 14), fg="red")
label_bool.pack()

# ENTRADA DE TEXTO COM StringVar (ligada em tempo real)
tk.Label(root, text="Digite algo:", font=("Arial", 12)).pack()
entrada_texto = tk.Entry(root, textvariable=texto, font=("Arial", 12))
entrada_texto.pack()

# SPINBOX para mudar o número inteiro (IntVar)
tk.Label(root, text="Escolha um número inteiro:", font=("Arial", 12)).pack()
spinbox = tk.Spinbox(root, from_=0, to=100, textvariable=numero_inteiro, font=("Arial", 12))
spinbox.pack()

# SLIDER para número decimal (DoubleVar)
tk.Label(root, text="Controle deslizante (float):", font=("Arial", 12)).pack()
slider = tk.Scale(root, from_=0, to=10, resolution=0.1, orient="horizontal", variable=numero_decimal)
slider.pack()

# CHECKBUTTON com BooleanVar
check = tk.Checkbutton(root, text="Ativado/Desativado", variable=valor_booleano, font=("Arial", 12))
check.pack()

# BOTÃO para modificar tudo manualmente
def alterar_tudo():
    texto.set("Texto alterado!")
    numero_inteiro.set(numero_inteiro.get() + 1)
    numero_decimal.set(numero_decimal.get() + 0.5)
    valor_booleano.set(not valor_booleano.get())  # inverte True/False

tk.Button(root, text="Alterar tudo manualmente", command=alterar_tudo, font=("Arial", 12)).pack(pady=10)

# EXIBINDO VALORES EM TEMPO REAL COM UM MÉTODO UPDATE
def atualizar_label_extra():
    valor_ao_vivo = f"""
Texto: {texto.get()}
Inteiro: {numero_inteiro.get()}
Decimal: {numero_decimal.get()}
Booleano: {valor_booleano.get()}
"""
    label_ao_vivo.config(text=valor_ao_vivo)
    root.after(500, atualizar_label_extra)  # atualiza a cada 0.5 segundos

label_ao_vivo = tk.Label(root, text="", justify="left", font=("Courier", 10))
label_ao_vivo.pack(pady=10)
atualizar_label_extra()  # chama a primeira vez

# Inicia a interface
root.mainloop()
