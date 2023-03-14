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


nome_test = "Verificar se a opção de Excluir perfil está funcionando corretamente"

def CT002():
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

        # Gerenciar perfis
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Gerenciar perfis'))
        ).click()
        time.sleep(5)
        
        # Escolher um perfil
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.LINK_TEXT, nome_perfil))
        ).click()
        time.sleep(5)
    
        # Excluir perfil
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-uia='profile-delete-button']"))
        ).click()
        time.sleep(5)
        
        # Excluir perfil definitivo
        click_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span[class='profile-button']"))
        )
        click_button.click()
        time.sleep(5)
        
        # Finalizar
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-uia='profile-button']"))
        ).click()
        time.sleep(5)
         
CT002()