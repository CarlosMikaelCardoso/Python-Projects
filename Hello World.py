import string
import time
import tkinter as tk


text = "Ate Agora quero saber como voce consegue ser tao gostosa!!"
temp = ''
for ch in text:
    for i in string.printable:
        if i == ch or ch == i:
            time.sleep(0.02)
            print(temp+i)
            temp += ch
            break
        else:
            time.sleep(0.02)
            print(temp+i)
            
            
            