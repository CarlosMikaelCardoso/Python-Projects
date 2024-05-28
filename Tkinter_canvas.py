from tkinter import *
import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Janela")

canvas = tk.Canvas(root,width=400, height=400)
canvas.pack()

canvas.create_oval(50,50,150,150, outline="black", fill="red")

canvas.create_rectangle(200,50,300,150, outline="white", fill="black")

canvas.create_line(100,200,300,350, fill="black", width=3)

canvas.create_text(300, 350, text="Hello, Tkinter!", fill="purple")

root.mainloop()