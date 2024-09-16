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
