# Importa o módulo tkinter e a sub-biblioteca de fontes
import tkinter as tk
from tkinter import font

# Função que insere texto no final do widget Text
def inserir_texto():
    # Insere um texto na última posição (tk.END) com a tag "negrito"
    texto.insert(tk.END, "\nTexto inserido pelo botão.\n", "negrito")

# Função que apaga todo o conteúdo do widget Text
def limpar_texto():
    # Deleta do início (linha 1, coluna 0) até o fim do texto
    texto.delete("1.0", tk.END)

# Função que desabilita a edição no Text (torna apenas leitura)
def desabilitar():
    texto.config(state="disabled")  # Text fica cinza e não-editável

# Função que reabilita a edição do Text
def habilitar():
    texto.config(state="normal")  # Permite editar o texto novamente

# Cria a janela principal do programa
janela = tk.Tk()
janela.title("Widget Text Completo")  # Define o título da janela
janela.geometry("600x400")  # Define o tamanho da janela (largura x altura)

# Cria uma barra de rolagem vertical (scrollbar)
scroll = tk.Scrollbar(janela)
scroll.pack(side=tk.RIGHT, fill=tk.Y)  # Posiciona a scrollbar à direita e preenche verticalmente

# Cria o widget Text com vários parâmetros personalizados
texto = tk.Text(
    janela,  # Janela principal como "pai"
    width=70,  # Largura em número de caracteres
    height=20,  # Altura em número de linhas
    bg="white",  # Cor de fundo
    fg="black",  # Cor do texto
    font=("Arial", 12),  # Fonte usada no texto
    wrap="word",  # Quebra de linha por palavra (evita quebrar palavras no meio)
    padx=10,  # Espaço interno à esquerda e à direita
    pady=10,  # Espaço interno acima e abaixo
    insertbackground="blue",  # Cor do cursor de texto
    selectbackground="lightblue",  # Cor do fundo do texto selecionado
    spacing1=5,  # Espaço antes de um parágrafo
    spacing3=5,  # Espaço depois de um parágrafo
    relief="sunken",  # Tipo de borda ("rebaixada")
    borderwidth=2  # Espessura da borda
)
texto.pack(padx=10, pady=10)  # Adiciona o widget na janela com margens externas

# Configura a scrollbar para controlar a rolagem vertical do Text
scroll.config(command=texto.yview)  # Associa a rolagem do texto à scrollbar
texto.config(yscrollcommand=scroll.set)  # Associa a scrollbar ao widget Text

# Cria uma tag chamada "negrito" com estilo de texto negrito
texto.tag_config("negrito", font=("Arial", 12, "bold"))

# Cria uma tag chamada "vermelho" que deixa o texto vermelho
texto.tag_config("vermelho", foreground="red")

# Cria uma tag chamada "grande" que aumenta o tamanho do texto
texto.tag_config("grande", font=("Arial", 16))

# Insere um texto no início (linha 1, coluna 0) com a tag "grande"
texto.insert("1.0", "Este é um exemplo do widget Text do Tkinter.\n", "grande")

# Insere outro texto no final com a tag "vermelho"
texto.insert(tk.END, "Você pode escrever várias linhas aqui.\n", "vermelho")

# Cria um frame (container) para os botões
frame_botoes = tk.Frame(janela)
frame_botoes.pack()  # Posiciona o frame na janela

# Cria e posiciona um botão que insere texto quando clicado
tk.Button(frame_botoes, text="Inserir", command=inserir_texto).pack(side=tk.LEFT, padx=5)

# Botão que limpa o texto
tk.Button(frame_botoes, text="Limpar", command=limpar_texto).pack(side=tk.LEFT, padx=5)

# Botão que desabilita a edição
tk.Button(frame_botoes, text="Desabilitar", command=desabilitar).pack(side=tk.LEFT, padx=5)

# Botão que reabilita a edição
tk.Button(frame_botoes, text="Habilitar", command=habilitar).pack(side=tk.LEFT, padx=5)

# Inicia o loop principal da interface gráfica
janela.mainloop()
