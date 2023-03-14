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


nome_test = "Teste de reprodução do próximo episódio na Netflix"

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

        # Seleciona o perfil
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.LINK_TEXT, nome_perfil))
        ).click()
        
         # Pesquisa por um filme
        search_bar = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "searchTab"))
        )
        search_bar.send_keys("Round 6")
        

        # Espera até que o elemento esteja disponível e clicável
        access_play = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'previewModal--player-titleTreatmentWrapper'))
        )
        access_play.click()
        
        time.sleep(5)
        
        # Reprodução do próximo episódio
        trade_episodio = WebDriverWait(driver, 12).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-uia='control-next']"))
        )
        trade_episodio.click()
    
        time.sleep(5)
        
        assert "Reprodução do novo episódio concluída com sucesso" in driver.page_source
        
CT004()