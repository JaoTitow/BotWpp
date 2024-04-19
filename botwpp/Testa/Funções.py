from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from pathlib import Path
from time import sleep

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)  

#Abrindo o Wpp
def abrir_janela_whatsapp():
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, timeout=60) #Serve pra não bugar // sem ele o wpp simplesmente fecha e é isso
    barra_lateral = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]'))) #Vai localizar a barra lateral das conversas
    driver.implicitly_wait(10)

#Pesquisando o contato
def abrindo_a_conversa(nome_contato):
    barra_pesquisa = driver.find_element(By.XPATH, '//div[@title="Caixa de texto de pesquisa"]')#Responsavel por achar caixa de pesquisa
    barra_pesquisa.send_keys(Keys.CONTROL + 'a') #Responsavel por apagar e certificar que não tem nada na caixa de pesquisa
    barra_pesquisa.send_keys(Keys.DELETE)

    barra_pesquisa = driver.find_element(By.XPATH, '//div[@title="Caixa de texto de pesquisa"]') 
    barra_pesquisa.send_keys(nome_contato) #Parte que pesquisa o nome do contato

    wait = WebDriverWait(driver, timeout=2) #Selecionando o contato desejado
    
    span_buscando = f'//span[@title="{nome_contato}"]'
    conversa_lateral = wait.until(EC.presence_of_element_located((By.XPATH, span_buscando))) #Procura a conversa na barra lateral
    driver.execute_script("arguments[0].scrollIntoView(true);", conversa_lateral) #Sem isso o script simplesmente crasha // serve pra "Scrollar" até o elemento caso ele esteja fora de vista
    conversa_lateral.click()

def fechando_a_conversa(): #Fecha conversa e limpa a barra de pesquisa
    barra_pesquisa = driver.find_element(By.XPATH, '//div[@title="Caixa de texto de pesquisa"]')
    barra_pesquisa.send_keys(Keys.CONTROL + 'a')
    barra_pesquisa.send_keys(Keys.DELETE)
    barra_pesquisa.send_keys(Keys.ESCAPE)
    
#Enviando mensagem
def enviando_mensagens(mensagem):
    caixa_de_mensagem = driver.find_element(By.XPATH, '//div[@title="Digite uma mensagem"]')
    caixa_de_mensagem.send_keys(mensagem)
    caixa_de_mensagem.send_keys(Keys.RETURN)

#Enviando documentos
def enviando_documentos(caminho_doc):
    bt_de_arquivos = driver.find_element(By.XPATH, '//div[@title="Anexar" or @title="Attach" ]')
    bt_de_arquivos.click()

    bt_doc = driver.find_element(By.XPATH, '//input[@accept="*" and @type="file"]')
    bt_doc.send_keys(caminho_doc)

    bt_doc_enviar = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
    bt_doc_enviar.click()

#Enviando fotos
def enviando_fotos(caminho_foto):
    bt_de_arquivos = driver.find_element(By.XPATH, '//div[@title="Anexar" or @title="Attach" ]')
    bt_de_arquivos.click()

    bt_doc = driver.find_element(By.XPATH, '//input[@accept="*" and @type="file"]')
    bt_doc.send_keys(caminho_foto)

    bt_doc_enviar = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
    bt_doc_enviar.click()