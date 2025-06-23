"""
Bloco de Notas: Imagens no Tkinter e Manipulação Avançada

Este script demonstra como exibir imagens em uma janela Tkinter e, mais importante,
como manipular essas imagens (redimensionar, cortar, girar, etc.) usando a biblioteca Pillow.

--------------------------------------------------------------------------------
Parte 1: O Básico - Exibindo uma Imagem (como no seu código original)
--------------------------------------------------------------------------------

O Tkinter pode carregar imagens usando a classe `PhotoImage`. No entanto, este método
é bastante limitado:
- Suporta apenas os formatos GIF e PGM/PPM. Para usar outros formatos como PNG ou JPG,
  precisamos de uma biblioteca auxiliar.
- Não oferece funções fáceis para redimensionar, cortar ou manipular a imagem depois de carregada.
  As únicas opções são `subsample()` e `zoom()`, que não são ideais para um redimensionamento de qualidade.

--------------------------------------------------------------------------------
Parte 2: A Solução Profissional - A Biblioteca Pillow (PIL Fork)
--------------------------------------------------------------------------------

Para manipular imagens de forma eficaz, usamos a biblioteca `Pillow`.
Ela é a sucessora da `PIL` (Python Imaging Library).

Primeiro, instale a biblioteca se ainda não tiver:
pip install Pillow

O fluxo de trabalho com Pillow e Tkinter é o seguinte:
1. Abrir a imagem com `PIL.Image.open()`.
2. Realizar todas as manipulações desejadas (redimensionar, cortar, etc.) no objeto da imagem PIL.
3. Converter a imagem PIL para um formato que o Tkinter entenda usando `PIL.ImageTk.PhotoImage()`.
4. Atribuir a imagem convertida a um widget, como um `Label`.

Vantagens:
- Suporte a dezenas de formatos de imagem (PNG, JPEG, BMP, etc.).
- Um conjunto completo de ferramentas para manipulação.
- Integração perfeita com o Tkinter.
"""
'''
import tkinter as tk
from PIL import Image, ImageTk, ImageFilter, ImageEnhance  # Importa as classes necessárias do Pillow


# --- Classe Principal da Aplicação ---
class ImageManipulatorApp:
    def __init__(self, root_window):
        self.root = root_window
        self.root.title("Demonstração de Manipulação de Imagens")
        self.root.configure(bg='#f0f0f0')

        # --- Carregamento da Imagem Original com Pillow ---
        # Abrimos a imagem UMA VEZ e a mantemos como nosso objeto "mestre".
        # Substitua 'Img/Monika_large.png' pelo caminho da sua imagem.
        try:
            pil_image = Image.open('Img/Monika_large.png')
            # CORREÇÃO: Converte a imagem para o modo RGBA.
            # Isso resolve o erro "cannot filter palette images", garantindo que a imagem
            # tenha um formato de cor direto (Vermelho, Verde, Azul, Alfa) que permite
            # a aplicação de filtros e outras manipulações complexas.
            self.original_pil_image = pil_image.convert('RGBA')

        except FileNotFoundError:
            # Se a imagem não for encontrada, cria uma imagem preta de placeholder.
            self.original_pil_image = Image.new('RGBA', (400, 400), color='black')
            # E adiciona um texto para indicar o erro.
            from PIL import ImageDraw
            draw = ImageDraw.Draw(self.original_pil_image)
            draw.text((10, 10), "Imagem não encontrada!", fill="white")

        # Frame para organizar as imagens
        frame = tk.Frame(self.root, bg='#f0f0f0', padx=10, pady=10)
        frame.pack()

        # --- Exibição das Imagens Manipuladas ---

        # 1. IMAGEM ORIGINAL
        # Convertemos a imagem PIL para o formato do Tkinter.
        self.tk_original = ImageTk.PhotoImage(self.original_pil_image)
        self.create_image_label(frame, "Original", self.tk_original, 0, 0)

        # 2. IMAGEM REDIMENSIONADA (Resize)
        # O método resize() recebe uma tupla (largura, altura).
        # Image.Resampling.LANCZOS (anteriormente ANTIALIAS) é um filtro de alta qualidade para redimensionamento.
        resized_pil = self.original_pil_image.resize((150, 150), Image.Resampling.LANCZOS)
        self.tk_resized = ImageTk.PhotoImage(resized_pil)
        self.create_image_label(frame, "Redimensionada (150x150)", self.tk_resized, 0, 1)

        # 3. IMAGEM RECORTADA (Crop)
        # O método crop() recebe uma tupla de 4 valores: (x_inicial, y_inicial, x_final, y_final).
        # A origem (0,0) é o canto superior esquerdo.
        box = (100, 50, 300, 250)  # Corta uma "caixa" de 200x200 pixels do centro da imagem.
        cropped_pil = self.original_pil_image.crop(box)
        self.tk_cropped = ImageTk.PhotoImage(cropped_pil)
        self.create_image_label(frame, "Recortada", self.tk_cropped, 0, 2)

        # 4. IMAGEM EM ESCALA DE CINZA (Grayscale)
        # O método convert() com o modo 'L' (Luminância) transforma a imagem em P&B.
        grayscale_pil = self.original_pil_image.convert('L')
        self.tk_grayscale = ImageTk.PhotoImage(grayscale_pil)
        self.create_image_label(frame, "Escala de Cinza", self.tk_grayscale, 1, 0)

        # 5. IMAGEM ROTACIONADA (Rotate)
        # O método rotate() gira a imagem em graus, no sentido anti-horário.
        # `expand=True` garante que a imagem inteira apareça, ajustando o tamanho do canvas.
        rotated_pil = self.original_pil_image.rotate(45, expand=True,
                                                     fillcolor=(255, 255, 255, 0))  # Fundo transparente
        self.tk_rotated = ImageTk.PhotoImage(rotated_pil)
        self.create_image_label(frame, "Rotacionada (45°)", self.tk_rotated, 1, 1)

        # 6. IMAGEM COM FILTRO (Filter)
        # Pillow vem com vários filtros pré-definidos no módulo ImageFilter.
        # BLUR: Desfoque | CONTOUR: Contorno | EMBOSS: Relevo | SHARPEN: Nitidez
        blurred_pil = self.original_pil_image.filter(ImageFilter.BLUR)
        self.tk_blurred = ImageTk.PhotoImage(blurred_pil)
        self.create_image_label(frame, "Filtro (Desfoque)", self.tk_blurred, 1, 2)

        # 7. AJUSTE DE BRILHO (Enhancement)
        # O módulo ImageEnhance permite ajustar brilho, contraste, cor e nitidez.
        enhancer = ImageEnhance.Brightness(self.original_pil_image)
        # O fator 1.0 é o original. > 1.0 aumenta o brilho, < 1.0 diminui.
        brighter_pil = enhancer.enhance(1.8)
        self.tk_brighter = ImageTk.PhotoImage(brighter_pil)
        self.create_image_label(frame, "Mais Brilho", self.tk_brighter, 2, 0)

        # 8. AJUSTE DE CONTRASTE (Enhancement)
        enhancer = ImageEnhance.Contrast(self.original_pil_image)
        contrast_pil = enhancer.enhance(2.0)
        self.tk_contrast = ImageTk.PhotoImage(contrast_pil)
        self.create_image_label(frame, "Mais Contraste", self.tk_contrast, 2, 1)

    def create_image_label(self, parent, text, image, row, col):
        """Função auxiliar para criar um label de texto e um label de imagem de forma organizada."""
        container = tk.Frame(parent, bg='#e0e0e0', bd=1, relief=tk.SOLID)
        container.grid(row=row, column=col, padx=10, pady=10)

        title_label = tk.Label(container, text=text, bg='#e0e0e0', font=('Arial', 10, 'bold'))
        title_label.pack(pady=(5, 5))

        image_label = tk.Label(container, image=image, bg='white')
        # IMPORTANTE: A referência à imagem DEVE ser mantida (ex: self.tk_image),
        # senão o garbage collector do Python a remove e a imagem some da tela.
        image_label.image = image
        image_label.pack(padx=5, pady=(0, 5))


# --- Bloco de Execução Principal ---
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageManipulatorApp(root)
    root.mainloop()'''

"""
Bloco de Notas: Imagens no Tkinter e Manipulação Avançada

Este script demonstra como exibir imagens em uma janela Tkinter e, mais importante,
como manipular essas imagens (redimensionar, cortar, girar, etc.) usando a biblioteca Pillow.

--------------------------------------------------------------------------------
Parte 1: O Básico - Exibindo uma Imagem (como no seu código original)
--------------------------------------------------------------------------------

O Tkinter pode carregar imagens usando a classe `PhotoImage`. No entanto, este método
é bastante limitado:
- Suporta apenas os formatos GIF e PGM/PPM. Para usar outros formatos como PNG ou JPG,
  precisamos de uma biblioteca auxiliar.
- Não oferece funções fáceis para redimensionar, cortar ou manipular a imagem depois de carregada.
  As únicas opções são `subsample()` e `zoom()`, que não são ideais para um redimensionamento de qualidade.

--------------------------------------------------------------------------------
Parte 2: A Solução Profissional - A Biblioteca Pillow (PIL Fork)
--------------------------------------------------------------------------------

Para manipular imagens de forma eficaz, usamos a biblioteca `Pillow`.
Ela é a sucessora da `PIL` (Python Imaging Library).

Primeiro, instale a biblioteca se ainda não tiver:
pip install Pillow

O fluxo de trabalho com Pillow e Tkinter é o seguinte:
1. Abrir a imagem com `PIL.Image.open()`.
2. Realizar todas as manipulações desejadas (redimensionar, cortar, etc.) no objeto da imagem PIL.
3. Converter a imagem PIL para um formato que o Tkinter entenda usando `PIL.ImageTk.PhotoImage()`.
4. Atribuir a imagem convertida a um widget, como um `Label`.

Vantagens:
- Suporte a dezenas de formatos de imagem (PNG, JPEG, BMP, etc.).
- Um conjunto completo de ferramentas para manipulação.
- Integração perfeita com o Tkinter.
"""

import tkinter as tk
from PIL import Image, ImageTk, ImageFilter, ImageEnhance  # Importa as classes necessárias do Pillow


# --- Classe Principal da Aplicação ---
class ImageManipulatorApp:
    def __init__(self, root_window):
        self.root = root_window
        self.root.title("Demonstração de Manipulação de Imagens")
        self.root.configure(bg='#f0f0f0')

        # --- Carregamento da Imagem Original com Pillow ---
        # Abrimos a imagem UMA VEZ e a mantemos como nosso objeto "mestre".
        # Substitua 'Img/Monika_large.png' pelo caminho da sua imagem.
        try:
            pil_image = Image.open('Img/Monika_large.png')
            # CORREÇÃO: Converte a imagem para o modo RGBA.
            # Isso resolve o erro "cannot filter palette images", garantindo que a imagem
            # tenha um formato de cor direto (Vermelho, Verde, Azul, Alfa) que permite
            # a aplicação de filtros e outras manipulações complexas.
            self.original_pil_image = pil_image.convert('RGBA')

        except FileNotFoundError:
            # Se a imagem não for encontrada, cria uma imagem preta de placeholder.
            self.original_pil_image = Image.new('RGBA', (400, 400), color='black')
            # E adiciona um texto para indicar o erro.
            from PIL import ImageDraw
            draw = ImageDraw.Draw(self.original_pil_image)
            draw.text((10, 10), "Imagem não encontrada!", fill="white")

        # Frame para organizar as imagens
        frame = tk.Frame(self.root, bg='#f0f0f0', padx=10, pady=10)
        frame.pack()

        # Define um tamanho de exibição padrão para todas as imagens na grade.
        # Isso garante que a janela tenha um layout consistente e previsível.
        display_size = (200, 200)

        # --- Exibição das Imagens Manipuladas ---

        # 1. IMAGEM ORIGINAL
        # Redimensionamos a imagem original apenas para exibição.
        display_original = self.original_pil_image.resize(display_size, Image.Resampling.LANCZOS)
        self.tk_original = ImageTk.PhotoImage(display_original)
        self.create_image_label(frame, "Original (Exibição)", self.tk_original, 0, 0)

        # 2. IMAGEM REDIMENSIONADA (Resize)
        resized_pil = self.original_pil_image.resize(display_size, Image.Resampling.LANCZOS)
        self.tk_resized = ImageTk.PhotoImage(resized_pil)
        self.create_image_label(frame, f"Redimensionada {display_size}", self.tk_resized, 0, 1)

        # 3. IMAGEM RECORTADA (Crop)
        box = (100, 50, 300, 250)
        cropped_pil = self.original_pil_image.crop(box)
        display_cropped = cropped_pil.resize(display_size, Image.Resampling.LANCZOS)  # Redimensiona para exibição
        self.tk_cropped = ImageTk.PhotoImage(display_cropped)
        self.create_image_label(frame, "Recortada", self.tk_cropped, 0, 2)

        # 4. IMAGEM EM ESCALA DE CINZA (Grayscale)
        grayscale_pil = self.original_pil_image.convert('L')
        display_grayscale = grayscale_pil.resize(display_size, Image.Resampling.LANCZOS)  # Redimensiona para exibição
        self.tk_grayscale = ImageTk.PhotoImage(display_grayscale)
        self.create_image_label(frame, "Escala de Cinza", self.tk_grayscale, 1, 0)

        # 5. IMAGEM ROTACIONADA (Rotate)
        rotated_pil = self.original_pil_image.rotate(45, expand=True, fillcolor=(255, 255, 255, 0))
        display_rotated = rotated_pil.resize(display_size, Image.Resampling.LANCZOS)  # Redimensiona para exibição
        self.tk_rotated = ImageTk.PhotoImage(display_rotated)
        self.create_image_label(frame, "Rotacionada (45°)", self.tk_rotated, 1, 1)

        # 6. IMAGEM COM FILTRO (Filter)
        blurred_pil = self.original_pil_image.filter(ImageFilter.BLUR)
        display_blurred = blurred_pil.resize(display_size, Image.Resampling.LANCZOS)  # Redimensiona para exibição
        self.tk_blurred = ImageTk.PhotoImage(display_blurred)
        self.create_image_label(frame, "Filtro (Desfoque)", self.tk_blurred, 1, 2)

        # 7. AJUSTE DE BRILHO (Enhancement)
        enhancer = ImageEnhance.Brightness(self.original_pil_image)
        brighter_pil = enhancer.enhance(1.8)
        display_brighter = brighter_pil.resize(display_size, Image.Resampling.LANCZOS)  # Redimensiona para exibição
        self.tk_brighter = ImageTk.PhotoImage(display_brighter)
        self.create_image_label(frame, "Mais Brilho", self.tk_brighter, 2, 0)

        # 8. AJUSTE DE CONTRASTE (Enhancement)
        enhancer = ImageEnhance.Contrast(self.original_pil_image)
        contrast_pil = enhancer.enhance(2.0)
        display_contrast = contrast_pil.resize(display_size, Image.Resampling.LANCZOS)  # Redimensiona para exibição
        self.tk_contrast = ImageTk.PhotoImage(display_contrast)
        self.create_image_label(frame, "Mais Contraste", self.tk_contrast, 2, 1)

    def create_image_label(self, parent, text, image, row, col):
        """Função auxiliar para criar um label de texto e um label de imagem de forma organizada."""
        container = tk.Frame(parent, bg='#e0e0e0', bd=1, relief=tk.SOLID)
        container.grid(row=row, column=col, padx=10, pady=10)

        title_label = tk.Label(container, text=text, bg='#e0e0e0', font=('Arial', 10, 'bold'))
        title_label.pack(pady=(5, 5))

        image_label = tk.Label(container, image=image, bg='white')
        # IMPORTANTE: A referência à imagem DEVE ser mantida (ex: self.tk_image),
        # senão o garbage collector do Python a remove e a imagem some da tela.
        image_label.image = image
        image_label.pack(padx=5, pady=(0, 5))


# --- Bloco de Execução Principal ---
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageManipulatorApp(root)
    root.mainloop()