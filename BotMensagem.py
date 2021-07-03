# Bibliotecas
from selenium import webdriver
import time
from webdriver_manager import chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# Navegar até o whatsapp
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com')
time.sleep(3)

# Definir contatos e grupos e mensagem a ser enviada
contatos = ["Nome"] #Colocar nome dos contatos a ser destinado a mensagem
mensagem = "Ola, Sou um bot" #Definir mensagem
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    # time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    # time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)

for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
# campo de pesquisa - "copyable-text selectable-text"
# campo de mensagem privada - "copyable-text selectable-text"
