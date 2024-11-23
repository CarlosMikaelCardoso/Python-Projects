import hashlib
import os
import json

class Blockchain:
    def __init__(self, prefixo="008", pasta="blockchain_data", arquivo="blockchain.txt"):
        self.prefixo = prefixo
        self.pasta = pasta
        self.arquivo = arquivo
        self.blockchain = self.carregar_blockchain()

        # Adicionar o bloco gênesis se a blockchain estiver vazia
        if not self.blockchain:
            self.adicionar_bloco_genesis()

    # Função para encontrar o hash com prefixo desejado
    def encontrar_hash_com_prefixo(self, texto):
        nonce = 0
        while True:
            valor_tentativa = f"{texto}{nonce}"
            hash_calculado = hashlib.sha256(valor_tentativa.encode('utf-8')).hexdigest()
            if hash_calculado.startswith(self.prefixo):
                return nonce, hash_calculado
            nonce += 1

    # Função para salvar a blockchain em um arquivo
    def salvar_blockchain(self):
        os.makedirs(self.pasta, exist_ok=True)
        caminho_arquivo = os.path.join(self.pasta, self.arquivo)
        with open(caminho_arquivo, "w") as arquivo:
            json.dump(self.blockchain, arquivo, indent=4)
        print(f"Blockchain salva em: {caminho_arquivo}")

    # Função para carregar a blockchain de um arquivo
    def carregar_blockchain(self):
        caminho_arquivo = os.path.join(self.pasta, self.arquivo)
        if os.path.exists(caminho_arquivo):
            with open(caminho_arquivo, "r") as arquivo:
                return json.load(arquivo)
        return []  # Retorna uma blockchain vazia se o arquivo não existir

    # Adicionar o bloco gênesis
    def adicionar_bloco_genesis(self):
        genesis_block = {
            "bloco": 0,
            "nonce": 0,
            "texto": "Bloco Genesis",
            "hash": "0000000000000000000000000000000000000000000000000000000000000000",
            "hash_anterior": "0000000000000000000000000000000000000000000000000000000000000000"
        }
        self.blockchain.append(genesis_block)

    # Adicionar um novo bloco à blockchain
    def adicionar_bloco(self, transacao):
        bloco = len(self.blockchain)  # Número do próximo bloco
        texto_inicial = transacao
        texto = ""
        texto += texto_inicial
        
        if bloco == 1:
            texto += str(self.blockchain[0]["bloco"])
            texto += str(self.blockchain[0]["nonce"])
            texto += self.blockchain[0]["texto"]
            texto += self.blockchain[0]["hash"]
            texto += self.blockchain[0]["hash_anterior"]
        elif bloco > 1:
            texto += str(self.blockchain[bloco - 1]["bloco"])
            texto += str(self.blockchain[bloco - 1]["nonce"])
            texto += self.blockchain[bloco - 1]["texto"]
            texto += self.blockchain[bloco - 1]["hash"]
            texto += self.blockchain[bloco - 1]["hash_anterior"]


        # Encontrar o nonce e o hash
        nonce_usado, hash_encontrado = self.encontrar_hash_com_prefixo(texto)

        # Adicionar o novo bloco à blockchain
        novo_bloco = {
            "bloco": bloco,
            "nonce": nonce_usado,
            "texto": texto_inicial,
            "hash": hash_encontrado,
            "hash_anterior": self.blockchain[bloco - 1]["hash"]
        }
        self.blockchain.append(novo_bloco)

        # Salvar a blockchain no arquivo
        self.salvar_blockchain()

        print(f"Hash encontrado: {hash_encontrado}")
        print(f"Nonce usado: {nonce_usado}")

    def listar_blocos(self):
        for bloco in self.blockchain:
            print(bloco)


# Exemplo de uso

if __name__ == "__main__":
    # Criar instância da classe Blockchain
    blockchain = Blockchain()

    # Registrar transações bancárias
    while True:
        transacao = input("Digite a transação (ou 'sair' para encerrar): ")
        if transacao.lower() == 'sair':
            break
        
        # Adicionar a transação à blockchain
        blockchain.adicionar_bloco(transacao)
