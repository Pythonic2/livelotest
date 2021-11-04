# language: pt

Funcionalidade: adicionar um produto ao carrinho
  
  # Contexto são ações que serão executadas antes de cada cenário.
  Contexto: acessar página de teste
    Dado que acesso a página da lilevo

  Cenário: acessar página da lilevo e adicionar produto ao carrinho
    Dado que preencho o campo de pesquisa com Berço
    E escolho um produto e clico nele
    E clico no botão adicionar ao carrinho
    Quando clico no botao não quero o desconto
    Então devo visualizar o produto no carrinho