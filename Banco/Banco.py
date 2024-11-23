from BlockChain import Blockchain

blockchain = Blockchain()

contas = []

# Função para criar uma nova conta
def new_acc(nome):
    id = len(contas)
    contas.append({"nome": nome, "id": id, "saldo": 0})  # Usando inteiro para saldo
    print(f"Conta criada para {contas[id]['nome']} com ID {contas[id]['id']} e saldo {contas[id]['saldo']}")

# Função para atualizar o saldo de uma conta com base no ID
def atualizar_saldo(id_conta, novo_saldo):
    for conta in contas:
        if conta["id"] == id_conta:
            conta["saldo"] = novo_saldo  # Atualiza o saldo
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

# Criando algumas contas
new_acc("Mikael")
new_acc("Alice")

# Realizando transações e registrando-as na blockchain
transacao = atualizar_saldo(0, 1000)  # Atualiza o saldo da conta com ID 0 (Mikael)
if transacao:
    blockchain.adicionar_bloco(transacao)

transacao = atualizar_saldo(1, 500)   # Atualiza o saldo da conta com ID 1 (Alice)
if transacao:
    blockchain.adicionar_bloco(transacao)

# Transferindo saldo entre contas e registrando na blockchain
transacao = remove_saldo(0, 1, 500)  # Mikael transfere 500 para Alice
if transacao:
    blockchain.adicionar_bloco(transacao)
