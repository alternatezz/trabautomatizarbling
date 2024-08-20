import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui
import random

# Caminho para o seu chromedriver.exe
caminho_chromedriver = 'C:/Users/MEUCOMPUTADOR/Documents/GitHub/trabautomatizarbling/chromedriver.exe'

# Configurações do navegador
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
servico = Service(caminho_chromedriver)
navegador = webdriver.Chrome(service=servico, options=chrome_options)

# Abrir a página
navegador.get("https://www.shopee.com.br/")
'''navegador.maximize_window()
pyautogui.moveTo(1238, 168, duration=0.5)'''

# Aguardar o botão de login aparecer
popup = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div/div[2]/div/div[2]/form/div[1]/div[1]/input')))

# Preencher informações de login e fazer login
navegador.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div/div[2]/div/div[2]/form/div[1]/div[1]/input').send_keys("vinimlima@gmail.com")
navegador.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div/div[2]/div/div[2]/form/div[2]/div[1]/input').send_keys("Vi37825337!")
navegador.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div/div[2]/div/div[2]/form/button').click()
fecharmensagem = WebDriverWait(navegador, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="step-0"]/button')))
navegador.find_element(By.XPATH, '//*[@id="step-0"]/button').click()

'''# Navegar até o local desejado
navegador.find_element(By.XPATH, '//*[@id="menu-novo"]/ul[1]/li[4]/a').click()
navegador.find_element(By.XPATH, '//*[@id="menu-novo"]/ul[1]/li[4]/ul/li[8]/a').click()

# Ajustar o zoom
navegador.execute_script("document.body.style.zoom='33%'")
time.sleep(10)

# Loop para clicar em cada elemento com a classe 'visible-xs.table-label'
elementos = navegador.find_elements(By.CLASS_NAME, 'visible-xs.table-label')
for elemento in elementos:
    # Clicar no elemento
    elemento.click()
    time.sleep(2)  # Aguardar um pouco

    # Localizar e manipular elementos
    try:
        # Aguardar até que o elemento "valorProdutos" seja visível
        valor_produtos = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.ID, 'valorProdutos')))

        # Obter o valor do atributo "value" do elemento
        texto_valor_produtos = valor_produtos.get_attribute("value")

        # Verificar se o texto não está vazio
        if texto_valor_produtos.strip():
            # Converter o texto para um valor float
            var1 = float(texto_valor_produtos.strip().replace(',', '.'))
            print("Valor de produtos como float:", var1)

            # Gerar um valor aleatório entre 1 e 1,15
            diff = round(random.uniform(1, 1.15), 2)

            # Calcular var2 tal que var1 - var2 seja igual ao valor aleatório gerado acima
            var2 = round(var1 - diff, 2)
            print("Var2:", var2)

            # Enviar var2 como uma string contendo apenas números com duas casas decimais para o elemento //*[@id="desconto"]
            xpath_desconto = '//*[@id="desconto"]'
            elemento_desconto = navegador.find_element(By.XPATH, xpath_desconto)
            elemento_desconto.send_keys(Keys.CONTROL + "a")  # Selecionar todo o texto no elemento
            elemento_desconto.send_keys("{:.2f}".format(var2).replace('.', ','))  # Substituir o valor selecionado

            time.sleep(2)

            # Clique no campo frete para selecionar todo o texto
            elemento_frete = navegador.find_element(By.XPATH, '//*[@id="frete"]')
            elemento_frete.send_keys(Keys.CONTROL + "a")  # Selecionar todo o texto
            elemento_frete.send_keys("0")  # Inserir o valor 0 no campo frete

            time.sleep(2)

            # Clique no botão "Salvar"
            navegador.execute_script("arguments[0].click();", navegador.find_element(By.XPATH, '//*[@id="botaoSalvar"]'))

            # Aumentar o valor de Y em 10
            # y += 13
        else:
            print("O elemento valorProdutos está vazio.")

    except Exception as e:
        print("Ocorreu um erro:", e)
        # Aumentando o valor de Y em 10
        # y += 13
'''