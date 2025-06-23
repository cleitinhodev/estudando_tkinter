from tkinter import *

'''
ENTRY NO TKINTER – GUIA DEFINITIVO
-----------------------------------

O widget `Entry` é usado para criar uma **caixa de entrada de texto de uma linha**.

É ideal para:
✅ Formulários (usuário, senha, email).
✅ Entrada de dados numéricos ou textuais.
✅ Campos de busca e pesquisa.
✅ Interação direta com o usuário.

Atributos comuns do Entry:
--------------------------
- master: O widget pai (root, frame etc).
- width: Largura da caixa de texto (em caracteres, não pixels).
- font: Fonte do texto (nome, tamanho e estilo).
- bg / background: Cor de fundo.
- fg / foreground: Cor do texto.
- bd / borderwidth: Largura da borda.
- relief: Tipo da borda (FLAT, RAISED, SUNKEN, GROOVE, RIDGE).
- show: Esconde os caracteres (ex: show="*" para senhas).
- justify: Alinhamento do texto (LEFT, CENTER, RIGHT).
- state: NORMAL (editável) ou DISABLED (não editável).
- insertbackground: Cor do cursor de digitação.
- highlightcolor: Cor da borda quando recebe foco.
- highlightthickness: Espessura da borda de foco.
- exportselection: Se True, seleciona texto ao copiar com Ctrl+C.

Métodos úteis do Entry:
-----------------------
- .get() → Retorna o conteúdo da caixa.
- .insert(posição, texto) → Insere texto (posição 0 = início, END = fim).
- .delete(início, fim) → Remove texto entre posições.
- .config() → Altera atributos dinamicamente.
- .focus() → Define o foco inicial.
- .icursor(posição) → Move o cursor para uma posição específica.
- .select_range(início, fim) → Seleciona parte do texto.
- .selection_clear() → Cancela seleção.
- .selection_present() → Retorna se há texto selecionado (True/False).

EXEMPLO PRÁTICO COMPLETO:
'''

# Janela principal
root = Tk()
root.title("Exemplo Completo de Entry")
root.geometry("450x300")
root.config(bg="#f0f0f0")

# Função que será chamada ao clicar no botão
def exibir_dados():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    resultado.config(text=f"Usuário: {usuario}\nSenha: {senha}")

# Labels informativos
Label(root, text="Usuário:", font=("Arial", 11)).place(x=30, y=30)
Label(root, text="Senha:", font=("Arial", 11)).place(x=30, y=80)

# Caixa de entrada de texto para usuário
entrada_usuario = Entry(
    root,
    width=30,
    font=("Arial", 11),
    fg="black",
    bg="#e8f5e9",
    bd=2,
    relief=GROOVE,
    highlightcolor="green",
    highlightthickness=1,
    insertbackground="black"
)
entrada_usuario.place(x=120, y=30)
entrada_usuario.insert(0, "Digite seu nome")  # Texto inicial
entrada_usuario.select_range(0, END)          # Seleciona tudo
entrada_usuario.focus()                       # Foco inicial

# Caixa de entrada para senha
entrada_senha = Entry(
    root,
    width=30,
    font=("Arial", 11),
    fg="black",
    bg="#fce4ec",
    bd=2,
    relief=GROOVE,
    show="*",                     # Oculta os caracteres (senha)
    insertbackground="black"
)
entrada_senha.place(x=120, y=80)

# Botão de ação
Button(
    root,
    text="Entrar",
    font=("Arial", 10),
    command=exibir_dados
).place(x=200, y=130)

# Label para exibir resultado
resultado = Label(root, text="", font=("Arial", 11), fg="blue")
resultado.place(x=120, y=180)

'''
DICAS AVANÇADAS:
----------------
✅ Você pode usar StringVar() para vincular variáveis e facilitar atualizações.
✅ Use validatecommand e validate para validar em tempo real (ex: números apenas).
✅ O método .after() pode ser usado para detectar texto ao vivo.
✅ Use o evento "<Return>" para ativar algo quando o usuário pressionar Enter.

Exemplo rápido de Enter:
entrada_usuario.bind("<Return>", lambda e: exibir_dados())

'''

# Iniciando o loop da interface
root.mainloop()
