import sqlite3 as connect
import os

def menu():
    while True:
        print("-----------------MENU-----------------")
        print("1 - Inserir informacoes nas tabelas")
        print("2 - Procurar")
        print("3 - Sair do Menu")
        op = int(input(": "))
        
        if op == 1:
            os.system('clear')
            print("------------------TABELAS----------------")
            print("1 - Curso")
            print("2 - Disciplina")
            print("3 - Aluno")
            print("4 - Professores")
            op = int(input(": "))
            if op == 1:
                insert_Curso()
            elif op == 2:
                insert_Disciplina()
            elif op == 3:
                insert_Aluno()
            elif op == 4:
                insert_Professor()
            else:
                os.system('clear')
        elif op == 2:
            os.system('clear')
            print("------------Procurar-------------")
            print("1 - Aluno por Curso")
            print("2 - Aluno por Disciplina")
            print("3 - Professor por Curso")
            print("4 - Professor por Disciplina")
            print("5 - Disciplina por Curso")
            op = int(input(": "))
            if op == 1:
                procurar_curso()
            elif op == 2:
                procurar_disciplina()
            elif op == 3:
                procurar_professor_curso()
            elif op == 4:
                procurar_professor_disciplina()
            elif op == 5:
                procurar_disciplina_curso()
            else:
                os.system('clear')
        elif op == 3:
            break
        else:
            os.system('clear')

def insert_Disciplina():
    os.system('clear')
    nome = input("Nome da Disciplina?: ").strip()
    id_curso = input("ID da curso associada á Disciplina: ")
    id_professor = input("Qual professor sera responsavel pela Disciplina?: ")
        
    conexao = connect.connect("Banco.db")
    cursor = conexao.cursor()
    
    cursor.execute(''' SELECT * FROM Professor''')
    prof = cursor.fetchall()
    if prof:
        print("---------Professores-------")
        for a in prof:
            print("Nome: ", a[0])
            print("ID: ", a[1])
            print('----------------------------')
    else:
        print("Nao ha professores disponiveis!")
    
    cursor.execute("SELECT MAX(id) FROM Disciplina;")
    result = cursor.fetchone()
    max_id = result[0] if result[0] is not None else 0
    id = max_id + 1
    
    cursor.execute("INSERT INTO Disciplina (nome, id, curso_id,id_professor) VALUES (?, ?, ?, ?)", (nome, id, id_curso, id_professor))
    
    conexao.commit()
    cursor.execute("SELECT * FROM Disciplina;")
    registros = cursor.fetchall()
    print("Registros na tabela Disciplina após inserção:", registros)
    
    cursor.close()
    conexao.close()

def insert_Curso():
    os.system('clear')
    nome = input("Nome do Curso?: ").strip()
    
    conexao = connect.connect("Banco.db")
    cursor = conexao.cursor()
    
    cursor.execute("SELECT MAX(id) FROM Curso;")
    result = cursor.fetchone()
    max_id = result[0] if result[0] is not None else 0
    id = max_id + 1
    
    cursor.execute("INSERT INTO Curso (nome, id) VALUES (?, ?)", (nome, id))
    
    conexao.commit()
    cursor.execute("SELECT * FROM Curso;")
    registros = cursor.fetchall()
    print("Registros na tabela Curso após inserção:", registros)
    
    cursor.close()
    conexao.close()

def insert_Aluno():
    os.system('clear')
    nome = input("Nome do Aluno?: ").strip()
    curso_id = int(input("ID do Curso?: "))
    disciplina_id = int(input("ID da Disciplina?: "))
    
    conexao = connect.connect("Banco.db")
    cursor = conexao.cursor()
    
    cursor.execute("SELECT MAX(id) FROM Aluno;")
    result = cursor.fetchone()
    max_id = result[0] if result[0] is not None else 0
    id = max_id + 1
    
    cursor.execute("INSERT INTO Aluno (nome, id, disciplina_id, curso_id) VALUES (?, ?, ?, ?)", (nome, id, disciplina_id, curso_id))
    
    conexao.commit()
    cursor.execute("SELECT * FROM Aluno;")
    registros = cursor.fetchall()
    print("Registros na tabela Aluno após inserção:", registros)
    
    cursor.close()
    conexao.close()

def insert_Professor():
    os.system('clear')
    nome = input("Nome do Professor?: ").strip()
    curso_id = int(input("ID do Curso?: "))
    disciplina_id = int(input("ID da Disciplina?: "))
    
    conexao = connect.connect("Banco.db")
    cursor = conexao.cursor()
    
    cursor.execute("SELECT MAX(id) FROM Professor;")
    result = cursor.fetchone()
    max_id = result[0] if result[0] is not None else 0
    id = max_id + 1
    
    cursor.execute("INSERT INTO Professor (nome, id, curso_id, disciplina_id) VALUES (?, ?, ?, ?)", (nome, id, curso_id, disciplina_id))
    
    conexao.commit()
    cursor.execute("SELECT * FROM Professor;")
    registros = cursor.fetchall()
    print("Registros na tabela Professor após inserção:", registros)
    
    cursor.close()
    conexao.close()
    
def procurar_curso():
    os.system('clear')
    conexao = connect.connect("Banco.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM Curso")
    result = cursor.fetchall()
    if result:
        print("-------Cursos------")
        for resultado in result:
            print("Nome: ", resultado[0])
            print("ID: ", resultado[1])
            print("--------------------")
    else:
        os.system('clear')
        print("Nenhum curso cadastrado")
    
    curso_id = input("--------------------\nID do Curso: ")
    os.system('clear')
    cursor.execute("SELECT * FROM Aluno WHERE curso_id = ?", (curso_id,))
    resultados = cursor.fetchall()
    if resultados:
        print("Resultado da busca:")
        for resultado in resultados:
            print("ID:", resultado[1])
            print("Nome:", resultado[0])
            print("-----------------")
    else:
        os.system('clear')
        print("Nenhum aluno encontrado matriculado neste curso.")

    cursor.close()
    conexao.close()

def procurar_disciplina():
    os.system('clear')
    conexao = connect.connect("Banco.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM Disciplina")
    result = cursor.fetchall()
    if result:
        print("----------Disciplinas----------")
        for resultados in result:
            print("ID: ", resultados[0])    
            print("Nome: ", resultados[1])
            print("------------------------------")
    else:
        os.system("clear")
        print("Sem disciplinas cadastradas")
        
    id_disciplina = input("------------------------------\nID da Disciplina: ")
    os.system('clear') 
    cursor.execute("SELECT * FROM Aluno WHERE disciplina_id = ?", (id_disciplina,))
    resultado = cursor.fetchall()
    if resultado:
        print("Resultado da Busca: ")
        for resultados in resultado:
            print("ID: ", resultados[0])
            print("Nome: ", resultados[1])
            print("----------------------------")
    else:
        os.system('clear')
        print("Não há alunos matriculados nessa disciplina")

    cursor.close()
    conexao.close()
   
def procurar_professor_curso():
    os.system('clear')
    conexao = connect.connect("Banco.db")
    cursor = conexao.cursor()
    
    cursor.execute(''' SELECT * FROM Curso ''')
    result = cursor.fetchall()

    if result:
        print("------Cursos------")
        for resultado in result:
            print("Nome: ",resultado[0])
            print("ID: ", resultado[1]) 
            print("-----------------")       
    else:
        os.system('clear')
        print("Não cursos cadastrados!")
     
    id_curso = input("-----------------\n ID do curso: ")
    os.system('clear')   
    cursor.execute(''' SELECT * FROM Professor WHERE curso_id=?''', (id_curso))
    resultado = cursor.fetchall()
    
    if resultado:
        print("-----Professores-----")
        for resultados in resultado:
            print("Nome: ", resultados[0])
            print("ID: ", resultados[1])
            print('---------------------')
    else:
        os.system("clear")
        print("Nao ha professore administrando esse curso")
        
    cursor.close()
    conexao.close()
 
def procurar_professor_disciplina():
    os.system('clear')
    conexao = connect.connect("Banco.db")
    cursor = conexao.cursor()
    
    cursor.execute(''' SELECT * FROM Disciplina ''')
    result = cursor.fetchall()
    
    if result:
        print("-----Professores-----")
        for resultado in result:
            print("Nome: ", resultado[0])
            print("ID: ", resultado[1])
            print("---------------------")
    else: 
        os.system('clear')
        print("Nao ha professores cadastrados nas disciplinas")
        
    id_disciplina = input("------------------\nID da disciplina: ")   
    os.system('clear')
    cursor.execute(''' SELECT * FROM Professor WHERE disciplina_id = ?; ''', (id_disciplina))
    resultado = cursor.fetchall()
    if resultado:
        print("-----Professores-----")
        for resultados in resultado:
            print("Nome: ", resultados[0])
            print("ID: ", resultados[1])
            print("---------------------")
    else: 
        os.system("clear")
        print("Nao ha professres ministrando essa disciplina!")
        
    cursor.close()
    conexao.close()
  
def procurar_disciplina_curso():
    os.system('clear')
    conexao = connect.connect("Banco.db")
    cursor = conexao.cursor()
    
    cursor.execute(''' SELECT * FROM Curso ''')
    result = cursor.fetchall()
    
    if result:
        print("------Cursos------")
        for resultado in result:
            print("Nome: ", resultado[0])
            print("ID: ", resultado[1])
            print("------------------")
            
    else: 
        os.system("clear")
        print("Nao ha curso cadastrados!")
    
    id_curso = input("------------------\nID do curso: ")
    cursor.execute(''' SELECT * FROM Disciplina WHERE curso_id = ?''', (id_curso,))

    resultado = cursor.fetchall()
    
    if resultado:
        os.system('clear')
        print("-----Disciplinas------")
        for resultados in resultado:
            print("Nome: ", resultados[0])
            print("ID: ", resultados[1])
            print("----------------------")

    else:
        os.system("clear")
        print("Nao ha disciplinas cadastradas nesse curso")
        
    cursor.close()
    conexao.close()

def procurar_aluno_diciplina_professor():
    os.system('clear')
    conexao = connect.connect("Banco.db")
    cursor = conexao.cursor()

    cursor.excute(''' SELECT * FROM Disciplinas ''')
    result = cursor.fetchall()
    
    if result:
        os.system("clear")
        print("-----Disciplinas-----")
        for resultado in result:
            print("Nome: ", resultado[0])
            print("ID: ", resultado[1])
            print("---------------------")
    else:
        os.system("clear")
        print("Nao ha disciplinas cadastradas!")

    id_disciplina = input("-----------------\nID da disciplina: ")
    os.system("clear")
    cursor.execute(''' SELECT * FROM Professor WHERE disciplina_id = ?''', (id_disciplina))
    resultado = cursor.fetchall()
    
    if resultado:
        os.system("clear")
        print("-----Professores-----")
        for resultados in resultado:
            print("Nome: ", resultados[0])
            print("ID: ", resultados[1])
            print("---------------------")
            
    else:
        os.system("clear")
        print("Nao ha professor nessa disciplina")
        
        
    cursor.execute(''' SELECT * FROM Aluno WHERE disciplina_id = ?''', ())
    
try:        
    conexao = connect.connect("Banco.db")
    cursor = conexao.cursor()
    
    cursor.execute(''' CREATE TABLE IF NOT EXISTS Curso(
                        nome TEXT NOT NULL,
                        id INTEGER NOT NULL PRIMARY KEY
                    );''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Professor(
                    nome TEXT NOT NULL,
                    id INTEGER NOT NULL PRIMARY KEY,
                    curso_id INTEGER,
                    disciplina_id INTEGER,
                    FOREIGN KEY (curso_id) REFERENCES Curso(id),
                    FOREIGN KEY (disciplina_id) REFERENCES Disciplina(id)
                );''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Disciplina (
                        nome TEXT NOT NULL UNIQUE,
                        id INTEGER NOT NULL PRIMARY KEY,
                        curso_id INTEGER,
                        id_professor INTEGER,
                        FOREIGN KEY (curso_id) REFERENCES Curso(id),
                        FOREIGN KEY (id_professor) REFERENCES Professor(id)
                    );''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Aluno (
                        nome TEXT NOT NULL,
                        id INTEGER NOT NULL PRIMARY KEY,
                        curso_id INTEGER,
                        disciplina_id INTEGER,
                        FOREIGN KEY (curso_id) REFERENCES Curso(id),
                        FOREIGN KEY (disciplina_id) REFERENCES Disciplina(id)
                    );''')



    menu()
    conexao.commit()

except connect.Error as e:
    print("Erro ao acessar o banco de dados:", e)

finally:
    if cursor:
        cursor.close()
    if conexao:
        conexao.close()
