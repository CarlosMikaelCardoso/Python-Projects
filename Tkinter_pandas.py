import tkinter as tk
from tkinter import ttk
import pandas as pd

# Dados de exemplo do pandas
data = {'Nome': ['Alice', 'Bob', 'Charlie'],
        'Idade': [24, 30, 22]}
df = pd.DataFrame(data)

root = tk.Tk()
root.geometry("300x200")
root.title("Treeview com Pandas")

tree = ttk.Treeview(root, columns=('Nome', 'Idade'), show='headings')
tree.heading('Nome', text='Nome')
tree.heading('Idade', text='Idade')

for index, row in df.iterrows():
    tree.insert('', 'end', values=(row['Nome'], row['Idade']))

tree.pack()

root.mainloop()
