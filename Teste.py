import random

def gerar_numeros_aleatorios_unicos(quantidade, limite_inferior, limite_superior):
    return random.sample(range(limite_inferior, limite_superior), quantidade)

def adicionar_prefixo(numeros, prefixo):
    return str(prefixo) + ''.join(f'{numero:01}' for numero in numeros)

# Parâmetros
quantidade_numeros = 8
limite_inferior = 0
limite_superior = 10  # Limitando para garantir que os números sejam de 0 a 9 e únicos

# Gerar números aleatórios únicos
numeros_aleatorios = gerar_numeros_aleatorios_unicos(quantidade_numeros, limite_inferior, limite_superior)

# Adicionar o prefixo "2024"
numero_completo_str = adicionar_prefixo(numeros_aleatorios, 2024)

# Converter para inteiro
numero_completo = int(numero_completo_str)

# Exibir o resultado
print(numero_completo)