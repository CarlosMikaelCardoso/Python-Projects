import tkinter as tk

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
    botao_janela.pack_forget()
    botao_adicionar.pack()


def adicionar_aluno():    
    global qalunos
    aluno = entrada_aluno.get()
    nota = entrada_nota.get()

    resultado.append(f"Aluno: {aluno} - Nota: {nota}")
    resultado.sort()

    entrada_aluno.delete(0, 'end')
    entrada_nota.delete(0, 'end')

    if qalunos > 0:
        qalunos -= 1
        alunos_label.config(text=f"Inserindo informações para {qalunos} alunos")

    if qalunos == 0:
        with open('arquivo.txt', 'w') as f:
            f.write('\n'.join(resultado))
        
        with open('arquivo.txt', 'r') as f:
            conteudo = f.read()
            result.config(text=conteudo)
            
            nome_alunos.pack_forget()
            nome_nota.pack_forget()
            entrada_nota.pack_forget()
            entrada_aluno.pack_forget()
            botao_janela.pack()
            botao_adicionar.pack_forget()

root = tk.Tk()
root.title("Alunos")
root.geometry("300x300")

alunos_label = tk.Label(root, text='')
alunos_label.pack()

nome_alunos = tk.Label(text='Aluno')
entrada_aluno = tk.Entry(root)
nome_nota = tk.Label(text='Nota')
entrada_nota = tk.Entry(root)

resultado = []

botao_adicionar = tk.Button(root, text="=", command=adicionar_aluno, width=16, height=1)

botao_janela = tk.Button(root, text="Iniciar", command=chama, width=16, height=1)
botao_janela.pack()

result = tk.Label(root, text='')
result.pack()

root.mainloop()
