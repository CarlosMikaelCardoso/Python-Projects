import math
import tkinter as tk
a = 0
b = 0
c = 0

def obter_input():
    global a,b,c
    a = int(campo_entrada1.get())
    b = int(campo_entrada2.get())
    c = int(campo_entrada3.get())
    resultado_label.config(text="Valor de a: " + str(a) + '\n'
                                "Valor de b: " + str(b) + '\n'
                                "Valor de c: " + str(c) + '\n')
    
    def delta (a,b,c):
        c = int(math.pow(b,2) - 4 * a * c)
        return int(c)

    c = delta(a,b,c)
    result_label.config(text=f"X1: {int((-b + math.isqrt(c)) / (2*a))}")
    
    result_label2.config(text=f"X2: {int((-b - math.isqrt(c)) / (2*a))}")
    

    

root = tk.Tk()
root.title("Calculo de Segundo Grau")

informacao_label = tk.Label(root, text="Esta é a informação que você quer escrever na janela")
informacao_label.pack()

campo_entrada1 = tk.Entry(root)
campo_entrada1.pack()

campo_entrada2 = tk.Entry(root)
campo_entrada2.pack()

campo_entrada3 = tk.Entry(root)
campo_entrada3.pack()

resultado_label = tk.Label(root, text="")
resultado_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

result_label2 = tk.Label(root, text="")
result_label2.pack()

botao_input = tk.Button(text="Enter",command=obter_input)
botao_input.pack()

root.mainloop()
