from tkinter import *
import tkinter as tk

def exiber_text():
    texto = entrada.get()
    info.config(text=texto)


root = tk.Tk()
root.geometry("300x200")
root.title("Janela")

entrada = tk.Entry(root)
entrada.grid(row=2, column=1)

entrada_button = tk.Button(root,text="Enter", command=exiber_text)
entrada_button.grid(row=2, column=0)

info = tk.Label(root, text="")
info.grid(row=1, column=2)

fecha_botao = tk.Button(root, text="Exit", command=lambda: root.destroy())
fecha_botao.grid(row=1, column=1)

botao1 = tk.Button(root, text="1")
botao1.grid(row=0,column=0)

botao2 = tk.Button(root, text="1")
botao2.grid(row=0,column=1)

botao3 = tk.Button(root, text="1")
botao3.grid(row=1,column=0)


root.mainloop()