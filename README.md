# livelo test:
Teste da funcionalidade adicionar produto ao carrinho

# observações:
É sempre bom ter o node.js e java instaldo na maquina para poder rodas todas as dependências  
node:  https://nodejs.org/pt-br/download/   
java:  https://www.java.com/pt-BR/download/ie_manual.jsp?locale=pt_BR

# Como Rodar:

Caso você não use o Pycharm que faz toda a mágica,(mas eu ja vou enviar com o venv(ambiente virtual)),
você deverá executar os seguintes comandos caso as dependencias não sejam instaladas:

pip install requirements.txt

Após as dependencias serem instaladas:

behave --tags=@add -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features

Isso irá gerar uma pasta com reports (relatórios de testes que executamos)

Após gerar a pasta, para ver os resultados: 

allure serve %allure_result_folder%

e será apresentado um link no terminal que você deve clicar para ir ao relatório.


