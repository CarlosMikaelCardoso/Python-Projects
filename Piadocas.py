import requests
from PIL import Image, ImageTk
import tkinter as tk
from io import BytesIO

def requisicao():
    req = requests.get('https://api.thecatapi.com/v1/images/search')
    if req.status_code == 200:
        try:
            # Obtém a URL da imagem da resposta
            imagem_url = req.json()[0]['url']

            # Faz uma nova solicitação para baixar a imagem
            imagem_req = requests.get(imagem_url)

            # Lendo os bytes da imagem da resposta
            imagem_bytes = BytesIO(imagem_req.content)

            # Abrindo a imagem usando a biblioteca Pillow
            imagem_pil = Image.open(imagem_bytes)

            # Redimensionar a imagem se necessário
            largura_max = 300
            altura_max = 300
            if imagem_pil.width > largura_max or imagem_pil.height > altura_max:
                imagem_pil.thumbnail((largura_max, altura_max))

            # Convertendo a imagem para o formato suportado pelo Tkinter
            imagem_tk = ImageTk.PhotoImage(imagem_pil)

            # Exibir a imagem no widget Label
            label_imagem.configure(image=imagem_tk)
            label_imagem.image = imagem_tk  # Manter uma referência para a imagem

        except Exception as e:
            print('Erro ao abrir a imagem:', e)
    else:
        # Imprimindo detalhes do erro
        print('Erro ao buscar a imagem:')
        print('Código de status:', req.status_code)
        print('Resposta:', req.text)
        
        
def requisicao2():
    req = requests.get('https://api.thedogapi.com/v1/images/search')
    if req.status_code == 200:
        try:
            # Obtém a URL da imagem da resposta
            imagem_url = req.json()[0]['url']

            # Faz uma nova solicitação para baixar a imagem
            imagem_req = requests.get(imagem_url)

            # Lendo os bytes da imagem da resposta
            imagem_bytes = BytesIO(imagem_req.content)

            # Abrindo a imagem usando a biblioteca Pillow
            imagem_pil = Image.open(imagem_bytes)

            # Redimensionar a imagem se necessário
            largura_max = 300
            altura_max = 300
            if imagem_pil.width > largura_max or imagem_pil.height > altura_max:
                imagem_pil.thumbnail((largura_max, altura_max))

            # Convertendo a imagem para o formato suportado pelo Tkinter
            imagem_tk = ImageTk.PhotoImage(imagem_pil)

            # Exibir a imagem no widget Label
            label_imagem.configure(image=imagem_tk)
            label_imagem.image = imagem_tk  # Manter uma referência para a imagem

        except Exception as e:
            print('Erro ao abrir a imagem:', e)
    else:
        # Imprimindo detalhes do erro
        print('Erro ao buscar a imagem:')
        print('Código de status:', req.status_code)
        print('Resposta:', req.text)

# Criar a janela
root = tk.Tk()
root.title("Gerador de imagens CAT and DOG!")

# Criar um widget Label para exibir a imagem
imagem_tk = tk.PhotoImage()  # Variável para manter a referência à imagem
label_imagem = tk.Label(root, image=imagem_tk)
label_imagem.pack()



# Criar um frame para conter os botões
frame = tk.Frame(root)
frame.pack()

# Botão para chamar a API e exibir a imagem cat
botao_chama_api = tk.Button(frame, text="CAT", command=requisicao)
botao_chama_api.pack(side=tk.LEFT)

# Botão para chamar a API e exibir a imagem dog
botao_chama_api1 = tk.Button(frame, text="DOG", command=requisicao2)
botao_chama_api1.pack(side=tk.LEFT)


root.mainloop()
