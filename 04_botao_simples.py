'''
import tkinter as tk

root = tk.Tk()
root.title('Novo Botão')


btn = tk.Button(root,
    text='Clique aqui',              # Texto exibido no botão
    command=alguma_funcao,           # Função que será executada ao clicar
    width=20,                        # Largura do botão (em caracteres)
    height=2,                        # Altura do botão (em linhas de texto)
    padx=10,                         # Espaço interno horizontal (padding interno no X)
    pady=5,                          # Espaço interno vertical (padding interno no Y)
    relief='raised',                # Tipo de borda: flat, raised, sunken, ridge, solid, groove
    bd=3,                            # Espessura da borda (borderwidth)
    fg='white',                      # Cor do texto (foreground)
    bg='blue',                       # Cor de fundo do botão (background)
    activeforeground='yellow',       # Cor do texto quando o botão é clicado
    activebackground='black',        # Cor de fundo quando o botão é clicado
    font=('Arial', 12, 'bold'),      # Fonte, tamanho e estilo do texto
    anchor='center',                 # Alinhamento do texto: n, ne, e, se, s, sw, w, nw, center
    cursor='hand2',                  # Tipo de cursor do mouse ao passar por cima
    image=alguma_imagem,             # Insere uma imagem (PhotoImage) no botão
    compound='left',                 # Se estiver usando imagem + texto: top, bottom, left, right, center
    state='normal',                  # Estado do botão: normal, disabled, active
    underline=0,                     # Sublinha o caractere no índice indicado (0 é o primeiro caractere)
    wraplength=100,                  # Quebra de linha automática se o texto ultrapassar esse valor (em pixels)
    takefocus=True                  # Se o botão pode receber foco ao usar TAB
)

root.mainloop()
'''

import tkinter as tk

def exemplo_callback():
    print("Você clicou!")

root = tk.Tk()
root.title("Botão Tkinter Completo")
root.geometry("700x500")

# (Opcional) Criar imagem se quiser usar nos testes (substitua por caminho válido se necessário)
# imagem_exemplo = tk.PhotoImage(file="icone.png")

# BOTÃO COMPLETO COM TODOS OS ATRIBUTOS CONHECIDOS
btn = tk.Button(root,

    # TEXTO
    text='Clique Aqui',             # Texto exibido no botão
    font=('Arial', 12, 'bold'),     # Fonte usada no botão
    underline=0,                    # Sublinha o caractere na posição do índice
    wraplength=150,                 # Comprimento máximo antes de quebrar o texto

    # TAMANHO
    width=20,                       # Largura (em caracteres)
    height=2,                       # Altura (em linhas de texto)

    # ESPAÇAMENTO
    padx=10,                        # Espaçamento interno lateral
    pady=5,                         # Espaçamento interno vertical

    # POSICIONAMENTO DO TEXTO
    anchor='center',               # Alinhamento interno (n, ne, e, se, s, sw, w, nw, center)
    justify='center',              # Justificação de múltiplas linhas de texto (left, center, right)

    # CORES
    fg='white',                    # Cor do texto
    bg='blue',                     # Cor de fundo
    activeforeground='yellow',     # Cor do texto quando ativo
    activebackground='black',      # Cor de fundo quando ativo
    disabledforeground='gray',     # Cor do texto quando desativado
    highlightbackground='red',     # Cor da borda externa quando não focado (macOS)
    highlightcolor='orange',       # Cor da borda quando em foco
    highlightthickness=2,          # Espessura da borda de foco

    # BORDA
    bd=4,                          # Espessura da borda
    relief='ridge',                # Estilo da borda: flat, raised, sunken, groove, ridge, solid

    # ESTADO
    state='normal',                # Estado: normal, disabled, active

    # CURSOR E FOCO
    cursor='hand2',                # Cursor ao passar por cima
    takefocus=True,                # Permite ou não foco via teclado (Tab)

    # IMAGEM (descomente se tiver imagem)
    # image=imagem_exemplo,        # Exibe uma imagem no botão
    # compound='left',             # Combina imagem + texto: top, bottom, left, right, center, none

    # FUNCIONALIDADE
    command=exemplo_callback,      # Função executada ao clicar

    # IDENTIFICADORES E CLASSES (menos usados, mas existem)
    name='botao_exemplo',          # Nome interno do widget (não visível)
    #class_='CustomButton',         # Classe de estilo usada pelo gerenciador de temas (geralmente ignorado no Tkinter puro)

)

btn.pack(pady=20)

'''
Observações:
✔️ Muitos atributos acima são específicos de sistema (ex: highlightbackground no macOS).
✔️ Alguns raramente são usados, mas são suportados.
✔️ Outros como imagem requerem arquivos válidos.
✔️ Alguns funcionam apenas em determinados estilos de tema.
✔️ Alguns nomes (como class_) têm sublinhado final porque "class" é palavra reservada do Python.
'''

root.mainloop()
