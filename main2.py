from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)

#Abrir na pagina
navegador.get("https://www.bling.com.br/")
popup = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="dropdown-login"]')))


#Pegar Info
navegador.find_element('xpath', '//*[@id="username"]').send_keys("mixetoy")
navegador.find_element('xpath', '//*[@id="senha"]').send_keys("748649Cv@")
navegador.find_element('xpath', '//*[@id="login-buttons"]/button').click()
fecharmensagem = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="step-0"]/button')))


navegador.find_element('xpath', '//*[@id="step-0"]/button').click()
navegador.find_element('xpath', '//*[@id="menu-novo"]/ul[1]/li[4]/a').click()
navegador.find_element('xpath', '//*[@id="menu-novo"]/ul[1]/li[4]/ul/li[8]/a').click()


