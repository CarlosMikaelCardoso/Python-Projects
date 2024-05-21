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
            print("1 - Disciplina")
            print("2 - Curso")
            print("3 - Aluno")
            print("4 - Professores")
            op = int(input(": "))
            if op == 1:
                insert_Disciplina()
            elif op == 2:
                insert_Curso()
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
            op = int(input(": "))
            if op == 1:
                procurar_curso()
            elif op == 2:
                procurar_disciplina()
            elif op == 3:
                procurar_professor_curso()
            elif op == 4:
                procurar_professor_disciplina()
            else:
                os.system('clear')
        elif op == 3:
            break
        else:
            os.system('clear')

def insert_Disciplina():
    os.system('clear')
    nome = input("Nome da Disciplina?: ").strip()
    
    conexao = connect.connect("Banco.db")
    cursor = conexao.cursor()
    
    cursor.execute("SELECT MAX(id) FROM Disciplina;")
    result = cursor.fetchone()
    max_id = result[0] if result[0] is not None else 0
    id = max_id + 1
    
    cursor.execute("INSERT INTO Disciplina (nome, id) VALUES (?, ?)", (nome, id))
    
    conexao.commit()
    cursor.execute("SELECT * FROM Disciplina;")
    registros = cursor.fetchall()
    print("Registros na tabela Disciplina após inserção:", registros)
    
    cursor.close()
    conexao.close()

def insert_Curso():
    os.system('clear')
    nome = input("Nome do Curso?: ").strip()
    id_disciplina = input("ID da disciplina associada ao curso: ")
    
    conexao = connect.connect("Banco.db")
    cursor = conexao.cursor()
    
    cursor.execute("SELECT MAX(id) FROM Curso;")
    result = cursor.fetchone()
    max_id = result[0] if result[0] is not None else 0
    id = max_id + 1
    
    cursor.execute("INSERT INTO Curso (nome, id, id_disciplina) VALUES (?, ?, ?)", (nome, id, id_disciplina))
    
    conexao.commit()
    cursor.execute("SELECT * FROM Curso;")
    registros = cursor.fetchall()
    print("Registros na tabela Curso após inserção:", registros)
    
    cursor.close()
    conexao.close()

def insert_Aluno():
    os.system('clear')
    nome = input("Nome do Aluno?: ").strip()
    disciplina_id = int(input("ID da Disciplina?: "))
    curso_id = int(input("ID do Curso?: "))
    
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
           
try:        
    conexao = connect.connect("Banco.db")
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Disciplina (
                        nome TEXT NOT NULL UNIQUE,
                        id INTEGER NOT NULL,
                        PRIMARY KEY (id)
                     );''')
    
    cursor.execute(''' CREATE TABLE IF NOT EXISTS Curso(
                        nome TEXT NOT NULL,
                        id INTEGER NOT NULL,
                        id_disciplina INTEGER,
                        PRIMARY KEY (id),
                        FOREIGN KEY (id_disciplina) REFERENCES Disciplina(id)
                    );''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Aluno (
                        nome TEXT NOT NULL,
                        id INTEGER NOT NULL,
                        disciplina_id INTEGER,
                        curso_id INTEGER,
                        PRIMARY KEY (id),
                        FOREIGN KEY (disciplina_id) REFERENCES Disciplina(id),
                        FOREIGN KEY (curso_id) REFERENCES Curso(id)
                     );''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Professor(
                        nome TEXT NOT NULL,
                        id INTEGER NOT NULL,
                        curso_id INTEGER,
                        disciplina_id INTEGER,
                        PRIMARY KEY (id),
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
