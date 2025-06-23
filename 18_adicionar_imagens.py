"""
Adicionar imagens a nossa janela pode ser muito útil, e tem algumas formas de fazer isso,
aqui faremos atravez de um label, da seguinte forma:
"""

import tkinter as tk

root = tk.Tk()

monika = tk.PhotoImage(file='Img/Monika_large.png')   # Carrega uma imagem no tamanho original
mini_monika = tk.PhotoImage(file='Img/Monika_small.png')    # O ideal é usar uma imagem no tamanho planejado

label_imagem = tk.Label(root, image=monika)    # O label tras a imagem atravez do comando 'image'
label_imagem2 = tk.Label(root, image=mini_monika)

label_imagem.grid(row=0, column=0)
label_imagem2.grid(row=0, column=1)

root.mainloop()



"""
CORREÇÃO DO ROBÔ


Trabalhando com imagens no Tkinter

Podemos adicionar imagens na nossa interface usando widgets como Label, Button, Canvas, etc.
A forma mais simples é usando o widget Label com o parâmetro 'image'.

Tkinter suporta nativamente imagens no formato GIF e PNG com o PhotoImage.

Para outros formatos como JPG, BMP, recomendamos usar a biblioteca Pillow (PIL).

Também é importante manter a referência da imagem para que ela não desapareça da interface.

import tkinter as tk

# Para formatos diferentes, importe Pillow (caso queira usar)
try:
    from PIL import Image, ImageTk
    pillow_installed = True
except ImportError:
    pillow_installed = False
    print("Pillow não está instalado. Apenas PNG e GIF funcionam nativamente.")

root = tk.Tk()
root.title("Exemplo de Imagens no Tkinter")

# --- Usando PhotoImage (apenas PNG e GIF) ---
# Carregando uma imagem PNG (recomenda-se usar a imagem já no tamanho final)
img_png = tk.PhotoImage(file='Img/Monika_small.png')

# --- Usando Pillow para JPG, BMP, PNG, redimensionamento etc ---
if pillow_installed:
    # Abrir a imagem original
    img_pil = Image.open('Img/Monika_large.jpg')  # Exemplo jpg, pode usar png também
    # Redimensionar (opcional)
    img_pil = img_pil.resize((200, 200))  # Ajusta para 200x200 px

    # Converter para imagem compatível com Tkinter
    img_pil_tk = ImageTk.PhotoImage(img_pil)
else:
    img_pil_tk = None

# Criando labels com as imagens
label1 = tk.Label(root, text="Imagem PNG (PhotoImage):")
label1.grid(row=0, column=0, padx=5, pady=5)
label_img1 = tk.Label(root, image=img_png)
label_img1.grid(row=1, column=0, padx=5, pady=5)

if img_pil_tk:
    label2 = tk.Label(root, text="Imagem JPG redimensionada (Pillow):")
    label2.grid(row=0, column=1, padx=5, pady=5)
    label_img2 = tk.Label(root, image=img_pil_tk)
    label_img2.grid(row=1, column=1, padx=5, pady=5)

# Importante: manter referências das imagens para evitar sumirem
# Se você usar apenas "image=img_png" sem guardar o objeto na variável, a imagem pode não aparecer

root.mainloop()


"""
