# Bem vindo desenvolvedor(a),

### Linguaguem de programação : 
    Python

### Projeto, coleta de dados em python; 

    Usaremos um site de vagas de emprego como exemplo para realiza uma varredura,
    Coletando informações, exemplo:
    Nome da vaga, cidade, data, link da vaga, email do(a) recrutador(a) 💥

### Guia para executar corretamente
    Passo 1, Primeiro Script MainMenu.py : 
    
    baixe os scripts acima.
    com o visual studio aberto ou um terminal, execute o script : MenuMain.py
    em seguida irá abrir um menu 
  
    1. Extrair dados das vagas
    2. Baixar dados formatados das vagas em um arquivo
    3. Sair do programa
    
    selecione a primeira opção, assim fazendo a varredura no site.
    depois que ele extrair todas informações que você requisitou do site,
    ele pedira que você defina um nome para o .txt, por obrigação voce terá que colocar
    arquivo.txt, assim finalizando o processo do primeiro script.

    Passo 2, Segundo Script ExtrairURLS.py : 

    aqui vamos fazer a formatação destes dados coletados
    e selecionar somente as url's que coletamos com o MainMenu.py,
    execute o script : ExtrairURLS.py depois de executado ele cria um arquivo chamado links_extraidos.txt
    não o renomeie.

    Passo 3, Terceiro Script FormatarURLS.py : 

    neste passo iremos formatar os links que extraimos com o ExtrairURLS.py,
    formatando eles para a execução deles no próximo script.
    execute o script : FormatarURLS.py depois de executado ele cria um arquivo chamado arquivo_formatado.txt.

    Passo 4, Quarto Script ColetorDeEmail.py : 

    neste ultimo passo iremos obter os emails dos recrutadores, com os links que formatamos acima.
    porem antes de executar o script... acesse o arquivo_formatado.txt e copie todos os links.
    com o script ColetorDeEmail.py aberto, vá até : # Lista de URLs para coletar e-mails
    urls = [ 
       ### aqui vai as url's exemplo : 
       "https://www.itajaionline.com.br/vaga/134712-gerente-de-loja",
       "https://www.itajaionline.com.br/vaga/134712-gerente-de-loja"
    ]
    certifique que o ultimo link esteja sem ( ,  virgula)
    agora que você já colocou os links, basta executar o coletor 
    e salvar os emails... 
    
### Printscreen's : 


<p float="left">
  
 <img src="https://raw.githubusercontent.com/Hufner-1/FutureTEC.py/main/menu.png" width="900" />

 <img src="https://raw.githubusercontent.com/Hufner-1/FutureTEC.py/main/ExtrairURL.png" width="900" />
 
 <img src="https://raw.githubusercontent.com/Hufner-1/FutureTEC.py/main/formatadorURL.png" width="900" />
  
 <img src="https://raw.githubusercontent.com/Hufner-1/FutureTEC.py/main/EMAILFINAL.png" width="900" />

</p>
