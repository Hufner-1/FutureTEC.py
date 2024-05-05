import requests
from bs4 import BeautifulSoup

def exibir_menu():
    print("Menu:")
    print("1. Extrair dados das vagas")
    print("2. Baixar dados formatados das vagas em um arquivo")
    print("3. Sair do programa")

def extrair_dados(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        vagas_destaque = soup.find_all('div', class_='col m6 s6 green lighten-5 boxVagas')
        vagas_outros = soup.find_all('div', class_='col m6 s6 grey lighten-5 boxVagas')
        dados = []
        
        for vaga in vagas_destaque:
            nome_vaga = vaga.find('h3').text.strip()
            cidade = vaga.find('p', class_='cidade').text.strip()
            data = vaga.find('div', class_='col m3 s12 right-align').text.strip()
            link = vaga.find('a')['href']
            dados.append((nome_vaga, cidade, data, link))
        
        for vaga in vagas_outros:
            nome_vaga = vaga.find('h3').text.strip()
            cidade = vaga.find('p', class_='cidade').text.strip()
            data = vaga.find('div', class_='col m3 s12 right-align').text.strip()
            link = vaga.find('a')['href']
            dados.append((nome_vaga, cidade, data, link))
        
        return dados
    else:
        print("Falha ao acessar a página:", response.status_code)
        return []

def salvar_dados_formatados(dados, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for vaga in dados:
            arquivo.write(f"Nome da vaga: {vaga[0]}\n")
            arquivo.write(f"Cidade: {vaga[1]}\n")
            arquivo.write(f"Data: {vaga[2]}\n")
            arquivo.write(f"Link: {vaga[3]}\n\n")

def main():
    urls = [
        "https://www.itajaionline.com.br/vagas",
        "https://www.itajaionline.com.br/vagas/parte-2",
        "https://www.itajaionline.com.br/vagas/parte-3",
        "https://www.itajaionline.com.br/vagas/parte-4",
        "https://www.itajaionline.com.br/vagas/parte-5",
        "https://www.itajaionline.com.br/vagas/parte-6",
        "https://www.itajaionline.com.br/vagas/parte-7",
        "https://www.itajaionline.com.br/vagas/parte-8",
        "https://www.itajaionline.com.br/vagas/parte-9"
    ]
    
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print("Extraindo dados das vagas...\n")
            dados_completos = []
            for url in urls:
                dados = extrair_dados(url)
                if dados:
                    dados_completos.extend(dados)
            if dados_completos:
                for idx, vaga in enumerate(dados_completos, start=1):
                    print(f"Vaga {idx}:")
                    print(f"Nome da vaga: {vaga[0]}")
                    print(f"Cidade: {vaga[1]}")
                    print(f"Data: {vaga[2]}")
                    print(f"Link: {vaga[3]}\n")
            else:
                print("Nenhum dado encontrado.")
        
        elif escolha == "2":
            print("Salvando dados formatados das vagas em um arquivo...\n")
            dados_completos = []
            for url in urls:
                dados = extrair_dados(url)
                if dados:
                    dados_completos.extend(dados)
            if dados_completos:
                nome_arquivo = input("Digite o nome do arquivo para salvar (com a extensão .txt): ")
                salvar_dados_formatados(dados_completos, nome_arquivo)
                print(f"Dados das vagas salvos em '{nome_arquivo}'\n")
            else:
                print("Nenhum dado encontrado.")
        
        elif escolha == "3":
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida. Por favor, escolha novamente.\n")

if __name__ == "__main__":
    main()
