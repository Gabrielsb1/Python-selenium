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


nome_test = "Verificar a opção de adicionar um novo perfil está funcionando corretamente"

def CT003():
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

        # Adicionar novo perfil
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Adicionar perfil'))
        ).click()
        time.sleep(5)
        
        # Adiciona o nome da conta
        add_nome = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "add-profile-name"))
        )
        add_nome.send_keys(nome_perfil)
        time.sleep(5)
        
        # Criar conta
        click_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span[class='profile-button preferred-action preferred-active']"))
        )
        click_button.click()
        time.sleep(5)
            
CT003()