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

# abrir na pagina
navegador.get("https://www.bling.com.br/")
navegador.maximize_window()
time.sleep(2)
pyautogui.moveTo(1238, 168, duration=0.5)
popup = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="dropdown-login"]')))

# tela de login
navegador.find_element(By.XPATH, '//*[@id="username"]').send_keys("usuario") # login
navegador.find_element(By.XPATH, '//*[@id="senha"]').send_keys("senha") #senha
navegador.find_element(By.XPATH, '//*[@id="login-buttons"]/button').click()
fecharmensagem = WebDriverWait(navegador, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="step-0"]/button')))
# entrar na tela de NF
navegador.find_element(By.XPATH, '//*[@id="step-0"]/button').click()
navegador.find_element(By.XPATH, '//*[@id="menu-novo"]/ul[1]/li[4]/a').click()
navegador.find_element(By.XPATH, '//*[@id="menu-novo"]/ul[1]/li[4]/ul/li[8]/a').click()

# zoom da pagina em 33%
navegador.execute_script("document.body.style.zoom='33%'")
time.sleep(15)

# coordenadas iniciais
x = 350
y = 213

# looping quantidade de NF
for _ in range(30):
    # coordenadas iniciais
    #x = 350
    #y = 212
    pyautogui.scroll(10)

    # mover o mouse para as posiçoes x e y
    pyautogui.moveTo(x, y, duration=0.5)
    pyautogui.click()
    time.sleep(2)

    try:
        # espera ate que o elemento apareça
        valor_produtos = WebDriverWait(navegador, 5).until(EC.visibility_of_element_located((By.ID, 'valorProdutos')))

        # reconhece o valor do atributo "value" do elemento
        texto_valor_produtos = valor_produtos.get_attribute("value")

        # da um check pra ver se nao esta vazio
        if texto_valor_produtos.strip():
            # converte string pra float 
            var1 = float(texto_valor_produtos.strip().replace(',', '.'))
            print("Valor de produtos como float:", var1)

            # gera um valor aleatório entre 1 e 1,15
            diff = round(random.uniform(1, 1.15), 2)

            # calcula o valor da diferenca
            var2 = round(var1 - diff, 2)
            print(var2)
            # envia var2 como string para o elemento 
            xpath_desconto = '//*[@id="desconto"]'
            elemento_desconto = navegador.find_element(By.XPATH, xpath_desconto)
            # da ctrl+a no elemento
            elemento_desconto.send_keys(Keys.CONTROL + "a")
            # substitui pelo var2
            elemento_desconto.send_keys("{:.2f}".format(var2).replace('.', ','))
            time.sleep(1)
            # da ctrl+a no frete
            elemento_frete = navegador.find_element(By.XPATH, '//*[@id="frete"]')
            elemento_frete.send_keys(Keys.CONTROL + "a")
            # coloca valor 0 no frete
            elemento_frete.send_keys("0")
            time.sleep(1)
            # salva
            navegador.execute_script("arguments[0].click();", navegador.find_element(By.XPATH, '//*[@id="botaoSalvar"]'))
            time.sleep(2)

        else:
            print("deu merda")

    except Exception as e:
        print("deu merda", e)

    # aumentando o valor de Y em 13
    y += 14
    print("Valor de Y atualizado:", y)
    # move o mouse para as novas coordenadas
    pyautogui.moveTo(x, y, duration=0.5)  