import requests
import random

def gerar_numeros():
    numeros = [random.randint(1, 4) for _ in range(4)]  # Gera 4 números aleatórios entre 1 e 100
    print("Números aleatórios:", numeros)

def detalhes(site):
    random = gerar_numeros()
    # Processa as perguntas e respostas da API
    info = ""
    
    for index, question in enumerate(site['results'], 1):
        info += f"Pergunta {index}: {question['question']}\n"
        info += f"A) {question['correct_answer']} (Resposta correta)\n"

        info += "\n"
    return info

def requisicao():
    try:
        # Solicita os dados do usuário
        quantidade = input("Número de questões? ")
        dificuldade = input("Dificuldade (easy, medium, hard): ").lower()
        tipo = input("Tipo (1 para múltipla escolha, 2 para verdadeiro/falso): ")

        # Traduz o tipo de questão para os parâmetros da API
        tipo_param = "multiple" if tipo == "1" else "boolean"

        # Monta a URL
        url = f"https://opentdb.com/api.php?amount={quantidade}&difficulty={dificuldade}&type={tipo_param}"
        req = requests.get(url)
        
        if req.status_code == 200:
            site = req.json()
            if site['response_code'] == 0:  # Verifica se a resposta é válida
                info = detalhes(site)
                print(info)
                input ("Ver a resposta? Enter")
                
            else:
                print("Erro: Não foi possível obter as questões.")
        else:
            print(f"Erro ao buscar dados: {req.status_code}")
    
    except Exception as e:
        print("Erro ao chamar a API: " + str(e))

# Chama a função
requisicao()
