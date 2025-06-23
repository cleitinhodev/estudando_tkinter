import tkinter as tk

# --- 1. Função de Callback Centralizada ---
# Esta função será chamada por todos os Checkbuttons quando clicados.
# Ela demonstra como acessar o valor das variáveis de controle.
def mostrar_estado_dos_checkbuttons():
    print("\n--- Estado Atual dos Checkbuttons ---")

    # Acessando o valor do Checkbutton INT
    valor_int = minha_int_var.get()
    print(f"Checkbutton INT (valor: 0 ou 1): {valor_int}")

    # Acessando o valor do Checkbutton STRING
    valor_str = minha_str_var.get()
    print(f"Checkbutton STRING (valor: 'ATIVO' ou 'INATIVO'): {valor_str}")

    # Acessando o valor do Checkbutton BOOLEAN
    valor_bool = minha_bool_var.get()
    print(f"Checkbutton BOOLEAN (valor: True ou False): {valor_bool}")

    # Acessando o valor do Checkbutton "Botão de Alternância"
    valor_toggle = toggle_var.get()
    print(f"Checkbutton 'Botão de Alternância' (valor: 0 ou 1): {valor_toggle}")
    print("--------------------------------------")


# --- 2. Configuração da Janela Principal (root) ---
root = tk.Tk()
root.title("Estudo Completo do Checkbutton no Tkinter")
root.geometry("500x400") # Define um tamanho inicial para a janela


# --- 3. Declaração das Variáveis de Controle ---
# Essas variáveis do Tkinter 'guardam' o estado (marcado/desmarcado) de cada Checkbutton.

# Para Checkbutton que retorna um número inteiro (0 ou 1 por padrão)
minha_int_var = tk.IntVar()
# Você pode definir um valor inicial se quiser. Ex: minha_int_var.set(1) para começar marcado.

# Para Checkbutton que retorna uma string específica
minha_str_var = tk.StringVar()
# Definimos valores on/off string abaixo no Checkbutton.

# Para Checkbutton que retorna True ou False
minha_bool_var = tk.BooleanVar()
# Você pode definir um valor inicial. Ex: minha_bool_var.set(True) para começar marcado.

# Para o Checkbutton que atua como um botão de alternância
toggle_var = tk.IntVar()


# --- 4. Criação e Configuração dos Checkbuttons ---

# Checkbutton Padrão com IntVar (valores 0 ou 1)
# Atributos focados em texto e vinculação de variável
check_int_padrao = tk.Checkbutton(root,
                                  text="Opção 1: Padrão (valor INT 0/1)",
                                  variable=minha_int_var,
                                  command=mostrar_estado_dos_checkbuttons, # Chama a função ao clicar
                                  font=("Helvetica", 10, "bold"))
check_int_padrao.pack(pady=5, anchor="w") # 'pady' para espaçamento, 'anchor="w"' para alinhar à esquerda


# Checkbutton com StringVar e valores customizados
# Atributos focados em cores e texto
check_string_custom = tk.Checkbutton(root,
                                     text="Opção 2: Recebe 'SIM' ou 'NÃO'",
                                     variable=minha_str_var,
                                     onvalue="SIM",    # Valor quando marcado
                                     offvalue="NÃO",   # Valor quando desmarcado
                                     command=mostrar_estado_dos_checkbuttons,
                                     fg="darkblue",      # Cor do texto
                                     bg="lightyellow",   # Cor de fundo
                                     activebackground="lightblue", # Cor de fundo ao passar o mouse
                                     selectcolor="green", # Cor do indicador quando selecionado
                                     relief=tk.RIDGE,    # Estilo de borda
                                     bd=2)               # Largura da borda
check_string_custom.pack(pady=5, anchor="w")


# Checkbutton com BooleanVar e aparência personalizada
# Atributos focados na cor do indicador e espaçamento
check_boolean = tk.Checkbutton(root,
                               text="Opção 3: Retorna True/False",
                               variable=minha_bool_var,
                               command=mostrar_estado_dos_checkbuttons,
                               selectcolor="purple",  # Cor do quadrado quando selecionado
                               padx=10,                # Espaçamento interno horizontal
                               pady=5,                 # Espaçamento interno vertical
                               cursor="hand2")         # Altera o cursor do mouse
check_boolean.pack(pady=5, anchor="w")


# Checkbutton transformado em um "Botão de Alternância"
# `indicatoron=False` remove o quadradinho tradicional.
# A mudança de cor de fundo indica o estado.
check_toggle_button = tk.Checkbutton(root,
                                     text="Opção 4: Botão de Alternância",
                                     variable=toggle_var,
                                     command=mostrar_estado_dos_checkbuttons,
                                     indicatoron=False,  # NÃO mostra o quadradinho!
                                     width=30,           # Define uma largura fixa em caracteres
                                     height=2,           # Define uma altura fixa em linhas
                                     bg="lightgrey",
                                     selectcolor="darkgreen", # Cor de fundo quando selecionado
                                     fg="black",
                                     activebackground="grey", # Cor de fundo ao passar o mouse
                                     font=("Arial", 12))
check_toggle_button.pack(pady=10) # Um pouco mais de espaço para este


# --- 5. Iniciar o Loop Principal da Aplicação ---
root.mainloop()
