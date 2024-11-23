import hashlib
import os
import json

# Função para encontrar o hash com prefixo desejado
def encontrar_hash_com_prefixo(texto, prefixo="008"):
    nonce = 0  # Variável para acompanhar as tentativas
    while True:
        # Combine o texto com o contador para gerar um valor único
        valor_tentativa = f"{texto}{nonce}"
        
        # Calcule o hash
        hash_calculado = hashlib.sha256(valor_tentativa.encode('utf-8')).hexdigest()
        
        # Verifique se o hash começa com o prefixo desejado
        if hash_calculado.startswith(prefixo):
            return nonce, hash_calculado  # Retorne o contador e o hash encontrado
        
        nonce += 1  # Incrementa o contador para tentar outra combinação

# Função para salvar a blockchain em um arquivo
def salvar_blockchain(blockchain, caminho_arquivo):
    with open(caminho_arquivo, "w") as arquivo:
        json.dump(blockchain, arquivo, indent=4)
    print(f"Blockchain salva em: {caminho_arquivo}")

# Função para carregar a blockchain de um arquivo
def carregar_blockchain(caminho_arquivo):
    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, "r") as arquivo:
            return json.load(arquivo)
    return []  # Retorna uma blockchain vazia se o arquivo não existir

# Inicialização de variáveis
pasta = "blockchain_data"
os.makedirs(pasta, exist_ok=True)  # Cria a pasta se ela não existir
caminho_arquivo = os.path.join(pasta, "blockchain.txt")

blockchain = carregar_blockchain(caminho_arquivo)

# Adicionar o bloco gênesis se a blockchain estiver vazia
if not blockchain:
    genesis_block = {
        "bloco": 0,
        "nonce": 0,
        "texto": "Bloco Genesis",
        "hash": "0000000000000000000000000000000000000000000000000000000000000000",
        "hash_anterior": "0000000000000000000000000000000000000000000000000000000000000000"
    }
    blockchain.append(genesis_block)

# Prefixo desejado (hash deve começar com "008")
prefixo_desejado = "008"

# Entrada do usuário
num = input("Digite 1 para criar um novo bloco ou 2 para sair: ")

if num == "1":
    texto_inicial = input("Insira sua transação: ")
    bloco = len(blockchain)  # Calcula o número do próximo bloco
    texto = ""
    texto += texto_inicial
    
    if bloco == 1:
        texto += str(blockchain[0]["bloco"])
        texto += str(blockchain[0]["nonce"])
        texto += blockchain[0]["texto"]
        texto += blockchain[0]["hash"]
        texto += blockchain[0]["hash_anterior"]
    elif bloco > 1:
        texto += str(blockchain[bloco - 1]["bloco"])
        texto += str(blockchain[bloco - 1]["nonce"])
        texto += blockchain[bloco - 1]["texto"]
        texto += blockchain[bloco - 1]["hash"]
        texto += blockchain[bloco - 1]["hash_anterior"]

    # Encontrar o nonce e o hash
    nonce_usado, hash_encontrado = encontrar_hash_com_prefixo(texto, prefixo=prefixo_desejado)

    # Adicionar o novo bloco à blockchain
    novo_bloco = {
        "bloco": bloco,
        "nonce": nonce_usado,
        "texto": texto_inicial,
        "hash": hash_encontrado,
        "hash_anterior": blockchain[bloco - 1]["hash"]
    }
    blockchain.append(novo_bloco)

    # Salvar a blockchain no arquivo
    salvar_blockchain(blockchain, caminho_arquivo)

    print(f"Hash encontrado: {hash_encontrado}")
    print(f"Nonce usado: {nonce_usado}")
else:
    print("Saindo...")
