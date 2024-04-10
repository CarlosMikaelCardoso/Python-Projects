import tkinter as tk
from tkinter import ttk
import pandas as pd
tabela = None
idd = 0
def error():
    #Mensagem após errar senha ou usuário de Login
    erro = tk.Tk()
    erro.title("Erro")
    erro_label = tk.Label(erro, text="Usuário/Senha incorreto!")
    erro_label.pack()

def inicio():
    #Volta para a janela root
    professor.withdraw()
    root.deiconify()
    
def inicio2():
    alunos.withdraw()
    root.deiconify()
    
def verificacao():
    #Login
    user1 = user_entry.get()
    senha1 = senha_entry.get()
    if user1 == user and senha1 == senha:
        autenticar.withdraw()
        janela_professor()
    else:
        senha_entry.delete(0, 'end')
        error()

def aluno():
    #Janela do Aluno, Consulta o Nome do Aluno
    global aluno_result, alunos, id_result
    alunos = tk.Tk()
    alunos.title("Alunos")
    nome_label = tk.Label(alunos, text="Nome")
    nome_label.pack()
    nome_buscado = tk.Entry(alunos)
    nome_buscado.pack()
    
    def busca():
        #Chama a função Buscar, Busca o nome do aluno
        nome_aluno = nome_buscado.get()  
        procurar_aluno(nome_aluno=nome_aluno) 
        
    busca_button = tk.Button(alunos, text="Buscar", command=busca, width=16, height=1)  
    busca_button.pack()
    
    voltar = tk.Button(alunos, text="Voltar", command=inicio2, width=16, height=1)
    voltar.pack()
    
    aluno_result = tk.Label(alunos, text='')
    id_result = tk.Label(alunos, text='')

def janela_professor():
    #Janela do Professor, Tem as funções Adicionar, Checar e Excluir
    global botao_janela, professor, botao_adicionar, nome_alunos, entrada_aluno, nome_nota, entrada_nota, alunos_label
    professor = tk.Toplevel()
    professor.title("Professor")
    professor.geometry("250x300")
    botao_janela = tk.Button(professor, text="Adicionar", command=chama, width=16, height=1)
    botao_janela.pack()
    botao_adicionar = tk.Button(professor, text="=", command=adicionar_aluno, width=16, height=1)
    nota_button = tk.Button(professor, text="Checar", command=notas, width=16, height=1)
    nota_button.pack()
    excluir_botao = tk.Button(professor, text="Excluir", command=excluir, width=16, height=1)
    excluir_botao.pack()
    alunos_label = tk.Label(professor, text='')
    alunos_label.pack()
    voltar = tk.Button(professor, text="Voltar", command=inicio, width=16, height=1)
    voltar.pack()

    nome_alunos = tk.Label(professor, text='Aluno')
    entrada_aluno = tk.Entry(professor)
    nome_nota = tk.Label(professor, text='Nota')
    entrada_nota = tk.Entry(professor)

def autenticacao():
    #Janela de Login
    global autenticar, user, senha, user_entry, senha_entry
    root.withdraw()
    autenticar = tk.Tk()
    autenticar.title("Login")
    autenticar.geometry("225x110")
    user_label = tk.Label(autenticar, text="Usuário")
    senha_label = tk.Label(autenticar, text="Senha")
    user_entry = tk.Entry(autenticar)
    senha_entry = tk.Entry(autenticar, show="*")  
    user_label.pack()
    user_entry.pack()
    senha_label.pack()
    senha_entry.pack()
    user = "Prof"
    senha = "0101"
    verificar_button = tk.Button(autenticar, text="Enter", command=verificacao)
    verificar_button.pack()

def configurar_qtd_alunos():
    #Quantidade de alunos a serem inseridos no Arquivo.txt 
    global qalunos, entry_qtd_alunos
    qalunos = int(entry_qtd_alunos.get())
    alunos_label.config(text=f"Inserindo informações para {qalunos} alunos")
    entry_qtd_alunos.delete(0, 'end')
    janela.destroy()
    
def chama():
    #Chama a janela Qalunos
    global janela, entry_qtd_alunos
    janela = tk.Toplevel()
    janela.title("Qalunos")

    entry_qtd_alunos = tk.Entry(janela)
    entry_qtd_alunos.pack()

    botao_configurar_qtd_alunos = tk.Button(janela, text="Configurar Quantidade de Alunos", command=configurar_qtd_alunos)
    botao_configurar_qtd_alunos.pack()
    
    nome_alunos.pack()
    entrada_aluno.pack()
    nome_nota.pack()
    entrada_nota.pack()
    botao_adicionar.pack()

def adicionar_aluno():    
    #Função para adicionar alunos
    global qalunos, idd
    idd += 1
    aluno = entrada_aluno.get()
    nota = entrada_nota.get()

    resultado.append(f"ID: {idd}|Aluno: {aluno}|Nota: {nota}")

    entrada_aluno.delete(0, 'end')
    entrada_nota.delete(0, 'end')

    if qalunos > 0:
        qalunos -= 1
        alunos_label.config(text=f"Inserindo informações para {qalunos} alunos")

    if qalunos == 0:
        #Depois da inserção dos alunos, e mostrado um planilha com as informações
        with open('arquivo.txt', 'w') as f:
            f.write('\n'.join(resultado))
            
        notas()
            
        nome_alunos.pack_forget()
        nome_nota.pack_forget()
        entrada_nota.pack_forget()
        entrada_aluno.pack_forget()
        botao_janela.pack()
        botao_adicionar.pack_forget()

def notas():
    #Criação da planilha com a biblioteca Pandas
    global tabela
    nota = tk.Tk()
    nota.title("Notas")
    
    tabela = ttk.Treeview(nota)
    tabela['columns'] = ('ID', 'Nome', 'Nota')

    # Define as colunas
    tabela.column('#0', width=0, stretch=tk.NO)  # Coluna invisível
    tabela.column('ID', anchor=tk.CENTER, width=100)
    tabela.column('Nome', anchor=tk.W, width=150)
    tabela.column('Nota', anchor=tk.CENTER, width=100)

    # Cabeçalho da tabela
    tabela.heading('ID', text='ID')
    tabela.heading('Nome', text='Nome')
    tabela.heading('Nota', text='Nota')

    # Carrega os dados do arquivo, se existir
    try:
        with open('arquivo.txt', 'r') as f:
            linha = f.readline()
            index = 0
            while linha:
                if linha.startswith('ID:'):
                    parts = linha.split('|')
                    id_ = parts[0].split(':')[1].strip()
                    nome = parts[1].split(':')[1].strip()
                    nota = parts[2].split(':')[1].strip()
                    tabela.insert('', index, values=(id_, nome, nota))
                    index += 1
                linha = f.readline()
    except FileNotFoundError:
        print("Arquivo 'arquivo.txt' não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

    if tabela is not None:
        # Empacota a tabela se ela foi inicializada corretamente
        tabela.pack(expand=True, fill=tk.BOTH)
    else:
        print("Erro: a tabela não foi inicializada corretamente.")

def procurar_aluno(nome_aluno=None):
    #Faz a proucura de alunos pelo nome
    if nome_aluno is None:
        print("É necessário fornecer o nome do aluno para procurar.")
        return
    
    with open('arquivo.txt', 'r') as f:
        alunos_encontrados = []
        for linha in f:
            if nome_aluno is not None and f"Aluno: {nome_aluno}" in linha:
                alunos_encontrados.append(linha.strip())

        if alunos_encontrados:
            resultado_texto = '\n'.join(alunos_encontrados)
            aluno_result.config(text=resultado_texto)
            aluno_result.pack()
        else:
            aluno_result.config(text=f"Aluno com o nome '{nome_aluno}' não encontrado.")
            aluno_result.pack()

def excluir():
    global excluir_entry
    #Janela de Excluir Alunos
    excluir1 = tk.Tk()
    excluir1.title("Excluir")
    notas()
    excluir_label = tk.Label(excluir1, text="ID")
    excluir_label.pack()
    excluir_entry = tk.Entry(excluir1)
    excluir_entry.pack()
    
    
    # Função lambda para chamar deletar_aluno com o ID do aluno inserido no Entry
    delta_aluno_botao = tk.Button(excluir1, text="Enter", command=lambda: deletar_aluno(excluir_entry.get()))
    delta_aluno_botao.pack()
    

def deletar_aluno(id_aluno):
    global tabela
    excluir_entry.delete(0, 'end')
    # Percorre todas as linhas da tabela
    for item in tabela.get_children():
        # Obtém o ID do aluno da linha atual
        id_atual = tabela.item(item, 'values')[0]
        # Verifica se o ID do aluno na linha atual corresponde ao ID fornecido
        if id_atual == id_aluno:
            # Remove a linha correspondente da tabela
            tabela.delete(item)
            # Atualiza o arquivo 'arquivo.txt' removendo a linha correspondente ao aluno deletado
            with open('arquivo.txt', 'r') as file:
                lines = file.readlines()
            with open('arquivo.txt', 'w') as file:
                for line in lines:
                    if f"ID: {id_aluno}" not in line:
                        file.write(line)
            return  # Sai da função após deletar o aluno
    print(f"Aluno com ID {id_aluno} não encontrado na tabela.")

root = tk.Tk()
root.title("Alunos")
root.geometry("300x300")

prof_button = tk.Button(root, text="Professor", command=autenticacao, width=16, height=1)
prof_button.pack()

alunos_button = tk.Button(root, text="Aluno", command=aluno, width=16, height=1)
alunos_button.pack()

resultado = []

root.mainloop()