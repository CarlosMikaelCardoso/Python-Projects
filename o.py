import os

arquivos = os.scandir()
for obj in arquivos:
        print(obj)