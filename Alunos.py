import tkinter as tk

def configurar_qtd_alunos():
    global qalunos
    qalunos = int(entry_qtd_alunos.get())
    alunos_label.config(text=f"Inserindo informações para {qalunos} alunos")

def adicionar_aluno():
    global qalunos
    qalunos -= 1
    alunos_label.config(text=f"Inserindo informações para {qalunos} alunos")

    aluno = entrada_aluno.get()
    nota = entrada_nota.get()

    resultado.append(f"Aluno: {aluno} - Nota: {nota}")

    entrada_aluno.delete(0, 'end')
    entrada_nota.delete(0, 'end')

    if qalunos == 0:
        with open('arquivo.txt', 'w') as f:
            f.write('\n'.join(resultado))
        
        with open('arquivo.txt', 'r') as f:
            conteudo = f.read()
            result.config(text=conteudo)
    else:
        alunos_label.config(text=f"Inserindo informações para {qalunos} alunos")

root = tk.Tk()
root.title("Alunos")

entry_qtd_alunos = tk.Entry(root)
entry_qtd_alunos.pack()

botao_configurar_qtd_alunos = tk.Button(root, text="Configurar Quantidade de Alunos", command=configurar_qtd_alunos)
botao_configurar_qtd_alunos.pack()

alunos_label = tk.Label(root, text='')
alunos_label.pack()

entrada_aluno = tk.Entry(root)
entrada_aluno.pack()

entrada_nota = tk.Entry(root)
entrada_nota.pack()

resultado = []

botao_adicionar = tk.Button(root, text="+", command=adicionar_aluno)
botao_adicionar.pack()

result = tk.Label(root, text='')
result.pack()

root.mainloop()
