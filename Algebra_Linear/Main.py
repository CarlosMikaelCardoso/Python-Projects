import numpy as np

# Definindo os vetores
u = np.array([1, 2, 3])
v = np.array([4, 5, 6])

# Soma de vetores
soma = u + v
print("Soma:", soma)

# Subtração de vetores
subtracao = u - v
print("Subtração:", subtracao)

# Produto escalar
produto_escalar = np.dot(u, v)
print("Produto Escalar:", produto_escalar)

# Produto vetorial
produto_vetorial = np.cross(u, v)
print("Produto Vetorial:", produto_vetorial)

# Multiplicação por escalar
k = 2
multiplicacao_escalar = k * u
print("Multiplicação por escalar:", multiplicacao_escalar)