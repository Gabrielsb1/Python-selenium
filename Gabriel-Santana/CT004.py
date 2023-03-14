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

# OBS: Esse código está 100% funcionando, certifique se que deseja cancelar sua assinatura antes de iniciar a execução do código.

nome_test = "Teste de cancelamento de assinatura na Netflix"

def CT004():
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
        
        # Configurações
        access_confg = driver.find_element(By.CLASS_NAME, "account-menu-item")
        access_confg.click()
        time.sleep(5)
        
        # Acessando configuração da conta
        access_confg_conta = driver.find_element(By.LINK_TEXT, 'Conta')
        access_confg_conta.click()
        time.sleep(5)
        
        # Click button (Cancelar Assinatura)
        cancelar_assinatura = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-uia='action-cancel-plan']"))
        )
        cancelar_assinatura.click()
        time.sleep(5)
               
CT004()