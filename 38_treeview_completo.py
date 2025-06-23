import tkinter as tk
from tkinter import ttk

# Cria a janela principal
root = tk.Tk()
root.title("Treeview Exemplo")       # Título da janela
root.geometry("400x250")             # Tamanho da janela

# -----------------------------------------
# 🌳 Criando o widget Treeview
# -----------------------------------------

# O widget Treeview permite criar tabelas, listas hierárquicas (tipo árvore), ou exibição tabular de dados.
# A opção "columns" define as colunas que vamos exibir (sem incluir a coluna especial "#0").
# O parâmetro show="headings" oculta a coluna especial "#0" e mostra apenas os cabeçalhos das colunas que criamos.

tree = ttk.Treeview(
    root,
    columns=("Nome", "Idade"),  # Define duas colunas de dados
    show="headings"             # Exibe apenas os cabeçalhos (sem coluna raiz "#0")
)

# -----------------------------------------
# 🏷️ Configurando os cabeçalhos da tabela
# -----------------------------------------

tree.heading("Nome", text="Nome")     # Define o título da coluna "Nome"
tree.heading("Idade", text="Idade")   # Define o título da coluna "Idade"

# Opcional: ajustar o tamanho de cada coluna
tree.column("Nome", width=150, anchor="w")   # "w" = alinhado à esquerda
tree.column("Idade", width=100, anchor="center")

# -----------------------------------------
# 📥 Inserindo dados na tabela
# -----------------------------------------

# Sintaxe: insert(pai, posição, id_opcional, text_opcional, valores)
# "" → significa sem pai (nível raiz)
# "end" → insere ao final da lista
# values → corresponde às colunas definidas em "columns"

tree.insert("", "end", values=("João", 25))
tree.insert("", "end", values=("Maria", 30))
tree.insert("", "end", values=("Carlos", 22))

# -----------------------------------------
# 📦 Adicionando a Treeview na janela
# -----------------------------------------

tree.pack(expand=True, fill='both')  # Expande para preencher o espaço da janela

# -----------------------------------------
# 🔁 Inicia o loop da interface
# -----------------------------------------

root.mainloop()


"""
📘 Explicação completa dos principais elementos:
🔤 columns=("Nome", "Idade")
Define os nomes internos das colunas. Esses nomes são usados no heading() e column().

🎯 show="headings"
Exibe apenas os títulos definidos por você. Se você remover essa opção, uma coluna adicional padrão chamada #0 aparecerá à esquerda.

🧾 tree.heading(coluna, text="Título")
Define o texto visível do cabeçalho da coluna.

🔢 tree.column(coluna, width, anchor)
width: largura da coluna (em pixels)

anchor: alinhamento do texto

"w" (left), "e" (right), "center"

📥 tree.insert(pai, posição, values=...)
pai: se estiver vazio "", o item é raiz. Para hierarquias, use o ID de outro item como pai.

posição: "end" ou um índice (insere na posição especificada)

values: tupla com os dados das colunas






🔄 Interação: Pegando item selecionado

def ver_selecao():
    item = tree.focus()                  # Pega o item atualmente selecionado
    valores = tree.item(item)["values"] # Extrai os dados do item
    print("Selecionado:", valores)

btn = ttk.Button(root, text="Ver Seleção", command=ver_selecao)
btn.pack(pady=5)






🧱 Adicionando Scrollbar (quando tiver muitos dados):

scroll = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscroll=scroll.set)
scroll.pack(side="right", fill="y")






Estrutura hierárquica (estilo árvore):
Se quiser usar a coluna especial #0 (padrão), tire show="headings" e use text= nos insert():

tree = ttk.Treeview(root)
tree.insert("", "end", text="Item Pai")
tree.insert("", "end", text="Outro Item")






| Função                        | Descrição                          |
| ----------------------------- | ---------------------------------- |
| `tree.get_children()`         | Retorna todos os itens             |
| `tree.delete(item)`           | Remove item                        |
| `tree.item(item, values=...)` | Atualiza valores                   |
| `tree.selection()`            | Retorna IDs dos itens selecionados |
| `tree.focus()`                | Retorna o item com foco            |

"""