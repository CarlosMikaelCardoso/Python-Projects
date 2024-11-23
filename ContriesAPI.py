import requests

def detalhes(site):
    # Extrai detalhes do primeiro país na resposta
    pais = site[0]['name']['common']
    capital = site[0].get('capital', ['N/A'])[0]  # Retorna 'N/A' se não houver capital
    populacao = site[0].get('population', 'Desconhecida')
    area = site[0].get('area', 'Desconhecida')
    regiao = site[0].get('region', 'Desconhecida')

    # Monta as informações em uma string
    info = ""
    info += "País: " + pais + "\n"
    info += "Capital: " + capital + "\n"
    info += "População: " + str(populacao) + "\n"
    info += "Área: " + str(area) + " km²\n"
    info += "Regiao: " + str(regiao) + "\n"
    
    return info

def requisicao():
    try:
        # Solicita o nome do país ao usuário
        city = input("Nome do país? ")
        req = requests.get(f'https://restcountries.com/v3.1/name/{city}')
        
        if req.status_code == 200:
            site = req.json()
            info = detalhes(site)
            print(info)
        else:
            print(f"Erro ao buscar dados: {req.status_code}")
    except Exception as e:
        print("Erro ao chamar a API: " + str(e))

# Teste simples
requisicao()
