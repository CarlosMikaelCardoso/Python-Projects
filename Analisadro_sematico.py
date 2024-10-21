# Função que verifica se a operação é válida
def verificar_erro_semantico(tipo1, operador, tipo2):
    # Verifica se os tipos são compatíveis com o operador
    if operador == "+":
        # Somente números ou strings podem ser somados com números ou strings
        if (tipo1 == "int" and tipo2 == "int") or (tipo1 == "string" and tipo2 == "string"):
            return False
        else:
            return True
        
    elif operador == "-":
        # Subtração só faz sentido para números
        if tipo1 == "int" and tipo2 == "int":
            return False
        else:
            return True
        
    elif operador == "*":
        if(tipo1 == "int" and tipo2 == 'int') or (tipo1 == "string" and tipo2 == "string"):
            return False
        else:
            return True
        
    elif operador == "/":
        if(tipo1 == "int" and tipo2 == 'int'):
            return False
        else:
            return True
    else:
        # Outros operadores podem ser adicionados conforme necessário
        return True

# Testando a função com algumas expressões
expressao1 = ("int", "+", "int")       # Válido
expressao2 = ("int", "*", "string")    # Inválido
expressao3 = ("string", "-", "string") # Válido
expressao4 = ("int", "/", "string")    # Inválido

# Lista de expressões para testar
expressoes = [expressao1, expressao2, expressao3, expressao4]

# Itera sobre as expressões para verificar se há erros
for i, expr in enumerate(expressoes, 1):
    tipo1, operador, tipo2 = expr
    if verificar_erro_semantico(tipo1, operador, tipo2):
        print(f"Erro semântico na expressão {i}: Não é possível usar o operador '{operador}' com '{tipo1}' e '{tipo2}'")
    else:
        print(f"Expressão {i} é válida")
