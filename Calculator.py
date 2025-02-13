import tkinter as tk 
def create_button(parent, text, command):
    button = tk.Button(parent, text=text, command=command, width=20)
    button.pack()

root = tk.Tk()
root.title("Calculator")

entrada_var = tk.StringVar()
entrada = tk.Entry(root, textvariable=entrada_var, state='readonly')
entrada.pack()

create_button(root, "1", lambda: entrada_var.set(entrada_var.get() + "1"))
create_button(root, "2", lambda: entrada_var.set(entrada_var.get() + "2"))
create_button(root, "3", lambda: entrada_var.set(entrada_var.get() + "3"))
create_button(root, "4", lambda: entrada_var.set(entrada_var.get() + "4"))
create_button(root, "5", lambda: entrada_var.set(entrada_var.get() + "5"))
create_button(root, "6", lambda: entrada_var.set(entrada_var.get() + "6"))  
create_button(root, "7", lambda: entrada_var.set(entrada_var.get() + "7"))  
create_button(root, "8", lambda: entrada_var.set(entrada_var.get() + "8"))  
create_button(root, "9", lambda: entrada_var.set(entrada_var.get() + "9"))  
create_button(root, "0", lambda: entrada_var.set(entrada_var.get() + "0"))  
create_button(root, "+", lambda: entrada_var.set(entrada_var.get() + "+"))  
create_button(root, "-", lambda: entrada_var.set(entrada_var.get() + "-"))  
create_button(root, "*", lambda: entrada_var.set(entrada_var.get() + "*"))  
create_button(root, "/", lambda: entrada_var.set(entrada_var.get() + "/"))  



root.mainloop()