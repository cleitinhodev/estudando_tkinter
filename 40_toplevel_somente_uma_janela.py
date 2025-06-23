import tkinter as tk

root = tk.Tk()
root.title('Janela Principal')
root.geometry('400x200')

# Referência global para a nova janela
nova_janela = None

def abrir():
    global nova_janela

    # Se a janela já existe e ainda está aberta, apenas trazê-la à frente
    if nova_janela is not None and nova_janela.winfo_exists():
        nova_janela.lift()
        nova_janela.focus_force()
        return

    # Cria nova janela
    nova_janela = tk.Toplevel()
    nova_janela.title('Nova Janela')
    nova_janela.geometry('300x150')

    lbn = tk.Label(nova_janela, text='Texto Demonstrativo')
    lbn.pack()

    # Função chamada ao clicar no "X" da janela
    def ao_fechar():
        global nova_janela
        nova_janela.destroy()  # fecha a janela de verdade
        nova_janela = None     # limpa a referência

    # Substitui o comportamento padrão do botão de fechar
    nova_janela.protocol("WM_DELETE_WINDOW", ao_fechar)


btn = tk.Button(root, text='Abrir Janela', command=abrir)
btn.pack()

root.mainloop()


"""
✅ destroy()
Fecha a janela imediatamente.

É chamado por você, dentro do código (ex: botão "Fechar", ou lógica interna).

Não executa nenhuma função extra ou lógica personalizada, a não ser que você escreva isso.

✅ protocol("WM_DELETE_WINDOW", função)
Intercepta o clique no botão "X" da janela (o de fechar do sistema).

Permite que você "avise" ou reaja antes do fechamento.

Você pode:

Executar uma confirmação (messagebox.askyesno).

Salvar algo em arquivo.

Limpar variáveis.

Chamar destroy() manualmente depois disso.

🧠 Analogia rápida
Pense assim:

destroy() é como fechar uma porta trancando de uma vez.

protocol("WM_DELETE_WINDOW", ao_fechar) é como alguém bater na porta primeiro e perguntar “posso fechar?”, 
e você faz o que quiser antes de trancar.
"""
