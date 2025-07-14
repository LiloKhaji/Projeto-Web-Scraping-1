import math
import time
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuração do driver
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Acessa a página inicial
url_base = 'https://www.kabum.com.br/hardware/placa-de-video-vga/placa-de-video-nvidia'
driver.get(url_base)

# Espera o elemento do site aparecer
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'productCard')))

# Extrai o número total de produtos
qtd_texto = driver.find_element(By.ID, 'listingCount').text.strip()
qtd = int(qtd_texto.split()[0])
ultima_pagina = math.ceil(qtd / 20)

# Lista para armazenar os resultados
produtos_lista = {'nome': [], 'preço': []}

# Loop por página
for pagina in range(1, ultima_pagina + 1):
    print(f'Página {pagina}')
    url_pag = f'{url_base}?page_number={pagina}&page_size=20&facet_filters=&sort=most_searched'
    driver.get(url_pag)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'productCard')))

    produtos = driver.find_elements(By.CLASS_NAME, 'productCard')

    for produto in produtos:
        try:
            nome = produto.find_element(By.CLASS_NAME, 'nameCard').text.strip()
            preco = produto.find_element(By.CLASS_NAME, 'priceCard').text.strip()

            produtos_lista['nome'].append(nome)
            produtos_lista['preço'].append(preco)

        except Exception as e:
            print(f"Erro ao capturar produto: {e}")
            continue

# Fecha o navegador
driver.quit()

# Criando local final do arquivo
pasta_documentos = os.path.join(os.path.expanduser("~"), "Documents", "Projeto Web Scraping")
os.makedirs(pasta_documentos, exist_ok=True)
caminho_txt = os.path.join(pasta_documentos, "preco_GPU_nvidea.txt")

df = pd.DataFrame(produtos_lista)
with open(caminho_txt, 'w', encoding='utf-8') as f:
    for _, row in df.iterrows():
        nome = row['nome']
        preco = row['preço']

        if len(nome) > 80:
            nome = nome[:77] + '...'

        f.write(f"{nome:<80} {preco:>12}\n")

print(f"{len(produtos_lista['nome'])} produtos salvos em:\n{caminho_txt}")

