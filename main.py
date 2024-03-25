from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains



chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)
#session_id = "1758eac58d2c8e1bce0be08152beb6f3"
#navegador = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities={})
#navegador.session_id = session_id


#Abrir na pagina
navegador.get("https://www.bling.com.br/")
popup = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="dropdown-login"]')))

#session_id = navegador.session_id
#print("ID da sessão:", session_id)
element = navegador.find_element(By.XPATH, '//*[@id="dropdown"]/a')
ActionChains(navegador).move_to_element(element).perform()

#Pegar Info
navegador.find_element('xpath', '//*[@id="username"]').send_keys("mixetoy")
navegador.find_element('xpath', '//*[@id="senha"]').send_keys("748649Cv@")
navegador.find_element('xpath', '//*[@id="login-buttons"]/button').click()
fecharmensagem = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="step-0"]/button')))

navegador.find_element('xpath', '//*[@id="step-0"]/button').click()
navegador.find_element('xpath', '//*[@id="menu-novo"]/ul[1]/li[4]/a').click()
navegador.find_element('xpath', '//*[@id="menu-novo"]/ul[1]/li[4]/ul/li[8]/a').click()
fecharmensagem = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="19983412743"]/td[2]')))

abrirnota = navegador.find_element('xpath', '//*[@id="19983412743"]/td[2]' )
x_coord = abrirnota.location['x']
y_coord = abrirnota.location['y']
ActionChains(navegador).move_by_offset(x_coord, y_coord).click().perform()


