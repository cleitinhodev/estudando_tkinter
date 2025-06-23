import tkinter as tk

# Inicializa a janela principal da aplicação Tkinter.
# 'root' é a janela que irá conter todos os outros widgets (elementos gráficos).
root = tk.Tk()
# Define o título da janela principal.
root.title("Exemplo de Listbox no Tkinter")
# Define as dimensões iniciais da janela.
root.geometry("600x600")

# ---
## Entendendo o Listbox Básico

# Cria o primeiro widget Listbox.
# Um Listbox é um widget que exibe uma lista de opções para o usuário.
# O usuário pode selecionar uma ou mais opções da lista.
lista_basica = tk.Listbox(root)
# O método 'pack()' organiza o widget na janela, de forma simples e automática.
# Ele dimensiona o widget para caber em seu conteúdo, o que é útil para layouts rápidos.
lista_basica.pack(pady=10) # 'pady' adiciona um espaçamento vertical acima e abaixo do widget.

# ---
### Inserindo Itens no Listbox

# O método 'insert()' é usado para adicionar itens ao Listbox.
# O primeiro argumento é o índice onde o item será inserido.
# O segundo argumento é o valor do item a ser adicionado.

# Inserindo um item no final da lista.
# 'tk.END' é uma constante especial que representa o final da lista, garantindo que o item seja adicionado por último.
lista_basica.insert(tk.END, 'Terceiro Item da Lista')

# Inserindo um item no início da lista.
# O índice '0' sempre se refere à primeira posição do Listbox.
lista_basica.insert(0, 'Primeiro Item da Lista')

# Inserindo um item em uma posição específica.
# O índice '1' se refere à segunda posição (lembre-se que os índices começam em 0).
lista_basica.insert(1, 'Segundo Item da Lista')

# ---
## Explorando Atributos do Listbox

# Cria um segundo Listbox para demonstrar atributos adicionais.
lista_basica2 = tk.Listbox(
    root,
    # 'selectmode' é um atributo importante que define como a seleção de itens funciona.
    # tk.SINGLE: Permite selecionar apenas um item por vez (padrão).
    # tk.BROWSE: Permite selecionar apenas um item, mas a seleção muda ao arrastar o mouse.
    # tk.MULTIPLE: Permite selecionar vários itens independentemente (clique em cada um).
    # tk.EXTENDED: Permite selecionar múltiplos itens, usando SHIFT para um bloco contínuo
    #              e CTRL para selecionar itens individuais (não contínuos).
    selectmode=tk.EXTENDED,
    # 'height' define o número de linhas visíveis do Listbox.
    # Se o número de itens exceder essa altura, uma barra de rolagem se tornará útil.
    height=8,
    # 'width' define a largura do Listbox em caracteres.
    width=30,
    # 'bg' (background) define a cor de fundo do Listbox.
    bg="#f0f0f0", # Um cinza claro
    # 'fg' (foreground) define a cor do texto dos itens.
    fg="blue",
    # 'font' define a fonte e o tamanho do texto dos itens.
    font=("Arial", 12),
    # 'borderwidth' define a largura da borda ao redor do Listbox.
    borderwidth=2,
    # 'relief' define o estilo da borda.
    # Pode ser 'flat', 'sunken', 'raised', 'groove', 'ridge'.
    relief="groove",
    # 'exportselection' define se a seleção pode ser copiada para outras aplicações.
    # Quando False, a seleção no Listbox não interfere na seleção de outros widgets.
    exportselection=False
)
lista_basica2.pack(pady=10)

# ---
### Inserindo Múltiplos Itens de uma Vez

# É comum ter os itens em uma lista Python e adicioná-los ao Listbox.
nomes = ['João', 'Ana', 'Carlos', 'Maria', 'Manoel', 'Osvaldo', 'Fernanda', 'Gustavo']

# Um loop 'for' é a forma mais eficiente de adicionar vários itens.
for n in nomes:
    lista_basica2.insert(tk.END, n)

# ---
### Deletando Itens do Listbox

# O método 'delete()' remove itens do Listbox.
# Ele pode receber um ou dois argumentos:
# - Se apenas um argumento for passado, ele remove o item no índice especificado.
# - Se dois argumentos forem passados (início e fim), ele remove um intervalo de itens.

# Deletando o item no índice 1 (que é 'Ana' neste caso, pois a lista começa do 0).
lista_basica2.delete(1) # Remove apenas o item no índice 1

# Exemplo de como deletar um intervalo (descomente para testar):
# lista_basica2.delete(0, 2) # Removeria 'João', 'Carlos' e 'Maria' (do índice 0 ao 2)

# ---
## Interagindo com o Listbox: Pegando Itens Selecionados

# É fundamental saber como obter os itens que o usuário selecionou.
# Isso é feito através de um botão ou outro evento.

# Define uma função que será chamada quando o botão for clicado.
def mostrar_nome():
    # 'curselection()' retorna uma tupla de índices dos itens selecionados.
    # É útil quando 'selectmode' é MULTIPLE ou EXTENDED.
    indices_selecionados = lista_basica2.curselection()

    if indices_selecionados: # Verifica se há algum item selecionado
        print("Itens selecionados:")
        for indice in indices_selecionados:
            # 'get(indice)' retorna o valor do item no índice especificado.
            print(lista_basica2.get(indice))
    else:
        print("Nenhum item selecionado.")

    # 'tk.ACTIVE' representa o item que está "ativo" (o item sob o cursor ou o último clicado).
    # Note que 'tk.ACTIVE' pega apenas um item, mesmo com selectmode EXTENDED.
    # Para múltiplos, use 'curselection()'.
    print(f"\nItem ativo (último selecionado ou sob o cursor): {lista_basica2.get(tk.ACTIVE)}")


# Cria um botão que, quando clicado, executa a função 'mostrar_nome'.
btn = tk.Button(
    root,
    text='Mostrar Itens Selecionados',
    command=mostrar_nome, # Associa a função 'mostrar_nome' ao clique do botão.
    font=("Arial", 12),
    bg="green",
    fg="white",
    activebackground="darkgreen" # Cor quando o botão é pressionado
)
btn.pack(pady=10)

# Inicia o loop principal do Tkinter.
# Esta linha é crucial, pois ela mantém a janela aberta e responsiva a eventos
# (como cliques de mouse, entrada de teclado, etc.) até que a janela seja fechada.
root.mainloop()
