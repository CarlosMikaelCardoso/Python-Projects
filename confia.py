import tkinter as tk
from PIL import Image, ImageTk

def adicao():
    global a, b
    
    a = campo_entrada1.get()
    b = campo_entrada2.get()
    resultado.config(text="Hello! World!")

root = tk.Tk()
root.title("Confia na Adicao")

campo_entrada1 = tk.Entry(root)
campo_entrada1.pack()

simbolo = tk.Label(root, text="+")
simbolo.pack()

campo_entrada2 = tk.Entry(root)
campo_entrada2.pack()

resultado = tk.Label(root, text="")
resultado.pack()

botao_add = tk.Button(text="=", command=adicao)
botao_add.pack()

imagem = Image.open("C:\\Users\\Administrator\\Downloads\\confia.png")
imagem_tk = ImageTk.PhotoImage(imagem)


label_imagem = tk.Label(root, image=imagem_tk)
label_imagem.pack()

root.mainloop()
