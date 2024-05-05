def formatar_arquivo_entrada(arquivo_entrada):
    linhas_formatadas = []
    with open(arquivo_entrada, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        for i, linha in enumerate(linhas):
            if i < len(linhas) - 1:
                linhas_formatadas.append(f'"{linha.strip()}",')
            else:
                linhas_formatadas.append(f'"{linha.strip()}"')
    return linhas_formatadas

def salvar_arquivo_saida(linhas_formatadas, arquivo_saida):
    with open(arquivo_saida, 'w', encoding='utf-8') as arquivo:
        arquivo.write('\n'.join(linhas_formatadas))

def formatar_arquivo_texto(arquivo_entrada, arquivo_saida):
    linhas_formatadas = formatar_arquivo_entrada(arquivo_entrada)
    salvar_arquivo_saida(linhas_formatadas, arquivo_saida)
    print(f'Arquivo formatado salvo em "{arquivo_saida}".')

# Teste
arquivo_entrada = 'links_extraidos.txt'
arquivo_saida = 'arquivo_formatado.txt'
formatar_arquivo_texto(arquivo_entrada, arquivo_saida)
