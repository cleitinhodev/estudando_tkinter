import tkinter as tk

# Spinbox é um widget do Tkinter que permite ao usuário selecionar um valor
# entre um intervalo ou uma lista pré-definida, utilizando setas (para cima e para baixo).

root = tk.Tk()
root.title("Exemplos de Spinbox")
root.geometry("300x200")  # Define o tamanho da janela

# ---------- EXEMPLO 1: Spinbox com intervalo numérico ----------
# from_ = valor inicial
# to = valor final
# increment = quanto aumenta ou diminui a cada clique (padrão é 1)
# wrap = se True, volta ao início após chegar ao final (e vice-versa)
# state = 'readonly' impede digitação manual
# command = função chamada ao mudar o valor (não funciona perfeitamente em todos os sistemas)

s1 = tk.Spinbox(root,
                from_=0,
                to=10,
                increment=1,
                wrap=False,
                font=("Arial", 12),
                width=10)
s1.pack(pady=5)

# ---------- EXEMPLO 2: Spinbox com valores fixos numéricos ----------
# values = tupla de opções personalizadas (números ou textos)
# wrap = se True, ao chegar no fim volta pro início

s2 = tk.Spinbox(root,
                values=(10, 20, 30, 40, 50),
                wrap=True,
                font=("Arial", 12),
                width=10)
s2.pack(pady=5)

# ---------- EXEMPLO 3: Spinbox com valores de texto ----------
# Também pode ser usado com strings (útil para nomes, dias da semana, meses etc.)

s3 = tk.Spinbox(root,
                values=('João', 'Carlos', 'Maria', 'Ana'),
                wrap=True,
                font=("Arial", 12),
                width=10)
s3.pack(pady=5)

# ---------- Função para obter o valor selecionado ----------
def ver_valor():
    print("Valor atual do Spinbox 3:", s3.get())  # .get() retorna o valor atual selecionado

# ---------- Botão para testar a leitura do Spinbox ----------
btn = tk.Button(root,
                text='Ver Item Selecionado',
                command=ver_valor,
                font=("Arial", 10))
btn.pack(pady=10)

root.mainloop()
