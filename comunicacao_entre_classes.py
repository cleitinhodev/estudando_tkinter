import tkinter as tk


class AreaDeTexto(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_de_texto = tk.Label(self, text='Olá Mundo')
        self.label_de_texto.pack()

    def muda_texto(self, novo_texto):
        self.label_de_texto.config(text=novo_texto)


class App:
    def __init__(self, master):
        self.root = master
        self.root.geometry('300x250')
        self.root.title('Comunicação entre Classes')

        # Objetos
        self.botao_de_acionamento = tk.Button(self.root, text='Mudar Texto', command=self.comando_do_botao)
        self.frame_com_texto = AreaDeTexto(self.root)

        # Pack
        self.frame_com_texto.pack()
        self.botao_de_acionamento.pack()

    def comando_do_botao(self):
        self.frame_com_texto.muda_texto('Tchau Mundo!')


root = tk.Tk()
app = App(root)
root.mainloop()
