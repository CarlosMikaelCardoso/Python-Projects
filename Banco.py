import tkinter as tk
import sqlite3 as net 
import random
import matplotlib.pyplot as plt
from fpdf import FPDF
#Gerador de numeros

def gerar_numeros_aleatorios_unicos(quantidade, limite_inferior, limite_superior):
    return random.sample(range(limite_inferior, limite_superior), quantidade)

def adicionar_prefixo(numeros, prefixo):
    return str(prefixo) + ''.join(f'{numero:01}' for numero in numeros)

def gerar_relatorio():
    conexao = net.connect("Trabalho.db")
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM Alunos')
    alunos = cursor.fetchall()
    cursor.execute('SELECT * FROM Professor')
    professores = cursor.fetchall()
    cursor.execute('SELECT * FROM Disciplinas')
    disciplinas = cursor.fetchall()
    cursor.execute('SELECT * FROM Cursos')
    cursos = cursor.fetchall()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Relatório da Instituição", ln=True, align='C')
    
    pdf.cell(200, 10, txt="Alunos:", ln=True, align='L')
    for aluno in alunos:
        pdf.cell(200, 10, txt=f"ID: {aluno[0]} | Nome: {aluno[1]} | Curso: {aluno[2]} | Disciplina: {aluno[3]}", ln=True, align='L')
    
    pdf.cell(200, 10, txt="Professores:", ln=True, align='L')
    for professor in professores:
        pdf.cell(200, 10, txt=f"ID: {professor[0]} | Nome: {professor[1]} | Curso: {professor[2]} | Disciplina: {professor[3]}", ln=True, align='L')
    
    pdf.cell(200, 10, txt="Disciplinas:", ln=True, align='L')
    for disciplina in disciplinas:
        pdf.cell(200, 10, txt=f"ID: {disciplina[0]} | Nome: {disciplina[1]} | Curso: {disciplina[2]}", ln=True, align='L')
    
    pdf.cell(200, 10, txt="Cursos:", ln=True, align='L')
    for curso in cursos:
        pdf.cell(200, 10, txt=f"ID: {curso[0]} | Nome: {curso[1]}", ln=True, align='L')
    
    # Contar a quantidade de alunos em cada curso
    cursos_alunos = {}
    for aluno in alunos:
        curso = aluno[2]
        if curso in cursos_alunos:
            cursos_alunos[curso] += 1
        else:
            cursos_alunos[curso] = 1

    # Remover duplicatas e padronizar o nome dos cursos
    cursos_unicos = {}
    for curso, quantidade in cursos_alunos.items():
        curso_padronizado = curso.strip().lower()  # Remover espaços em branco e converter para minúsculas
        if curso_padronizado in cursos_unicos:
            cursos_unicos[curso_padronizado] += quantidade
        else:
            cursos_unicos[curso_padronizado] = quantidade

    # Ordenar os cursos pela quantidade de alunos (em ordem decrescente)
    cursos_ordenados = sorted(cursos_unicos.items(), key=lambda item: item[1], reverse=True)
    cursos = [item[0] for item in cursos_ordenados]
    quantidade_alunos = [item[1] for item in cursos_ordenados]

    # Gerar o gráfico de dispersão invertido
    plt.figure(figsize=(10, 5))
    plt.scatter(quantidade_alunos, cursos, color='blue')
    plt.xlabel('Quantidade de Alunos')
    plt.ylabel('Curso')
    plt.title('Quantidade de Alunos por Curso')
    plt.yticks(range(len(cursos)), cursos)  # Rotula o eixo y com os nomes dos cursos
    plt.tight_layout()
    plt.savefig('grafico_dispersao.png')
    plt.close()

    # Ajustar a largura da imagem para caber no PDF
    pdf.image('grafico_dispersao.png', x=10, y=None, w=190)  # Largura ajustada para caber na página

    pdf.output("relatorio_instituicao.pdf")

    cursor.close()
    conexao.close()

    sucesso = tk.Tk()
    sucesso.title("Relatório")
    sucesso_label = tk.Label(sucesso, text="Relatório gerado com sucesso!")
    sucesso_label.pack()



#Def's
def error():
    #Mensagem após errar senha ou usuário de Login
    erro = tk.Tk()
    erro.title("Erro")
    erro_label = tk.Label(erro, text="Usuário/Senha incorretos!")
    erro_label.pack()
#Alunos    
def aluno():
    #Janela do Aluno, Consulta o Nome do Aluno
    janela_alunos = tk.Toplevel()
    janela_alunos.title("Alunos")
    nome_label = tk.Label(janela_alunos, text="Nome")
    nome_label.pack()
    
    exit = tk.Button(janela_alunos, text="Voltar", command=lambda: inicio(janela_alunos))
    exit.pack()
    
#Professor
def janela_professor():
    #Janela do Professor, Tem as funções Adicionar, Checar e Excluir
    professor = tk.Toplevel()
    professor.title("Professor")
    professor.geometry("250x300")

    see_aluno = tk.Button(professor, text="Visualizar\n Aluno",command=procurar_alunos_por_disciplina_janela)
    see_aluno.grid(row=0,column=0,padx=5,pady=5)
    
    see_disciplinas = tk.Button(professor, text="Visualizar\n Disicplinas", command=disciplinas_curso_janela)
    see_disciplinas.grid(row=0, column=1, padx=5, pady=5)
    
    see_professor = tk.Button(professor, text="Visualizar\n Professor(Disciplina)", command=professor_disciplina_janela)
    see_professor.grid(row=0,column=2,padx=5,pady=5)
    
    see_professor_C = tk.Button(professor, text="Visualizar\n Professor(Curso)", command=professor_curso_janela)
    see_professor_C.grid(row=0,column=3,padx=5,pady=5)
    
    gerar_relatorios = tk.Button(professor, text="Relatório", command=gerar_relatorio)
    gerar_relatorios.grid(row=0, column=4, padx=5,pady=5)
    
    exit = tk.Button(professor, text="Voltar", command=lambda: inicio(professor))
    exit.grid(row=2,column=0, padx=5,pady=5)

#P_alunos------------------------------|
def procurar_alunos_por_disciplina_janela():
    global disciplina_entry
    p_aluno = tk.Toplevel()
    p_aluno.title("Procurar Aluno")
    p_aluno.geometry("200x300")
    
    disciplina = tk.Label(p_aluno, text="Disciplina")
    disciplina.grid(row=0,column=0, padx=5,pady=5)
    
    disciplina_entry = tk.Entry(p_aluno)
    disciplina_entry.grid(row=0,column=1, padx=5, pady=5)
    
    enter = tk.Button(p_aluno, text="Enter", command=lambda: procurar_alunos_por_disciplina(disciplina_entry.get()))
    enter.grid(row=1,column=0, padx=5,pady=5)
def procurar_alunos_por_disciplina(disciplina):
    disciplina_entry.delete(0, 'end')
    conexao = net.connect("Trabalho.db")
    cursor = conexao.cursor()
    
    info_janela = tk.Toplevel()
    info_janela.title("Aluno(s)")
    info_janela.withdraw()
    
    info_label = tk.Label(info_janela,text='')
    info_label.pack()
    
    cursor.execute('''SELECT * FROM Alunos JOIN Disciplinas ON Alunos.Disciplina = Disciplinas.Nome WHERE Disciplina = ?''', (disciplina,))
    alunos = cursor.fetchall()
    info = ""

    if alunos:
        for aluno in alunos:
            info += f"ID: {aluno[0]} | Nome: {aluno[1]} | Curso: {aluno[2]} | Disciplina: {aluno[3]} |\n"
    
    info_janela.deiconify()
    info_label.config(text=info)

    
    conexao.commit()
    cursor.close()
    conexao.close()
#--------------------------------------|   
#P_Disciplinas-------------------------|
def disciplinas_curso_janela():
    global disciplina_entry
    p_disciplinas = tk.Toplevel()
    p_disciplinas.title("Procurar Disciplinas")
    p_disciplinas.geometry("200x300")
    
    disciplina = tk.Label(p_disciplinas, text="Curso")
    disciplina.grid(row=0,column=0, padx=5,pady=5)
    
    disciplina_entry = tk.Entry(p_disciplinas)
    disciplina_entry.grid(row=0,column=1, padx=5, pady=5)
    
    enter = tk.Button(p_disciplinas, text="Enter", command=lambda:disciplianas_curso(disciplina_entry.get()))
    enter.grid(row=1,column=0, padx=5,pady=5)
def disciplianas_curso(curso):    
    disciplina_entry.delete(0, 'end')
    conexao = net.connect("Trabalho.db")
    cursor = conexao.cursor()
    
    info_janela = tk.Toplevel()
    info_janela.title("Curso(s)")
    info_janela.withdraw()
    
    info_label = tk.Label(info_janela,text='')
    info_label.pack()
    
    cursor.execute('''SELECT * FROM Disciplinas JOIN Cursos ON Disciplinas.Curso = Cursos.Nome WHERE Curso = ?''', (curso,))
    alunos = cursor.fetchall()
    info = ""

    if alunos:
        for aluno in alunos:
            info += f"ID: {aluno[0]} | Nome: {aluno[1]} | Curso: {aluno[2]} |\n"
    
    info_janela.deiconify()
    info_label.config(text=info)

    
    conexao.commit()
    cursor.close()
    conexao.close()
#--------------------------------------|
#P_Professor_Disciplina----------------|
def professor_disciplina_janela():
    global disciplina_entry
    p_professor = tk.Toplevel()
    p_professor.title("Procurar Professor")
    p_professor.geometry("200x300")
    
    disciplina = tk.Label(p_professor, text="Disciplina")
    disciplina.grid(row=0,column=0, padx=5,pady=5)
    
    disciplina_entry = tk.Entry(p_professor)
    disciplina_entry.grid(row=0,column=1, padx=5, pady=5)
    
    enter = tk.Button(p_professor, text="Enter", command=lambda:professor_disciplina(disciplina_entry.get()))
    enter.grid(row=1,column=0, padx=5,pady=5)
def professor_disciplina(disciplina):
    disciplina_entry.delete(0, 'end')
    conexao = net.connect("Trabalho.db")
    cursor = conexao.cursor()
    
    info_janela = tk.Toplevel()
    info_janela.title("Professor(es)")
    info_janela.withdraw()
    
    info_label = tk.Label(info_janela,text='')
    info_label.pack()
    
    cursor.execute('''SELECT * FROM Professor WHERE Disciplina = ?''', (disciplina,))
    alunos = cursor.fetchall()
    info = ""

    if alunos:
        for aluno in alunos:
            info += f"ID: {aluno[0]} | Nome: {aluno[1]} | Curso: {aluno[2]} | Disciplina: {aluno[3]} |\n"
    
    info_janela.deiconify()
    info_label.config(text=info)

    
    conexao.commit()
    cursor.close()
    conexao.close()
#--------------------------------------|
#P_Professor_Curso---------------------|
def professor_curso_janela():
    global disciplina_entry
    p_professor = tk.Toplevel()
    p_professor.title("Procurar Professor")
    p_professor.geometry("200x300")
    
    disciplina = tk.Label(p_professor, text="Curso")
    disciplina.grid(row=0,column=0, padx=5,pady=5)
    
    disciplina_entry = tk.Entry(p_professor)
    disciplina_entry.grid(row=0,column=1, padx=5, pady=5)
    
    enter = tk.Button(p_professor, text="Enter", command=lambda:professor_curso(disciplina_entry.get()))
    enter.grid(row=1,column=0, padx=5,pady=5)
def professor_curso(curso):
    disciplina_entry.delete(0, 'end')
    conexao = net.connect("Trabalho.db")
    cursor = conexao.cursor()
    
    info_janela = tk.Toplevel()
    info_janela.title("Professore(es)")
    info_janela.withdraw()
    
    info_label = tk.Label(info_janela,text='')
    info_label.pack()
    
    cursor.execute('''SELECT * FROM Professor WHERE Curso = ?''', (curso,))
    alunos = cursor.fetchall()
    info = ""

    if alunos:
        for aluno in alunos:
            info += f"ID: {aluno[0]} | Nome: {aluno[1]} | Curso: {aluno[2]} | Disciplina: {aluno[3]} |\n"
    
    info_janela.deiconify()
    info_label.config(text=info)

    
    conexao.commit()
    cursor.close()
    conexao.close()
#--------------------------------------|


     
#Diretor-------------------------------|
def diretor():
    global janela_diretor
    janela_diretor = tk.Toplevel()
    janela_diretor.title("Diretor")
    janela_diretor.geometry("600x300")   
    
    cad_aluno = tk.Button(janela_diretor,text="Cadastrar aluno", command=add_aluno_janela)
    cad_aluno.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
    
    del_alunos = tk.Button(janela_diretor,text="Deletar Aluno", command=del_alunos_janela)
    del_alunos.grid(row=1,column=0,padx=5,pady=5,sticky=tk.W)   
    
    cad_professor = tk.Button(janela_diretor, text="Cadastrar Professor", command=add_professor_janela)
    cad_professor.grid(row=0,column=1,padx=5,pady=5,sticky=tk.W) 
    
    del_professor = tk.Button(janela_diretor, text="Deletear Professor", command=del_professor_janela)
    del_professor.grid(row=1,column=1,padx=5,pady=5,sticky=tk.W)    
    
    cad_disciplina = tk.Button(janela_diretor, text="Cadastrar Disciplina", command=add_disciplina_janela)
    cad_disciplina.grid(row=0,column=2,padx=5,pady=5)
    
    del_disciplina = tk.Button(janela_diretor, text="Deletear Disciplina", command=del_disciplina_janela)
    del_disciplina.grid(row=1,column=2,padx=5,pady=5,sticky=tk.W)  
    
    cad_curso = tk.Button(janela_diretor, text="Cadastrar Curso", command=add_curso_janela)
    cad_curso.grid(row=0,column=3,padx=5,pady=5)
    
    del_curso = tk.Button(janela_diretor, text="Deletear Curso", command=del_curso_janela)
    del_curso.grid(row=1,column=3,padx=5,pady=5,sticky=tk.W) 
    
    exit = tk.Button(janela_diretor, text="Voltar", command=lambda: inicio(janela_diretor))
    exit.grid(row=2,column=0, padx=5,pady=5)   
#Add_alunos----------------------------|
def add_aluno_janela():
    global nome_entry, curso_entry, disciplina_entry
    add_janela = tk.Toplevel()
    add_janela.title("Cadastro de aluno")
    add_janela.geometry("200x300")

    nome = tk.Label(add_janela, text="Aluno")
    nome.grid(row=0,column=0,padx=5,pady=5)
    nome_entry = tk.Entry(add_janela)
    nome_entry.grid(row=0,column=1,padx=5,pady=5)
    
    curso = tk.Label(add_janela, text="Curso")
    curso.grid(row=1,column=0,padx=5,pady=5)
    curso_entry = tk.Entry(add_janela)
    curso_entry.grid(row=1,column=1,padx=5,pady=5)
    
    disciplina = tk.Label(add_janela, text="Disciplina")
    disciplina.grid(row=2,column=0,padx=5,pady=5)
    disciplina_entry = tk.Entry(add_janela)
    disciplina_entry.grid(row=2,column=1,padx=5,pady=5)
    
    add_button = tk.Button(add_janela, text="Enter", command=lambda: add_aluno(nome_entry.get(),curso_entry.get(),disciplina_entry.get()))
    add_button.grid(row=3,column=0,padx=5,pady=5)  
def add_aluno(nome,curso,disciplina):
    nome_entry.delete(0, 'end')
    curso_entry.delete(0,'end')
    disciplina_entry.delete(0, 'end')    
    conexao = net.connect("Trabalho.db")
    cursor = conexao.cursor()
    # Parâmetros
    quantidade_numeros = 8
    limite_inferior = 0
    limite_superior = 10 # Limite ajustado para garantir dois dígitos para cada número gerado

    # Gerar números aleatórios únicos
    numeros_aleatorios = gerar_numeros_aleatorios_unicos(quantidade_numeros, limite_inferior, limite_superior)

    # Adicionar o prefixo "2024"
    numero_completo_str = adicionar_prefixo(numeros_aleatorios, 2024)

    # Converter para inteiro
    numero_de_matricula = int(numero_completo_str)

    # Exibir o resultado
    print(numero_de_matricula)
    
    cursor.execute('''INSERT INTO Alunos(ID,Nome,Curso,Disciplina) VALUES (?, ?, ?, ?)''',(numero_de_matricula,nome,curso,disciplina))
    
    conexao.commit()
    cursor.close()
    conexao.close()
#--------------------------------------| 
#Delete_alunos-------------------------|
def del_alunos_janela():
    global id_entry
    del_janela = tk.Toplevel()
    del_janela.title("Deletar Aluno")
    del_janela.geometry("200x300")
    
    id = tk.Label(del_janela, text="ID")
    id.grid(row=0,column=0,padx=5,pady=5)
    id_entry = tk.Entry(del_janela)
    id_entry.grid(row=0,column=1,padx=5,pady=5)
    
    del_button = tk.Button(del_janela, text="Enter", command=lambda: del_aluno(id_entry.get()))
    del_button.grid(row=1,column=0, padx=5,pady=5)
def del_aluno(Id):
    id_entry.delete(0, 'end')
    conexao = net.connect("Trabalho.db")
    cursor = conexao.cursor()
    
    cursor.execute('''DELETE FROM Alunos WHERE ID = ?''', (Id,))
    
    conexao.commit()
    cursor.close()
    conexao.close()
#--------------------------------------|   
#Add_Professor-------------------------|
def add_professor_janela():
    global nome_entry, curso_entry, disciplina_entry
    add_p_janela = tk.Toplevel()
    add_p_janela.title("Cadastrar Professor")
    add_p_janela.geometry("300x200")

    nome = tk.Label(add_p_janela, text="Professor")
    nome.grid(row=0,column=0,padx=5,pady=5)
    nome_entry = tk.Entry(add_p_janela)
    nome_entry.grid(row=0,column=1,padx=5,pady=5)
    
    curso = tk.Label(add_p_janela, text="Curso")
    curso.grid(row=1,column=0,padx=5,pady=5)
    curso_entry = tk.Entry(add_p_janela)
    curso_entry.grid(row=1,column=1,padx=5,pady=5)
    
    disciplina = tk.Label(add_p_janela, text="Disciplina")
    disciplina.grid(row=2,column=0,padx=5,pady=5)
    disciplina_entry = tk.Entry(add_p_janela)
    disciplina_entry.grid(row=2,column=1,padx=5,pady=5)
    
    add_button = tk.Button(add_p_janela, text="Enter", command=lambda: add_professor(nome_entry.get(),curso_entry.get(),disciplina_entry.get()))
    add_button.grid(row=3,column=0,padx=5,pady=5)   
def add_professor(nome, curso, disciplina):
    nome_entry.delete(0, 'end')
    curso_entry.delete(0,'end')
    disciplina_entry.delete(0, 'end')    
    conexao = net.connect("Trabalho.db")
    cursor = conexao.cursor()
    # Parâmetros
    quantidade_numeros = 5
    limite_inferior = 0
    limite_superior = 10 # Limite ajustado para garantir dois dígitos para cada número gerado
    # Gerar números aleatórios únicos
    numeros_aleatorios = gerar_numeros_aleatorios_unicos(quantidade_numeros, limite_inferior, limite_superior)
    # Adicionar o prefixo "2024"
    numero_completo_str = adicionar_prefixo(numeros_aleatorios, 2024)
    # Converter para inteiro
    numero_de_matricula = int(numero_completo_str)
    # Exibir o resultado
    print(numero_de_matricula)
    
    cursor.execute('''INSERT INTO Professor (ID,Nome,Curso,Disciplina) VALUES (?, ?, ?, ?)''',(numero_de_matricula,nome,curso,disciplina))
    
    conexao.commit()
    cursor.close()
    conexao.close()
#--------------------------------------|
#Delete_professor----------------------|
def del_professor_janela():
    global id_entry
    del_janela = tk.Toplevel()
    del_janela.title("Deletar Professor")
    del_janela.geometry("300x200")
    
    id = tk.Label(del_janela, text="ID")
    id.grid(row=0,column=0,padx=5,pady=5)
    id_entry = tk.Entry(del_janela)
    id_entry.grid(row=0,column=1,padx=5,pady=5)
    
    del_button = tk.Button(del_janela, text="Enter", command=lambda: del_professor(id_entry.get()))
    del_button.grid(row=1,column=0, padx=5,pady=5)   
def del_professor(Id):
    id_entry.delete(0, 'end')
    conexao = net.connect("Trabalho.db")
    cursor = conexao.cursor()
    
    cursor.execute('''DELETE FROM Professor WHERE ID = ?''', (Id,))
    
    conexao.commit()
    cursor.close()
    conexao.close()
#--------------------------------------|
#Add_disciplina------------------------|
def add_disciplina_janela():
    global nome_entry, curso_entry, disciplina_entry
    add_d_janela = tk.Toplevel()
    add_d_janela.title("Cadastrar Disciplina")
    add_d_janela.geometry("300x200")

    nome = tk.Label(add_d_janela, text="Disciplina")
    nome.grid(row=0,column=0,padx=5,pady=5)
    nome_entry = tk.Entry(add_d_janela)
    nome_entry.grid(row=0,column=1,padx=5,pady=5)
    
    curso = tk.Label(add_d_janela, text="Curso")
    curso.grid(row=1,column=0,padx=5,pady=5)
    curso_entry = tk.Entry(add_d_janela)
    curso_entry.grid(row=1,column=1,padx=5,pady=5)
    
    add_button = tk.Button(add_d_janela, text="Enter", command=lambda: add_disciplina(nome_entry.get(),curso_entry.get()))
    add_button.grid(row=3,column=0,padx=5,pady=5)   
def add_disciplina(nome, curso):
    nome_entry.delete(0, 'end')
    curso_entry.delete(0,'end')    
    conexao = net.connect("Trabalho.db")
    cursor = conexao.cursor()
    # Parâmetros
    quantidade_numeros = 4
    limite_inferior = 0
    limite_superior = 10 # Limite ajustado para garantir dois dígitos para cada número gerado
    # Gerar números aleatórios únicos
    numeros_aleatorios = gerar_numeros_aleatorios_unicos(quantidade_numeros, limite_inferior, limite_superior)
    # Adicionar o prefixo "2024"
    numero_completo_str = adicionar_prefixo(numeros_aleatorios, 'ARA')
    # Converter para inteiro
    numero_de_matricula = str(numero_completo_str)
    # Exibir o resultado
    print(numero_de_matricula)
    
    cursor.execute('''INSERT INTO Disciplinas (ID,Nome,Curso) VALUES (?, ?, ?)''',(numero_de_matricula,nome,curso))
    
    conexao.commit()
    cursor.close()
    conexao.close()
#--------------------------------------|
#Delete_Disciplina---------------------|
def del_disciplina_janela():
    global id_entry
    del_janela = tk.Toplevel()
    del_janela.title("Deletar Disciplina")
    del_janela.geometry("300x200")
    
    id = tk.Label(del_janela, text="ID")
    id.grid(row=0,column=0,padx=5,pady=5)
    id_entry = tk.Entry(del_janela)
    id_entry.grid(row=0,column=1,padx=5,pady=5)
    
    del_button = tk.Button(del_janela, text="Enter", command=lambda: del_disciplina(id_entry.get()))
    del_button.grid(row=1,column=0, padx=5,pady=5)   
def del_disciplina(Id):
    id_entry.delete(0, 'end')
    conexao = net.connect("Trabalho.db")
    cursor = conexao.cursor()
    
    cursor.execute('''DELETE FROM Disciplinas WHERE ID = ?''', (Id,))
    
    conexao.commit()
    cursor.close()
    conexao.close()
#--------------------------------------|
#Add_Curso-----------------------------|
def add_curso_janela():
    global nome_entry
    add_c_janela = tk.Toplevel()
    add_c_janela.title("Cadastrar Curso")
    add_c_janela.geometry("300x200")

    nome = tk.Label(add_c_janela, text="Curso")
    nome.grid(row=0,column=0,padx=5,pady=5)
    nome_entry = tk.Entry(add_c_janela)
    nome_entry.grid(row=0,column=1,padx=5,pady=5)
    
    add_button = tk.Button(add_c_janela, text="Enter", command=lambda: add_curso(nome_entry.get()))
    add_button.grid(row=3,column=0,padx=5,pady=5)   
def add_curso(nome):
    nome_entry.delete(0, 'end')  
    conexao = net.connect("Trabalho.db")
    cursor = conexao.cursor()
    # Parâmetros
    quantidade_numeros = 4
    limite_inferior = 0
    limite_superior = 10 # Limite ajustado para garantir dois dígitos para cada número gerado
    # Gerar números aleatórios únicos
    numeros_aleatorios = gerar_numeros_aleatorios_unicos(quantidade_numeros, limite_inferior, limite_superior)
    # Adicionar o prefixo "CRS"
    numero_completo_str = adicionar_prefixo(numeros_aleatorios, 'CRS')
    # Converter para inteiro
    numero_de_matricula = str(numero_completo_str)
    # Exibir o resultado
    print(numero_de_matricula)
    
    cursor.execute('''INSERT INTO Cursos (ID,Nome) VALUES (?, ?)''',(numero_de_matricula,nome))
    
    conexao.commit()
    cursor.close()
    conexao.close()    
#--------------------------------------|
#Delete_curso--------------------------|
def del_curso_janela():
    global id_entry
    del_janela = tk.Toplevel()
    del_janela.title("Deletar Curso")
    del_janela.geometry("300x200")
    
    id = tk.Label(del_janela, text="ID")
    id.grid(row=0,column=0,padx=5,pady=5)
    id_entry = tk.Entry(del_janela)
    id_entry.grid(row=0,column=1,padx=5,pady=5)
    
    del_button = tk.Button(del_janela, text="Enter", command=lambda: del_curso(id_entry.get()))
    del_button.grid(row=1,column=0, padx=5,pady=5)   
def del_curso(Id):
    id_entry.delete(0, 'end')
    conexao = net.connect("Trabalho.db")
    cursor = conexao.cursor()
    
    cursor.execute('''DELETE FROM Cursos WHERE ID = ?''', (Id,))
    
    conexao.commit()
    cursor.close()
    conexao.close()
#--------------------------------------|
def autenticacao():
    #Janela de Login
    global autenticar,user, senha, user_entry, senha_entry
    root.withdraw()
    autenticar = tk.Toplevel()
    autenticar.title("Login")
    autenticar.geometry("225x110")
    user_label = tk.Label(autenticar, text="Usuário")
    senha_label = tk.Label(autenticar, text="Senha")
    user_entry = tk.Entry(autenticar)
    senha_entry = tk.Entry(autenticar, show="*")  
    user_label.grid(row=0,column=0,padx=8,pady=5)
    user_entry.grid(row=0,column=1,padx=8,pady=5)
    senha_label.grid(row=1,column=0,padx=8,pady=5)
    senha_entry.grid(row=1,column=1,padx=8,pady=5)
    user = "Prof"
    senha = "0101"
    verificar_button = tk.Button(autenticar, text="Enter",padx=7, command=lambda:verificacao(user_entry.get(),senha_entry.get()))
    verificar_button.grid(row=3, column=0)
    
    exit = tk.Button(autenticar, text="Voltar", command=lambda: inicio(autenticar))
    exit.grid(row=3,column=1, padx=5,pady=5)
    
def verificacao(user,senha):
    #Login
    user1 = "Prof"
    senha1 = "0101"
    user2 = "dir"
    senha2 = "1010"
    if user == user1 and senha == senha1:
        autenticar.withdraw()
        janela_professor()
        
    elif user == user2 and senha == senha2:
        autenticar.withdraw()
        diretor()
    else:
        senha_entry.delete(0, 'end')
        error()
def iniciar_db():
    conexao = net.connect("Trabalho.db")
    cursor = conexao.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Cursos(
                ID INTEGER NOT NULL,
                Nome TEXT PRIMARY KEY
                );''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Professor(
                ID INTEGER NOT NULL,
                Nome TEXT PRIMARY KEY,
                Curso TEXT,
                Disciplina TEXT,
                FOREIGN KEY (Curso) REFERENCES Cursos(Nome)
                FOREIGN KEY (Disciplina) REFERENCES Disciplinas(Nome)
                 );''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Disciplinas(
                    ID TEXT NOT NULL,
                    Nome TEXT PRIMARY KEY,
                    Curso TEXT,
                    FOREIGN KEY (Curso) REFERENCES Cursos(Nome)
                );''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Alunos(
                    ID INTEGER NOT NULL, 
                    Nome TEXT,
                    Curso TEXT,
                    Disciplina TEXT,
                    FOREIGN KEY (Curso) REFERENCES Cursos(Nome)
                    FOREIGN KEY (Disciplina) REFERENCES Disciplinas(Nome)
                );''')
    
    conexao.commit()
    cursor.close()
    conexao.close()
 
def inicio(janela):
    janela.withdraw()
    root.deiconify()
    
#Janelas Principal
iniciar_db()
root = tk.Tk()
root.title("Janela Principal")
root.geometry("200x200")

form_frame = tk.Frame()
form_frame.pack(pady=20)

botao_aluno = tk.Button(form_frame,text="Alunos", command=aluno)
botao_aluno.grid(row=1,column=0,padx=5,pady=5)

botao_professor = tk.Button(form_frame, text="Login", command=autenticacao)
botao_professor.grid(row=0, column=0,padx=5,pady=5)

root.mainloop()
#Progama Principal
