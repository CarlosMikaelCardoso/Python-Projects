import tkinter as tk
import sqlite3 as connect  

#Def's
def error():
    #Mensagem após errar senha ou usuário de Login
    erro = tk.Tk()
    erro.title("Erro")
    erro_label = tk.Label(erro, text="Usuário/Senha incorretos!")
    erro_label.pack()
    
def aluno():
    #Janela do Aluno, Consulta o Nome do Aluno
    alunos = tk.Toplevel()
    alunos.title("Alunos")
    nome_label = tk.Label(alunos, text="Nome")
    nome_label.pack()

def janela_professor():
    #Janela do Professor, Tem as funções Adicionar, Checar e Excluir
    professor = tk.Toplevel()
    professor.title("Professor")
    professor.geometry("250x300")

def diretor():
    janela_diretor = tk.Toplevel()
    janela_diretor.title("Diretor")
    janela_diretor.geometry("600x300")   

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
    cursor.execute('''CREATE TABLE IF NOT EXISTS Professor(
                id INTEGER NOT NULL,
                nome TEXT PRIMARY KEY,
                Disciplina TEXT,
                FOREIGN KEY (Disciplina) REFERENCES Disciplinas(nome)
            );''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Disciplinas(
                    id INTEGER NOT NULL,
                    nome TEXT PRIMARY KEY,
                    Professor TEXT,
                    FOREIGN KEY (Professor) REFERENCES Professor(nome)
                );''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Alunos(
                    id INTEGER NOT NULL, 
                    nome TEXT,
                    Disciplina TEXT,
                    FOREIGN KEY (Disciplina) REFERENCES Disciplinas(nome)
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
