import tkinter as tk
import sqlite3 as connect 
import random
#Gerador de numeros

def gerar_numeros_aleatorios_unicos(quantidade, limite_inferior, limite_superior):
    return random.sample(range(limite_inferior, limite_superior), quantidade)

def adicionar_prefixo(numeros, prefixo):
    return str(prefixo) + ''.join(f'{numero:01}' for numero in numeros)



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
    alunos = tk.Toplevel()
    alunos.title("Alunos")
    nome_label = tk.Label(alunos, text="Nome")
    nome_label.pack()
#Professor
def janela_professor():
    #Janela do Professor, Tem as funções Adicionar, Checar e Excluir
    professor = tk.Toplevel()
    professor.title("Professor")
    professor.geometry("250x300")
#Diretor
def diretor():
    janela_diretor = tk.Toplevel()
    janela_diretor.title("Diretor")
    janela_diretor.geometry("600x300")   
    
    cad_aluno = tk.Button(janela_diretor,text="Cadastrar aluno", command=add_aluno_janela)
    cad_aluno.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
    
    del_alunos = tk.Button(janela_diretor,text="Deletar Aluno")
    del_alunos.grid(row=1,column=0,padx=5,pady=5,sticky=tk.W)   
    
    cad_professor = tk.Button(janela_diretor, text="Cadastrar Professor")
    cad_professor.grid(row=0,column=1,padx=5,pady=5,sticky=tk.W) 
    
    del_professor = tk.Button(janela_diretor, text="Deletear Professor")
    del_professor.grid(row=1,column=1,padx=5,pady=5,sticky=tk.W)

def add_aluno_janela():
    global nome_entry, curso_entry, disciplina_entry
    add_janela = tk.Toplevel()
    add_janela.title("Cadastro de aluno")
    add_janela.geometry("200x200")

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
    conexao = connect.connect("Trabalho.db")
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
#--------------------------------------
def autenticacao():
    #Janela de Login
    global autenticar, user, senha, user_entry, senha_entry
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
    conexao = connect.connect("Trabalho.db")
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
                    ID INTEGER NOT NULL,
                    Nome TEXT PRIMARY KEY,
                    Curso TEXT,
                    Professor TEXT,
                    FOREIGN KEY (Curso) REFERENCES Cursos(Nome)
                    FOREIGN KEY (Professor) REFERENCES Professor(Nome)
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
    
#Janelas Principal
iniciar_db()
root = tk.Tk()
root.title("Janela Principal")
root.geometry("200x200")

form_frame = tk.Frame()
form_frame.pack(pady=20)

botao_aluno = tk.Button(form_frame,text="Alunos", command=aluno)
botao_aluno.grid(row=0,column=0,padx=5,pady=5)

botao_professor = tk.Button(form_frame, text="Professor", command=autenticacao)
botao_professor.grid(row=0, column=1,padx=5,pady=5)

botao_diretor = tk.Button(form_frame, text="Diretor", command=autenticacao)
botao_diretor.grid(row=0, column=2,padx=5,pady=5)

root.mainloop()
#Progama Principal
