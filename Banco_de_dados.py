import sqlite3 as connect
import os
def menu():
    a = 0
    while a == 0:
        print ("-----------------MENU-----------------\n 1 - Inserir informacoes nas tabelas \n 2 - Procurar \n 3 - Sair do Menu")
        op = int(input(": "))
        if op == 1:
            os.system('clear')
            print("------------------TABELAS----------------\n 1 - Diciplina \n 2 - Curso \n 3 - Aluno \n 4 - Professores")
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
                pass
        elif op == 2:
            os.system('clear')
            print("------------Procurar-------------\n 1 - Por Curso \n 2 - Por Disciplina")
            op = int(input(": "))
            if op == 1:
                procurar_curso()
            elif op == 2:
                procurar_disciplina()
            else:
                os.system('clear')
                pass
            
        elif op == 3:
            a = 1
        else:
            pass
            
def insert_Disciplina():
    os.system('clear')
    nome = input("Nome da Disciplina?: ").strip()
    
    conexao = connect.connect("Banco.db")
    cursor = conexao.cursor()
    
    cursor.execute("SELECT MAX(id) FROM Disciplina;")
    result = cursor.fetchone()
    max_id = result[0] if result[0] is not None else 0
    id = max_id + 1
    
    comando = '''INSERT INTO Disciplina (nome, id)
                 VALUES (?, ?)'''
    cursor.execute(comando, (nome, id))
    
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
    
    comando = '''INSERT INTO Curso (nome, id)
                 VALUES (?, ?)'''
    cursor.execute(comando, (nome, id))
    
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
    
    comando = '''INSERT INTO Aluno (nome, id, disciplina_id, curso_id)
                 VALUES (?, ?, ?, ?)'''
    cursor.execute(comando, (nome, id, disciplina_id, curso_id))
    
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
    
    comando = '''INSERT INTO Professor (nome, id, curso_id, disciplina_id)
                 VALUES (?, ?, ?, ?)'''
    cursor.execute(comando, (nome, id, curso_id, disciplina_id))
    
    conexao.commit()
    cursor.execute("SELECT * FROM Professor;")
    registros = cursor.fetchall()
    print("Registros na tabela Professor após inserção:", registros)
    
    cursor.close()
    conexao.close()
    
def procurar_curso():
    os.system('clear')
    comando = '''SELECT * FROM Curso'''
    cursor.execute(comando)
    result = cursor.fetchall()
    if result:
        print("-------Cursos------")
        for resultado in result:
            print("Nome: ", resultado[0])
            print("ID: ", resultado[1])
            print("--------------------")
    else:
        print("Nennhum curso cadastrado")
        
    curso_id = input("--------------------\nID do Curso: ")
    os.system('clear')
    comando = '''SELECT * FROM Aluno WHERE curso_id = ?;'''
    cursor.execute(comando, (curso_id,))
    resultados = cursor.fetchall()
    if resultados:
        print("Resultado da busca:")
        for resultado in resultados:
            print("ID:", resultado[1])
            print("Nome:", resultado[0])
            print("-----------------")
    else:
        print("Nenhum aluno encontrado matriculado neste curso.")

def procurar_disciplina():
    os.system('clear')
    comando = ''' SELECT * FROM Disciplina '''
    cursor.execute(comando)
    result = cursor.fetchall()
    if result:
        print ("----------Disciplinas----------")
        for resultados in result:
            print("ID: ", resultados[0])    
            print("Nome: ", resultados[1])
            print("------------------------------")
    else:
        print("Sem disciplinas cadastradas")
    id_disciplina = input("------------------------------\nID da Disciplina: ")
    os.system('clear') 
    comando = ''' SELECT * FROM Aluno WHERE disciplina_id = ?;'''
    cursor.execute(comando, (id_disciplina))
    resultado = cursor.fetchall()
    if resultado:
        print("Resultado da Busca: ")
        for resultados in resultado:
            print("ID: ", resultados[0])
            print("Nome: ", resultados[1])
            print("----------------------------")
    else:
        print("Não há alunos matriculados nessa disciplina")
        
try:        
    conexao = connect.connect("Banco.db")
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Disciplina (
                        nome TEXT NOT NULL UNIQUE,
                        id INTEGER NOT NULL,
                        PRIMARY KEY (id)
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
    # Fechar o cursor e a conexão
    if cursor:
        cursor.close()
    if conexao:
        conexao.close()
