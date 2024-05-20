import sqlite3 as connect

# Connect to the database (with a proper extension, e.g., .db)
conexao = connect.connect("Banco.db")

cursor = conexao.cursor()

# Corrected table creation commands
comando = ''' CREATE TABLE Disciplina (
                nome TEXT NOT NULL UNIQUE,
                id INTEGER NOT NULL,
                PRIMARY KEY (nome)
                );'''
cursor.execute(comando)

comando = ''' CREATE TABLE Curso(
                nome TEXT NOT NULL UNIQUE,
                id INTEGER NOT NULL,
                PRIMARY KEY (nome) 
                );'''
cursor.execute(comando)

comando = ''' CREATE TABLE Aluno (
                id INTEGER NOT NULL UNIQUE,
                nome TEXT NOT NULL,
                disciplina_nome TEXT,
                curso_nome TEXT,
                PRIMARY KEY (id),
                FOREIGN KEY (disciplina_nome) REFERENCES Disciplina(nome),
                FOREIGN KEY (curso_nome) REFERENCES Curso(nome)
                );'''
cursor.execute(comando)
cursor.fetchall()

# Close the cursor and the connection
cursor.close()
conexao.close()
