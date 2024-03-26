import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui
import random


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)

# Abrir na pagina
navegador.get("https://www.bling.com.br/")
popup = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="dropdown-login"]')))

# Pegar Info
navegador.find_element(By.XPATH, '//*[@id="username"]').send_keys("mixetoy")
navegador.find_element(By.XPATH, '//*[@id="senha"]').send_keys("748649Cv@")
navegador.find_element(By.XPATH, '//*[@id="login-buttons"]/button').click()
fecharmensagem = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="step-0"]/button')))

navegador.find_element(By.XPATH, '//*[@id="step-0"]/button').click()
navegador.find_element(By.XPATH, '//*[@id="menu-novo"]/ul[1]/li[4]/a').click()
navegador.find_element(By.XPATH, '//*[@id="menu-novo"]/ul[1]/li[4]/ul/li[8]/a').click()

# Ajustar o zoom para 33%
navegador.execute_script("document.body.style.zoom='33%'")

# Esperar 10 segundos
time.sleep(10)

# Coordenadas iniciais
x = 350
y = 208

# Loop para executar o código PyAutoGUI 40 vezes
for _ in range(1):
    # Movendo o mouse para as coordenadas especificadas
    pyautogui.moveTo(x, y, duration=0.5)
    # Efetuando um clique
    pyautogui.click()
    # Localize o elemento do valor de produtos

time.sleep(10)
# Execute um script JavaScript para obter o texto do elemento
navegador.maximize_window()



try:
    # Aguarde até que o elemento "valorProdutos" seja visível
    valor_produtos = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.ID, 'valorProdutos')))

    # Obtenha o valor do atributo "value" do elemento
    texto_valor_produtos = valor_produtos.get_attribute("value")

    # Verifique se o texto não está vazio
    if texto_valor_produtos.strip():
        # Converta o texto para um valor float
        var1 = float(texto_valor_produtos.strip().replace(',', '.'))
        print("Valor de produtos como float:", var1)

        # Gere um valor aleatório entre 1 e 1,15
        diff = round(random.uniform(1, 1.15), 2)

        # Calcule var2 tal que var1 - var2 seja igual ao valor aleatório gerado acima
        var2 = round(var1 - diff, 2)
        print(var2)
        # Enviar var2 como uma string contendo apenas números com duas casas decimais para o elemento //*[@id="desconto"]
        xpath_desconto = '//*[@id="desconto"]'
        elemento_desconto = navegador.find_element(By.XPATH, xpath_desconto)
        # Selecionar todo o texto no elemento
        elemento_desconto.send_keys(Keys.CONTROL + "a")
        # Substituir o valor selecionado pelo novo valor
        elemento_desconto.send_keys("{:.2f}".format(var2).replace('.', ','))

    else:
        print("O elemento valorProdutos está vazio.")

except Exception as e:
    print("Ocorreu um erro:", e)
    # Aumentando o valor de Y em 10
    #y += 13
