from tkinter import *

'''
==============================
FOCUS() E ORDEM DE TABULAÇÃO
==============================

A função focus() é usada para definir qual widget (geralmente uma caixa de texto) 
receberá o foco do cursor assim que a interface for iniciada. Isso é útil em 
formulários, pois indica ao usuário por onde começar a digitar.

----------------------------
COMPORTAMENTO DO FOCUS() E TAB
----------------------------

Algo importante a entender é que a tecla TAB, que permite ao usuário navegar entre os 
widgets da interface, **não segue a ordem do grid** (ou do layout visual), mas sim 
a ordem em que os widgets foram **criados no código**.

Ou seja, o Tkinter monta a "sequência de tabulação" com base na ordem de criação dos 
elementos — e não onde eles aparecem visualmente na tela.

Por isso, mesmo que o campo `t1` esteja acima de `t3` visualmente, se `t3` for 
criado antes no código, ele virá antes na sequência do TAB.

A função focus() apenas define **qual widget receberá o foco inicial**, mas 
a partir desse ponto, o TAB seguirá para os próximos widgets com base na ordem 
em que foram instanciados no código.

----------------------------
EXEMPLO DE NAVEGAÇÃO COM TAB
----------------------------

Exemplo 1: ordem tradicional
    - t1
    - t2
    - t3
    - Botão

    t1.focus()

    Ordem de navegação ao pressionar TAB:
        1º t1
        2º t2
        3º t3
        4º Botão

Exemplo 2: widgets criados em ordem diferente
    - t3 (criado primeiro)
    - t1
    - t2
    - Botão

    t1.focus()

    Ordem de navegação:
        1º t1 (por causa do focus)
        2º t2
        3º Botão
        4º t3 (porque foi criado primeiro no código)

Resumo:
    - A tecla TAB percorre os widgets na ordem em que foram **criadas no código**.
    - O método focus() só define o ponto de partida, não reorganiza a ordem do TAB.
    - Isso é MUITO importante na criação de formulários, onde a ordem natural de digitação deve ser respeitada.

----------------------------
OUTROS MÉTODOS RELACIONADOS
----------------------------

- `focus_set()` → Mesma coisa que `focus()`. Define o foco em um widget.
- `focus_get()` → Retorna o widget que está atualmente com o foco.
- `focus_force()` → Força o foco em um widget, mesmo que a janela não esteja ativa (menos usado).
- `tk_focusNext(widget)` e `tk_focusPrev(widget)` → Avança ou volta para o próximo widget na ordem de foco.

'''

# Código de exemplo

root = Tk()
root.title('Focus e Tab Order')

def mudar_textos():
    l1.config(text=t1.get())
    l2.config(text=t2.get())
    l3.config(text=t3.get())

# Criação dos widgets (ordem importa para o TAB)
t1 = Entry(root)
t2 = Entry(root)
t3 = Entry(root)

l1 = Label(root)
l2 = Label(root)
l3 = Label(root)

bt = Button(root, text='Executar', command=mudar_textos)

# Posicionamento (não influencia a ordem do TAB)
t1.grid(padx=5, pady=2)
t2.grid(padx=5, pady=2)
t3.grid(padx=5, pady=2)

l1.grid(padx=5, pady=2)
l2.grid(padx=5, pady=2)
l3.grid(padx=5, pady=2)

bt.grid(padx=5, pady=10)

# Define foco inicial
t1.focus()

root.mainloop()
