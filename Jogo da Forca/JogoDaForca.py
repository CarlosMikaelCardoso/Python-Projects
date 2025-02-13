import random

def animais1():
    num1 = random.randint(1, 10)
    print (animais[num1])



num = random.randint(1, 3)
if num == 1:
    animais1()
    print('Animais')
elif num == 2:
    print('Objetos')
else:
    print('Paises')



animais = {
    1: 'cachorro',
    2: 'gato',
    3: 'elefante',
    4: 'cavalo',
    5: 'papagaio',
    6: 'girafa',
    7: 'leao',
    8: 'tigre',
    9: 'macaco',
    10: 'pato',
}

objetos = {
    1: 'cadeira',
    2: 'mesa',
    3: 'sofa',
    4: 'geladeira',
    5: 'fogao',
    6: 'microondas',
    7: 'computador',
    8: 'notebook',
    9: 'tablet',
    10: 'smartphone',
}

paises = {
    1: 'brasil',
    2: 'argentina',
    3: 'chile',
    4: 'peru',
    5: 'colombia',
    6: 'equador',
    7: 'uruguai',
    8: 'paraguai',
    9: 'bolivia',
    10: 'venezuela',
}

