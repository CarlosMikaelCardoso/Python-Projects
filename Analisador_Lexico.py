palavras_chaves = ["if", "else"]
operadores = ["+", "-", "=", "*", "/", "%", "=="]
numeros = ["0","1","2","3","4","5","6","7","8","9"]
identificadores = [" "]
tokens = 0

codigo = "if x + y = 8 % 2 == 0"
tokens_codigo = codigo.split()
print("Tokens do código:", tokens_codigo)

for token in tokens_codigo[:]:
    if token in palavras_chaves:
        tokens_codigo.remove(token)
        tokens += 1

for token in tokens_codigo[:]:
    if token in operadores:
        tokens_codigo.remove(token)
        tokens += 1
        
for token in tokens_codigo[:]:
    if token in numeros:
        tokens_codigo.remove(token)
        tokens += 1       
    
for token in tokens_codigo[:]:
    if token.isalpha():
        tokens_codigo.remove(token) 
        tokens += 1
        
print("Número total de tokens encontrados:", tokens)
print("Tokens restantes:", tokens_codigo)
