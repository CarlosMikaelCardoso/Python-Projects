#pip install pygame
import math
import tkinter as tk
from PIL import Image, ImageTk
import pygame.mixer

pygame.mixer.init()

pygame.mixer.music.load("C:\\Users\\Administrator\\Downloads\\c418-sweden-minecraft-made-with-Voicemod.wav") 
pygame.mixer.music.play()      
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
                                "Valor de c: " + str(c) + '\n', font=("Arial", 11))
    
    def delta (a,b,c):
        delta1.config(text=f"Delta: {math.pow(b,2) - 4 * a * c}", font=("Arial", 11))
        c = math.pow(b,2) - 4 * a * c
        return int(c)

    c = delta(a,b,c)
    if c <= 0:
        resultado_label.config(text="")
        result_label.config(text="Delta deu um valor invalido para o calculo do X1 e X2!", font=("Arial", 18))
        result_label2.config(text="")
        pygame.mixer.music.load("C:\\Users\\Administrator\\Downloads\\buzzer-or-wrong-answer-20582.wav") 
        pygame.mixer.music.play()
    else:
        result_label.config(text=f"X1: {(-b + math.isqrt(c)) / (2*a)}", font=("Arial", 11))
        result_label2.config(text=f"X2: {(-b - math.isqrt(c)) / (2*a)}", font=("Arial", 11))
        
         # Tocar áudio
        pygame.mixer.music.load("C:\\Users\\Administrator\\Downloads\\and-the-correct-answer-is-39671.wav") 
        pygame.mixer.music.play()
        
    

    

root = tk.Tk()
root.title("Calculo de Segundo Grau")

informacao_label = tk.Label(root, text="Digite os valores de A B C respectivamente")
informacao_label.pack()

campo_entrada1 = tk.Entry(root)
campo_entrada1.pack()

campo_entrada2 = tk.Entry(root)
campo_entrada2.pack()

campo_entrada3 = tk.Entry(root)
campo_entrada3.pack()

resultado_label = tk.Label(root, text="")
resultado_label.pack()

delta1 = tk.Label(root, text="")
delta1.pack()

result_label = tk.Label(root, text="")
result_label.pack()

result_label2 = tk.Label(root, text="")
result_label2.pack()

botao_input = tk.Button(text="Enter",command=obter_input)
botao_input.pack()

imagem = Image.open("C:\\Users\\Administrator\\Downloads\\confia.png")
imagem_tk = ImageTk.PhotoImage(imagem)


label_imagem = tk.Label(root, image=imagem_tk)
label_imagem.pack()

root.mainloop()
