import re

def extrair_links(arquivo_entrada, arquivo_saida):
    # Lista para armazenar os links encontrados
    links = []

    # Expressão regular para encontrar links
    regex = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

    # Abre o arquivo de entrada
    with open(arquivo_entrada, 'r', encoding='utf-8') as file:
        # Lê o conteúdo do arquivo
        conteudo = file.read()

        # Encontra todos os links no conteúdo usando a expressão regular
        links = re.findall(regex, conteudo)

    # Abre o arquivo de saída para escrever os links
    with open(arquivo_saida, 'w', encoding='utf-8') as file:
        # Escreve os links no arquivo de saída
        for link in links:
            file.write(link + '\n')

    print(f"Links extraídos do arquivo '{arquivo_entrada}' e salvos em '{arquivo_saida}'.")

# Teste da função com um arquivo de exemplo
if __name__ == "__main__":
    arquivo_entrada = 'arquivo.txt'
    arquivo_saida = 'links_extraidos.txt'
    extrair_links(arquivo_entrada, arquivo_saida)
