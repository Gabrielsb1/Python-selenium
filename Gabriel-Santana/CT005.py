import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Informe seu (email, senha e nome_perfil) da sua conta Netflix
email = "suaConta@Outlook.com"
senha = "suaSenha"
nome_perfil = ''


nome_test = "Verificar se a opção de assistir ao trailer de um filme está funcionando corretamente."

def CT005():
    with webdriver.Chrome() as driver:
        # Acessa a página inicial da Netflix
        driver.get("https://www.netflix.com/in/login")

        # Preenche o email
        email_input = driver.find_element(By.NAME, "userLoginId")
        email_input.send_keys(email)

        # Preenche a senha
        senha_input = driver.find_element(By.NAME, "password")
        senha_input.send_keys(senha)

        # Faz login
        driver.find_element(By.CSS_SELECTOR, "button[data-uia=login-submit-button]").send_keys(Keys.ENTER)
    
        # Selecionar o perfil
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.LINK_TEXT, nome_perfil))
        ).click()
        time.sleep(5)
        
        # Busca por gêneros de filmes e séries
        navegation_filme = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Filmes'))
        )
        navegation_filme.click()
        time.sleep(5)
        
        # Escolha do filme
        access_filme = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Luther: O Cair da Noite'))
        )
        access_filme.send_keys(Keys.ENTER)
        time.sleep(5)
        
        # Acessar Trailer
        access_trailer = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-label='Trailer: Luther: O Cair da Noite']"))
        )
        access_trailer.send_keys(Keys.ENTER)
        time.sleep(5)
        
CT005()