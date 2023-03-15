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
    print("Teste do sistema de classificação de filmes e séries na Netflix")
    
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
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.LINK_TEXT, nome_perfil))
        ).click()

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
        
        # Access classificação
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-uia='thumbs-rate-button']"))
        ).click()
        time.sleep(5)
        
        # Adicionando classificação (Amei)
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-uia='thumbs-wayup-button']"))
        ).click()
        time.sleep(5)
        
        assert "Acesso a classificação de filmes e séries funcionando corretamente" in driver.page_source  
CT001()

def CT002():
    print("Verificar se a opção de Excluir perfil está funcionando corretamente")
    
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
        
        assert "Exclusão do perfil com sucesso" in driver.page_source  
CT002()

def CT003():
    print("Verificar se a opção de legendas e áudio em diferentes idiomas está funcionando corretamente.")
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
        search_bar.send_keys("De Volta ao Espaço")
        
        # Espera até que o elemento esteja disponível e clicável
        access_play = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'previewModal--player-titleTreatmentWrapper'))
        )
        access_play.click()
        time.sleep(5)
        
        # Idioma e Legenda
        Acess_IL = WebDriverWait(driver, 12).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-uia='control-audio-subtitle']"))
        )
        Acess_IL.click()
        time.sleep(5)
        
        # Alterando Idioma
        WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "li[data-uia='audio-item-Inglês [original]']"))
        ).click()    
        time.sleep(5)
        
        # Alterando Legenda
        WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "li[data-uia='subtitle-item-Português']"))
        ).click() 
        time.sleep(5)
          
        assert "Alteração da legenda/idioma funcionando corretamente" in driver.page_source  
CT003()

def CT004():
    print("Teste de cancelamento de assinatura na Netflix")
    
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
        
        assert "Encerramento da assinatura com sucesso" in driver.page_source   
CT004()

def CT005():
    with webdriver.Chrome() as driver:
        print("Verificar se a opção de assistir ao trailer de um filme está funcionando corretamente.")
        
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
        
        assert "Trailer exibido com sucesso" in driver.page_source  
CT005()