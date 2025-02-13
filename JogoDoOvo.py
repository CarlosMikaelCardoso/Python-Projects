import tkinter as tk

class JogoDoOvo:
    def __init__(self):
        self.cont = 0
        self.morte = {
            1.1: "Você passou fome!",
            1.3: "Não deu conta de tantos ovos!",
            1.4: "Você foi guloso, deixou sua família desejando seus ovos",
            2.1: "Perdeu! Meu mano(a) você não é o Jacan!",
            2.2: "Putz! O último ovo estava podre!",
            2.4: "Espirrou ovo para todos os lados, sua mãe vai te matar!",
        }
        self.root()

    def root(self):
        self.main = tk.Tk()
        self.main.title("Jogo do Ovo")
        self.main.geometry("200x100")
        self.main.resizable(False, False)
        
        botao_start = tk.Button(self.main, text="Start", command=self.start, width=10)    
        botao_start.pack()

        self.main.mainloop()

    def start(self):
        self.cont += 1
        self.primeira = tk.Tk()
        self.primeira.title("1 questão")
        self.primeira.geometry("300x200")
        
        label = tk.Label(self.primeira, text="Quantos ovos você quer comer?")
        label.pack()
        
        self.create_button(self.primeira, "1", lambda: self.erro(1.1))
        self.create_button(self.primeira, "2", self.dois)
        self.create_button(self.primeira, "4", lambda: self.erro(1.3))
        self.create_button(self.primeira, "7", lambda: self.erro(1.4))
        
        self.main.destroy()

    def dois(self):
        self.cont += 1
        self.primeira.destroy()
        
        self.segunda = tk.Tk()
        self.segunda.title("2 questão")
        self.segunda.geometry("300x200")
        
        label = tk.Label(self.segunda, text="Como você quebra os ovos?")
        label.pack()
        
        self.create_button(self.segunda, "Estilo Masterchef", lambda: self.erro(2.1))
        self.create_button(self.segunda, "Com uma colher", lambda: self.erro(2.2))
        self.create_button(self.segunda, "De maneira segura", self.tres)
        self.create_button(self.segunda, "Com as moes", lambda: self.erro(2.4))

    def tres(self):
            self.cont += 1
            self.segunda.destroy()
            
            self.terceira = tk.Tk()
            self.terceira.title("3 questão")
            self.terceira.geometry("300x200")
            
            label = tk.Label(self.terceira, text="Como você quebra os ovos?")
            label.pack()
            
            self.create_button(self.terceira, "Estilo Mastechef", lambda: self.erro(1.1))
            self.create_button(self.terceira, "De maneira segura", self.dois)
            self.create_button(self.terceira, "Com uma colher", lambda: self.erro(1.3))
            self.create_button(self.terceira, "Com as moes", lambda: self.erro(1.4))
            
            
    def create_button(self, parent, text, command):
        button = tk.Button(parent, text=text, command=command, width=20)
        button.pack()
        
    def erro(self, code):
        print(self.morte[code])

if __name__ == "__main__":
    JogoDoOvo()