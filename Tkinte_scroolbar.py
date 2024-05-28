from tkinter import *
import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Janela")

scrollbarra = tk.Scrollbar(root)
scrollbarra.pack(side=tk.RIGHT, fill=tk.Y)

listabox = tk.Listbox(root, yscrollcommand=scrollbarra.set)

for i in range(1, 100):
    listabox.insert(tk.END,f"Item {i}")
listabox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbarra.config(command=listabox.yview)

root.mainloop()