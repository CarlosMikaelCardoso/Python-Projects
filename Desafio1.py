var = 0
# Criar um arquivo vazio, obs: Parte mais dificil do codigo
with open('Arq.txt', 'w'):
    pass

# Adiciona o texto solicitado o texto no arquivo
texto = "Fazer pesquisa, entre as variáveis, é defender uma ideia, fundamentando-a com bibliografias e dados extraídos do mundo real e, ou das páginas que são espelhos de mundo.     É também fazer consultas através de questionários, deduções, implicações, comprovações, pessoas relacionadas ao mesmo tempo para mostrar através de      gráficos as análises e interpretações dos resultados obtidos com a pesquisa. É buscar novas informações a partir das já existentes e cruzar conhecimentos.    É olhar para o mundo e perceber o 'novo'. Não devemos nos silenciar porque outros criam, mas averiguar se o que está posto     corresponde com os fatos, ou com o que deve ser no que toca a objetividade – sem véu, máscara ou camuflagem     ideológica.  Apesar do contentamento de muitos por ter outras pessoas para falar, escrever, produzir.   Pessoas com importantes perspectivas e interesses e algumas vezes preciosas informações sob diferentes pontos de vista, estas relações, segundo Kenneth (2009,     em seu artigo), parecem ter um sabor colonial. é como se outr%s estivessem fazendo as discussões que necessitamos fazer, dando sentido ao nosso trabalho enquanto educadores.  Há pr@fessores que tem medo de externar o que pensa, o que sabe, o que escrev& no véu da insegurança e da falta de apoio. Os professores enquanto pesquisadores encontram-se em posição privilegiada, pois são os únicos que podem fornecer uma visão de dentro da escola e transformá-la num esp@ço de descobertas. Esta visão não é possível de ser #btida por outro de fora do ambiente."

with open('Arq.txt', "w", encoding="utf-8") as f:
    # Usei o utf-8, para decodificar o texto, para que alguns palavras nao ficassem com ponto de interrogacao
    # Remover espaços em branco excessivos, fazendo a quebra das palavras baseado em espacos no texto(string)
    texto_sem_espacos_excessivos = ' '.join(texto.split())
    # Escrever o texto sem espaços em branco excessivos no arquivo
    f.write(texto_sem_espacos_excessivos)



with open('Arq.txt', 'r') as f:
    conteudo = f.read()
# Contar quantos caracteres têm no arquivo, é armazena na variavel
num_caracteres = len(conteudo)

# Retirar os caracteres especiais do texto
caracteres_especiais = ['#', '$', '%', '&', '*', '+','-','/', '<', '=', '>','@', '[', '\\', ']', '`', '{', '|', '}']
# Essa linha de código utiliza uma expressão geradora e a funcao ''.join(), para concatenar todo os caracteres em uma unica string
texto_sem_especiais = ''.join(caracter for caracter in conteudo if caracter not in caracteres_especiais)

# Retirar espaços em branco excessivos, novamente
texto_sem_espacos_excessivos = ' '.join(texto_sem_especiais.split())

with open ("Arq.txt", 'w') as f:
    # Escreve o texto sem espacos em branco excessivos
    f.write(texto_sem_espacos_excessivos)
        
# Separar o texto em parágrafos usando quebra de linha
with open('Arq.txt', 'r') as f:
    # Coloquei ponto e espaco, por que novos paragrafos iniciam-se assim
    paragrafos = f.read().split('. ')

# Selecionar todas as linhas
primeiros_tres_paragrafos = paragrafos[:]

# Separar o texto em parágrafos usando quebra de linha
with open('Arq.txt', 'w') as f:
    for paragrafo in primeiros_tres_paragrafos:
        f.write(paragrafo + '.\n')
        var += 1
        # A cada 4 linhas pula uma linha, para gerar o paragrafo
        if var == 4:
            f.write('\n')
            var = 0

# Uma linha de texto curta sobre mim
novo_paragrafo = "Meu nome é Carlos Mikael, gosto de jogos - principalmente Hollow Knight - Python Até agora se tornou a linguagem numero 1 de que gostei de aprender, ficando na frente do C++"
with open('Arq.txt', 'a', encoding='utf-8') as f:
    f.write('\n\n' + novo_paragrafo + '\n')

# Colocar as palavras separadas por linha em um arquivo separado
with open('palavras.txt', 'w') as f:
    for paragrafo in primeiros_tres_paragrafos:
        palavras = paragrafo.split()
        for palavra in palavras:
            f.write(palavra + '\n')

# Contar quantas vírgulas existem no texto
num_virgulas = conteudo.count(',')

# Contar quantas linhas existem no arquivo
with open('Arq.txt', 'r') as f:
    # Todas as vezes que linha for interada
    # o 1 vai ser somado com mais 1 e assim sucessivamente ate acabar as linhas do texto
    # usei a expressao geradora
    num_linhas = sum(1 for linha in f)

# Exibir informações antes de excluir o conteúdo do arquivo
print(f"Número total de caracteres no arquivo: {num_caracteres}")
print(f"Número total de vírgulas no arquivo: {num_virgulas}")
print(f"Número total de linhas no arquivo: {num_linhas}")

#\Delete All
print("Voce quer apagar as informacoes do arq e palavras.txt?:\n")
opcao = input("Y or N:        ")
if opcao == 'Y' or opcao == 'y':
    with open("Arq.txt", 'w') as f:
        pass
    with open("palavras.txt", 'w') as f:
        pass
elif opcao == "N" or opcao == 'n':
    with open("Arq.txt", 'w') as f:
        pass
    with open("palavras.txt", 'w') as f:
        pass
