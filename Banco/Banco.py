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

# Criando algumas contas
new_acc("Mikael")
new_acc("Alice")

# Realizando transações e registrando-as na blockchain
transacao = atualizar_saldo(0, 1000)  # Atualiza o saldo da conta com ID 0 (Mikael)
if transacao:  # Verifica se a transação foi criada corretamente
    blockchain.adicionar_bloco(transacao)

transacao = atualizar_saldo(1, 500)   # Atualiza o saldo da conta com ID 1 (Alice)
if transacao:  # Verifica se a transação foi criada corretamente
    blockchain.adicionar_bloco(transacao)
