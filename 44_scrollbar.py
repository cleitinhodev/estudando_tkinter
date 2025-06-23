import tkinter as tk

# Cria a janela principal
janela = tk.Tk()
janela.title("Text com Scrollbar Vertical e Horizontal")
janela.geometry("600x400")  # Tamanho da janela

# Frame para conter o Text e as Scrollbars
frame = tk.Frame(janela)
frame.pack(fill=tk.BOTH, expand=True)

# Scrollbar vertical
scroll_y = tk.Scrollbar(frame, orient=tk.VERTICAL)
scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

# Scrollbar horizontal
scroll_x = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

# Widget Text com scroll configurado
texto = tk.Text(
    frame,
    wrap="none",              # Não quebra linha automaticamente (para horizontal funcionar)
    yscrollcommand=scroll_y.set,  # Associa barra vertical
    xscrollcommand=scroll_x.set,  # Associa barra horizontal
    font=("Courier", 12)      # Fonte com espaçamento fixo para facilitar leitura
)
texto.pack(fill=tk.BOTH, expand=True)  # Expande para ocupar todo o espaço do frame

# Conecta scrollbars ao Text
scroll_y.config(command=texto.yview)
scroll_x.config(command=texto.xview)

# Função para adicionar texto longo
def adicionar_texto():
    for i in range(50):
        texto.insert(tk.END, f"Linha {i+1}: Este é um exemplo de linha muito longa que ultrapassa a largura da janela do Text.\n")

# Botão para adicionar conteúdo
botao = tk.Button(janela, text="Adicionar Texto", command=adicionar_texto)
botao.pack(pady=5)

# Inicia o loop principal da interface
janela.mainloop()
