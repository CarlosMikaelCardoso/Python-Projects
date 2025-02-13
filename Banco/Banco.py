import json
from BlockChain import Blockchain

blockchain = Blockchain()

contas = []

# Função para carregar contas de um arquivo
def carregar_contas():
    global contas
    try:
        with open('contas.txt', 'r') as file:
            contas = json.load(file)
    except FileNotFoundError:
        contas = []

# Função para salvar contas em um arquivo
def salvar_contas():
    with open('contas.txt', 'w') as file:
        json.dump(contas, file)

# Função para criar uma nova conta
def new_acc(nome):
    id = len(contas)
    contas.append({"nome": nome, "id": id, "saldo": 0})  # Usando inteiro para saldo
    salvar_contas()
    print(f"Conta criada para {contas[id]['nome']} com ID {contas[id]['id']} e saldo {contas[id]['saldo']}")

# Função para atualizar o saldo de uma conta com base no ID
def atualizar_saldo(id_conta, novo_saldo):
    for conta in contas:
        if conta["id"] == id_conta:
            conta["saldo"] = novo_saldo  # Atualiza o saldo
            salvar_contas()
            print(f"Saldo da conta {conta['nome']} (ID {conta['id']}) atualizado para {conta['saldo']}")
            # Criando uma transação para a blockchain
            transacao = f"Conta {conta['nome']} (ID {conta['id']}) atualizou seu saldo para {conta['saldo']}"
            return transacao

    print("Conta não encontrada.")
    return None  # Retorna None se a conta não for encontrada

# Função para transferir saldo entre contas
def remove_saldo(id_conta_origem, id_conta_destino, saldo):
    conta_origem = next((conta for conta in contas if conta["id"] == id_conta_origem), None)
    conta_destino = next((conta for conta in contas if conta["id"] == id_conta_destino), None)

    if conta_origem is None:
        print(f"Conta de origem com ID {id_conta_origem} não encontrada.")
        return None

    if conta_destino is None:
        print(f"Conta de destino com ID {id_conta_destino} não encontrada.")
        return None

    if conta_origem["saldo"] >= saldo:
        conta_origem["saldo"] -= saldo
        conta_destino["saldo"] += saldo
        salvar_contas()
        print(f"Transferência concluída: {saldo} de {conta_origem['nome']} (ID {conta_origem['id']}) para {conta_destino['nome']} (ID {conta_destino['id']})")
        # Criando a transação para registrar na blockchain
        transacao = (
            f"Transferencia de {saldo} realizada: "
            f"Conta origem {conta_origem['nome']} (ID {conta_origem['id']}, novo saldo {conta_origem['saldo']}), "
            f"Conta destino {conta_destino['nome']} (ID {conta_destino['id']}, novo saldo {conta_destino['saldo']})"
        )
        return transacao
    else:
        print(f"Saldo insuficiente na conta {conta_origem['nome']} (ID {conta_origem['id']}) para transferir {saldo}.")
        return None    

def menu():
    carregar_contas()
    print("1 - Criar conta")
    print("2 - Fazer uma Transação")
    num = int(input("3 - Transferir Saldo \n"))
    if num == 1:
        nome = input("Qual seu nome?\n")
        new_acc(nome)
    elif num == 2:
        id_conta = int(input("Qual o seu ID? \n"))
        saldo_novo = int(input("Qual o valor? \n"))
        transacao = atualizar_saldo(id_conta, saldo_novo)
        if transacao:
            blockchain.adicionar_bloco(transacao)
    elif num == 3: 
        id_conta = int(input("Qual o seu ID?\n"))
        id_conta_destino = int(input("Qual o ID da conta destino?\n"))
        saldo_novo = int(input("Qual o saldo irá tranferir?\n"))
        transacao = remove_saldo(id_conta, id_conta_destino, saldo_novo)
        if transacao:
            blockchain.adicionar_bloco(transacao)       

menu()