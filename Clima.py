import requests
import json
import tkinter as tk
import datetime

def erro(site):
    if site['cod'] == '404':
        return True
    else:
        return False
    
def detalhes(site):
    # Definição das informações
    Longitude = site['coord']['lon']
    Latitude = site['coord']['lat']
    Temperatura = site['main']['temp']
    sensacaoTermica = site['main']['feels_like']
    Umidade = site['main']['humidity']
    maxima = site['main']['temp_max']
    pais = site['sys']['country']
    sunrise = site['sys']['sunrise']
    sunset = site['sys']['sunset']
    ticks = sunrise
    tecks = sunset
    horario = datetime.datetime.utcfromtimestamp(ticks)
    hora = datetime.datetime.utcfromtimestamp(tecks)
    horario_formatado = horario.strftime('%H:%M:%S')
    hora_formatado = hora.strftime('%H:%M:%S')
    
    # Monta as informações em uma string
    info = ""
    info += "Pais: " + str(pais) + "\n"
    info += "Nascer do sol: " + str(horario_formatado) + "\n"
    info += "Por do sol: " + str(hora_formatado) + "\n"
    info += "Longitude: " + str(Longitude) + "\n"
    info += "Latitude: " + str(Latitude) + "\n"
    info += "Temperatura atual: " + str(Temperatura) + " Celcius\n"
    info += "Sensacao termica: " + str(sensacaoTermica) + " Celcius\n"
    info += "Umidade: " + str(Umidade) + "%\n"
    info += "Temperatura Maxima: " + str(maxima) + " Celcius\n"
    
    return info

def requisicao():
    try:
        city = entrada_cidade.get()  # Obtém o nome da cidade inserido pelo usuário
        req = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+ city +'&units=metric&appid=28aec1fc0b8871a47406b017e63d40a2')  
        site = req.json()  # Não é necessário usar json.loads, pois requests.get já retorna um JSON
        info = detalhes(site)  # Chama a função detalhes para formatar as informações
        resultado_api_text.delete(1.0, tk.END)  # Limpa o conteúdo anterior do widget de texto
        resultado_api_text.insert(tk.END, info)  # Insere as informações formatadas no widget de texto
    except Exception as e:
        resultado_api_text.delete(1.0, tk.END)
        resultado_api_text.insert(tk.END, "Erro ao chamar a API: " + str(e))

# Criar a janela
root = tk.Tk()
root.title("Clima")
root.resizable(False,False)

# Caixa de entrada para o nome da cidade
entrada_cidade = tk.Entry(root)
entrada_cidade.pack()

# Botão para chamar a API
botao_chama_api= tk.Button(root,text="Clima",command=requisicao)
botao_chama_api.pack()

# Widget de texto para exibir o resultado da API
resultado_api_text = tk.Text(root, height=10, width=50)
resultado_api_text.pack()

root.mainloop()
