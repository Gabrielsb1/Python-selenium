import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# preencha os campos abaixo de acordo com a sua conta Netflix (Email, senha e Nome do perfil)
email = "suaConta@Outlook.com"
senha = "suaSenha"
nome_perfil = ''


def CT001():
    with webdriver.Chrome() as driver:
        print("Verificar se a pesquisa por títulos está funcionando corretamente.")
        
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

        # Clica no elemento e acessa o filme ou série
        access_play.click()
        time.sleep(5)
        
        assert "Reprodução concluída" in driver.page_source      
CT001()


def CT002():
    with webdriver.Chrome() as driver:
        print("Teste de adição de títulos à lista de favoritos na Netflix.")
        
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
        WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'previewModal--player-titleTreatmentWrapper'))
        )
        
        # Adiciona titulos na lista de favoritos
        driver.find_element(By.CSS_SELECTOR, "button[data-uia='add-to-my-list']").click()
        
        time.sleep(5)
        
        assert "Adicionado com sucesso" in driver.page_source 
CT002()


def CT003():
    with webdriver.Chrome() as driver:
        print("Teste de interromper áudio na reprodução.")
        
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
        
        # interrompe áudio na reprodução
        disable_audio = WebDriverWait(driver, 12).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-uia='control-volume-high']"))
        )
        disable_audio.click()
        time.sleep(5)
        
        assert "Desabilitado com sucesso" in driver.page_source   
CT003()


def CT004():
    with webdriver.Chrome() as driver:
        print("Teste de reprodução do próximo episódio na Netflix.")
        
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


def CT005():
    with webdriver.Chrome() as driver:
        print("Teste de pausa e retomada de reprodução na Netflix.")
        
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
        
        # Reprodução pausada
        pause_play = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-uia='control-play-pause-pause']"))
        )
        pause_play.click()
        time.sleep(5)
        
        # Reprodução retomada
        resume_play = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-uia='control-play-pause-play']"))
        )
        resume_play.click()
        time.sleep(5)
        
        assert "Reprodução interrompida e retomada com sucesso" in driver.page_source
CT005()