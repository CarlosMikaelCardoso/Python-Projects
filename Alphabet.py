def a():
    return [
        "   A  ",
        " A   A ",
        "A     A",
        "A A A A",
        "A     A",
        "A     A",
        "A     A"
    ]

def b():
    return [
        "B B B",
        "B    B",
        "B    B",
        "B  B ",
        "B    B",
        "B    B",
        "B B B"
    ]

def c():
    return [
        " C C C ",
        "C     C",
        "C      ",
        "C      ",
        "C      ",
        "C     C",
        " C C C "
    ]

def d():
    return [
        "D D D",
        "D    D",
        "D    D",
        "D    D",
        "D    D",
        "D    D",
        "D D D"
    ]

def e():
    return [
        "E E E E",
        "E",
        "E",
        "E E E",
        "E",
        "E",
        "E E E E"
    ]
    
def f():
    return [
        "F F F F",
        "F",
        "F",
        "F F F",
        "F",
        "F",
        "F"
    ] 
    
def g():
    return [
        " G G G",
        "G     G",
        "G",
        "G   G G",
        "G     G",
        "G     G",
        " G G G"
    ]
    
def h():
    return[
        "H   H",
        "H   H",
        "H   H",
        "H H H",
        "H   H",
        "H   H",
        "H   H"
    ]
    
def i():
    return[
        "I I I I",
        "   I  ",
        "   I  ",
        "   I  ",
        "   I  ",
        "   I  ",
        "I I I I"
    ]   
    
def j():
    return[
        "J J J J",
        "    J  ",
        "    J  ",
        "    J  ",
        "J   J  ",
        "J   J  ",
        " J J"
    ] 
    
def k():
    return[
        "K    K",
        "K   K",
        "K  K",
        "K K",
        "K  K",
        "K   K",
        "K    K"
 
    ]
    
def l():
    return[
        "L",
        "L",
        "L",
        "L",
        "L",
        "L",
        "L L L L",
    ]
    
def m():
    return[
        "M       M",
        "M M   M M",
        "M   M   M",
        "M       M",
        "M       M",
        "M       M",
        "M       M",
    ]
    
def n():
    return[
        "NN    N",
        "N N   N",
        "N  N  N",
        "N   N N",
        "N    NN",
        "N     N",
        "N     N",
        "N     N",
        
        
    ]
    
def o():
    return[
        " O O O",
        "O     O",   
        "O     O",
        "O     O",
        "O     O",
        "O     O",
        " O O O",
    ]
    
def p():
    return[
        "P P P",
        "P    P",
        "P    P",
        "P P P",
        "P    ",
        "P    ",
        "P    "
    ]
    
def q():
    return[
        " Q Q Q",
        "Q     Q",
        "Q     Q",
        "Q     Q",
        "Q     Q",
        "Q    Q",
        " Q Q  Q" 
    ]
    
def r():
    return[
        "R R R",
        "R     R",
        "R R R",
        "R R",
        "R   R",
        "R     R",
        "R     R"
    ]
    
def s():
    return[
        " S S",
        "S    S",
        " S",
        "  S",
        "    S",
        "S    S",
        " S S" 
    ]
    
def t():
    return[
        "T T T T",
        "   T",
        "   T",
        "   T",
        "   T",
        "   T",
        "   T"
    ] 
def u():
    return[
        "U     U",
        "U     U",
        "U     U",
        "U     U",
        "U     U",
        "U     U",
        "U U U U"
    ]   
    
def v():
    return[
    "V     V",
    "V     V",
    "V     V",
    "V     V",
    " V   V",
    "  V V",
    "   V  "
] 
    
def w():
    return[
    "W     W",
    "W     W",
    "W     W",
    "W  W  W",
    "W W W W",
    "W W W W",
    "W     W"
] 
    
def x():
    return[
        "X      X",
        "X      X",
        " X   X",
        "   X",
        " X   X",
        "X      X",
        "X      X"
    ]
    
def y():        
    return[
    "Y   Y",
    " Y Y",
    "  Y",
    "  Y",
    "  Y",
    "  Y",
    "  Y"
    ]
    
def z():
    return[
        "Z Z Z Z",
        "      Z",
        "     Z",
        "   Z",
        " Z",
        "Z",
        "Z Z Z Z",
        
        
    ]

# Mapeamento de letras para funções
letters = {
    "a": a,
    "b": b,
    "c": c,
    "d": d,
    "e": e,
    "f": f,
    "g": g,
    "h": h,
    "i": i,
    "j": j,
    "k": k,
    "l": l,
    "m": m,
    "n": n,
    "o": o,
    "p": p,
    "q": q,
    "r": r,
    "s": s,
    "t": t,
    "u": u,
    "v": v,
    "w": w,
    "x": x,
    "y": y,
    "z": z
}

def print_letters(input_letters):
    max_lines = 7  # Máximo de linhas para todas as letras
    letter_width = 7  # Define a largura fixa para todas as letras (ajuste conforme necessário)
    output_lines = [""] * max_lines

    for letter in input_letters:
        if letter in letters:
            # Pega as linhas da letra atual
            lines = letters[letter]()
            # Preenche com linhas em branco se necessário
            while len(lines) < max_lines:
                lines.append(" " * len(lines[0]))  # Adiciona linha em branco do mesmo comprimento
            # Adiciona espaçamento para que todas as letras tenham a mesma largura
            for i in range(max_lines):
                output_lines[i] += lines[i].ljust(letter_width) + "  "  # Ajusta a largura da letra
        else:
            print(f"Letra '{letter}' não reconhecida.")
            return

    # Imprime as letras estilizadas lado a lado
    print("\n".join(output_lines))




# Recebe a entrada do usuário
input_string = input("Digite as letras: ").lower()

# Remove espaços e processa cada letra
print_letters(input_string)
