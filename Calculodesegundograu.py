import math

a = int(input("Digite o Valoe de a: "))
b = int(input("Digite o Valoe de b: "))
c = int(input("Digite o Valoe de c: "))

def delta (a,b,c):
    c = int(math.pow(b,2) - 4 * a * c)
    return int(c)

c = delta(a,b,c)
print ((-b + math.isqrt(c)) / (2*a))
print ((-b - math.isqrt(c)) / (2*a))

