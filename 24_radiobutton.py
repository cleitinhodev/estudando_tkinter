import tkinter as tk

# Funções associadas a cada opção de gênero
def diga_oi_M():
    print('Olá Amigo')

def diga_oi_F():
    print('Olá Amiga')

def diga_oi_O():
    print('Olá Amigx')

# Criação da janela principal
root = tk.Tk()
root.title("Exemplo de RadioButton")
root.geometry("300x300")  # Define o tamanho da janela

# Variável que armazenará o valor selecionado
genero = tk.StringVar()
genero.set("Masculino")  # Valor padrão inicial selecionado

# Criando os Radiobuttons
gen_1 = tk.Radiobutton(
    root,
    text='Masculino',          # Texto exibido ao lado do botão
    variable=genero,           # Variável de controle (todos compartilham a mesma)
    value='Masculino',         # Valor que será armazenado se este botão for selecionado
    command=diga_oi_M,         # Função chamada quando o botão for clicado
    bg='lightblue',            # Cor de fundo
    fg='black',                # Cor do texto
    font=('Arial', 12),        # Fonte
    activebackground='blue',   # Cor de fundo ao passar o mouse
    activeforeground='white',  # Cor do texto ao passar o mouse
    selectcolor='white',       # Cor do círculo interno quando selecionado
    anchor='w',                # Alinhamento do conteúdo
    padx=10, pady=5            # Espaço interno
)
gen_1.pack(anchor='w', padx=20)

gen_2 = tk.Radiobutton(
    root,
    text='Feminino',
    variable=genero,
    value='Feminino',
    command=diga_oi_F,
    bg='lightpink',
    fg='black',
    font=('Arial', 12),
    activebackground='deeppink',
    activeforeground='white',
    selectcolor='white',
    anchor='w',
    padx=10, pady=5
)
gen_2.pack(anchor='w', padx=20)

gen_3 = tk.Radiobutton(
    root,
    text='Outro',
    variable=genero,
    value='Outro',
    command=diga_oi_O,
    bg='lightgray',
    fg='black',
    font=('Arial', 12),
    activebackground='gray',
    activeforeground='white',
    selectcolor='white',
    anchor='w',
    padx=10, pady=5
)
gen_3.pack(anchor='w', padx=20)

# Label que exibe o valor atual selecionado
visor = tk.Label(
    root,
    textvariable=genero,  # Exibe dinamicamente o valor selecionado
    font=('Arial', 16, 'bold'),
    pady=10
)
visor.pack()

# Botão para mostrar o valor no console
def ver_valor():
    print(f"Gênero selecionado: {genero.get()}")

btn = tk.Button(root, text='Ver Gênero', command=ver_valor)
btn.pack(pady=10)

# Loop principal
root.mainloop()
