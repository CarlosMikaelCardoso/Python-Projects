import os
import time

def calculo(a,b):
    result = a/b
    return result

while True:

    try:
        a = int(input("Valor de A:"))
        b = int(input("Valor de B:"))
        a = calculo(a,b)
        print (a)
        break

    except ValueError:
        print("Digite apenas numeros interiros!!!")
        time.sleep(2.5)
        os.system('cls')
        
    except ZeroDivisionError:
        print("Não tem como dividir numeros por zero(Seu corno)!!!")
        time.sleep(2.5)
        os.system('cls')
    