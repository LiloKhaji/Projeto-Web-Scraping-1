# Projeto-Web-Scraping-1

Meu desafio foi criar um web scraping que colete dados de algum site público (notícias, clima, e-commerce etc.) e colocar os dados em um arquivo com formato .txt, escolhi o site da kabum mais especificamente na categoria das Gpu's Nvidea.
O codigo tem função automatica de reconhecer quantas paginas de produtos tem no site, usei uma logica simples de ver quantos produtos tem no site e dividi por quantos produtos fica em exibição por pagina.
o codigo passa de pagina em pagina pegando os dados de nome da GPU, preço e organiza ao lado do nome seu valor em um arquivo .txt, o codigo tem como função colocar o arquivo .txt como padrão na pasta "documentos/Projeto Web Scraping" do computador do usuario.

Requerimentos:
Python / Pandas / Selenium
