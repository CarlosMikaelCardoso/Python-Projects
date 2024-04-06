import tkinter as tk
idd = 0

def aluno():
    global aluno_result,alunos
    alunos = tk.Tk()
    alunos.title("Alunos")
    id_label = tk.Label(text="ID")
    id_label.pack()
    id_buscado = tk.Entry(alunos)
    id_buscado.pack()
    nome_label = tk.Label(text="Nome")
    nome_label.pack()
    nome_buscado = tk.Entry(alunos)
    nome_buscado.pack()
    
    def busca():
        id_aluno = id_buscado.get()  # Obter o texto da entrada do ID
        nome_aluno = nome_buscado.get()  # Obter o texto da entrada do nome
        procurar_aluno(id_aluno=id_aluno, nome_aluno=nome_aluno)  # Passar os textos para a função de busca
        
    busca_button = tk.Button(alunos, text="Buscar", command=busca, width=16, height=1)  
    busca_button.pack()
    
    voltar = tk.Button(alunos, text="Voltar", command=inicio2, width=16, height=1)
    voltar.pack()
    
    aluno_result = tk.Label(alunos,text='')

def inicio():
    professor.withdraw()
    root.deiconify()
    
def inicio2():
    alunos.withdraw()
    root.deiconify()

def janela_professor():
    global botao_janela,professor,botao_adicionar,nome_alunos,entrada_aluno,nome_nota,entrada_nota,alunos_label
    professor = tk.Toplevel()
    professor.title("Professor")
    professor.geometry("250x300")
    botao_janela = tk.Button(professor, text="Adicionar", command=chama, width=16, height=1)
    botao_janela.pack()
    botao_adicionar = tk.Button(professor, text="=", command=adicionar_aluno, width=16, height=1)
    nota_button = tk.Button(professor, text="Checar", command=notas, width=16, height=1)
    nota_button.pack()
    alunos_label = tk.Label(professor, text='')
    alunos_label.pack()
    voltar = tk.Button(professor, text="Voltar", command=inicio, width=16, height=1)
    voltar.pack()

    nome_alunos = tk.Label(professor,text='Aluno')
    entrada_aluno = tk.Entry(professor)
    nome_nota = tk.Label(professor,text='Nota')
    entrada_nota = tk.Entry(professor)
    
def verificacao():
    user1 = user_entry.get()
    senha1 = senha_entry.get()
    if user1 == user and senha1 == senha:
        autenticar.withdraw()
        janela_professor()
    else:
        print("error")

def autenticacao():
    global autenticar, user, senha,user_entry,senha_entry
    root.withdraw()
    autenticar = tk.Tk()
    autenticar.title("Login")
    autenticar.geometry("225x110")
    user_label = tk.Label(autenticar, text="Usúario")
    senha_label = tk.Label(autenticar, text="Senha")
    user_entry = tk.Entry(autenticar)
    senha_entry = tk.Entry(autenticar, show="*")  # To hide the password
    user_label.pack()
    user_entry.pack()
    senha_label.pack()
    senha_entry.pack()
    user = "Prof"
    senha = "0101"
    verificar_button = tk.Button(autenticar, text="Enter", command=verificacao)
    verificar_button.pack()

def configurar_qtd_alunos():
    global qalunos, entry_qtd_alunos
    qalunos = int(entry_qtd_alunos.get())
    alunos_label.config(text=f"Inserindo informações para {qalunos} alunos")
    entry_qtd_alunos.delete(0, 'end')
    janela.destroy()
    
def chama():
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
    global qalunos,idd
    idd += 1
    aluno = entrada_aluno.get()
    nota = entrada_nota.get()

    resultado.append(f"ID: {idd}|Aluno: {aluno}| Nota: {nota}|")
    resultado.sort()

    entrada_aluno.delete(0, 'end')
    entrada_nota.delete(0, 'end')

    if qalunos > 0:
        qalunos -= 1
        alunos_label.config(text=f"Inserindo informações para {qalunos} alunos")

    if qalunos == 0:
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
    global result
    nota = tk.Tk()
    nota.title("Notas")
    result = tk.Label(nota, text='')
    result.pack()
    
    with open('arquivo.txt', 'r') as f:
        conteudo = f.read()
        result.config(text=conteudo)

    
def procurar_aluno(id_aluno=None, nome_aluno=None):
    if id_aluno is None and nome_aluno is None:
        print("É necessário fornecer pelo menos o ID ou o nome do aluno para procurar.")
        return
    
    with open('arquivo.txt', 'r') as f:
        for linha in f:
            if id_aluno is not None and f"ID: {id_aluno}" in linha:
                aluno_result.config(text=linha)
                aluno_result.pack()
                return
            elif nome_aluno is not None and f"Aluno: {nome_aluno}" in linha:
                aluno_result.config(text=linha)
                aluno_result.pack()
                return
    aluno_result.config(text=f"Aluno com ID '{id_aluno}' ou nome '{nome_aluno}' não encontrado.")
       
root = tk.Tk()
root.title("Alunos")
root.geometry("300x300")

prof_button = tk.Button(root, text="Professor", command=autenticacao, width=16, height=1)
prof_button.pack()

alunos_button = tk.Button(root, text="Aluno", command=aluno, width=16, height=1)
alunos_button.pack()
resultado = []

root.mainloop()