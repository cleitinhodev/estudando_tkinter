import tkinter as tk
import time

# CRIANDO A JANELA PRINCIPAL
root = tk.Tk()
root.title("Relógio com .after()")
root.geometry("300x150")

# -------------------------------
# O QUE É O MÉTODO .after()?
# -------------------------------

'''
No Tkinter, o método .after() serve para executar uma função depois de um certo tempo,
sem travar a interface gráfica.

Sintaxe básica:
    widget.after(tempo_em_milissegundos, funcao)

Por exemplo:
    root.after(1000, atualizar)  # chama a função 'atualizar' após 1 segundo (1000 ms)

IMPORTANTE:
Se a função chamada usar .after() dentro dela mesma, ela criará um "loop",
executando automaticamente a cada intervalo de tempo definido.

Isso é útil para:
✔ Criar relógios
✔ Animações
✔ Contadores
✔ Atualizações em tempo real
✔ Efeitos visuais

'''

# LABEL PARA MOSTRAR A HORA
relogio_label = tk.Label(root, text="", font=("Arial", 30), fg="blue")
relogio_label.pack(pady=20)

# -------------------------------
# FUNÇÃO DE ATUALIZAÇÃO COM .after()
# -------------------------------

def atualizar_relogio():
    # Pega a hora atual no formato HH:MM:SS
    horario_atual = time.strftime("%H:%M:%S")

    # Atualiza o texto do label com a nova hora
    relogio_label.config(text=horario_atual)

    # Chama novamente essa função após 1000 milissegundos (1 segundo)
    root.after(1000, atualizar_relogio)


# -------------------------------
# INÍCIO DA PRIMEIRA CHAMADA
# -------------------------------

# Chama a função pela primeira vez (depois ela se chamará sozinha)
atualizar_relogio()

# -------------------------------
# INICIANDO O LOOP DO TKINTER
# -------------------------------

root.mainloop()
