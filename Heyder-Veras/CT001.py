import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# preencha os campos abaixo de acordo com a sua conta Netflix (Email, senha e Nome do perfil)
email = ""
senha = ""
nome_perfil = ''


def CT001():
    with webdriver.Chrome() as driver:
        print("Verificar se o sistema de busca por gêneros de filmes e séries está funcionando corretamente")
        
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

        # Busca por gêneros de filmes e séries
        navegation_filme = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Filmes'))
        )
        navegation_filme.click()
        time.sleep(5)
        
        # Acessa o button de gênero
        acces_genero = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "label"))
        )
        acces_genero.click()
        time.sleep(5)
        
        # Escolhe o gênero
        click_genero = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Ação'))
        )
        click_genero.click()
        time.sleep(5)
        
        assert "Busca por gêneros de filmes e séries está funcionando corretamente" in driver.page_source
          
CT001()

def CT002():
    print("Verificar se os trailers estão sendo reproduzidos corretamente na página de detalhes de um título")
    
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
        
        #Acessa o detalhe e verifica o trailer
        acess_detalhe = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-uia='billboard-more-info']"))
        )
        acess_detalhe.click()
        time.sleep(5)
        
        assert "Reprodução de trailers funcionando corretamente" in driver.page_source  
        return None

CT002()

def CT003():
    print("Verificar a funcionalidade de adicionar títulos a lista do usuário")
    
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

        # Entrar no perfil
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
        
        # Adiciona titulos na lista de favoritos
        driver.find_element(By.CSS_SELECTOR, "button[data-uia='add-to-my-list']").click()
        time.sleep(5)
        
        assert "Titulo adicionado na lista com sucesso" in driver.page_source  
        return None
    
CT003()

def CT004():
    print("Adicionar um novo perfil na Netflix")
    
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
        
        assert f"Conta {nome_perfil}, criada com sucesso" in driver.page_source  
        return None 
    
CT004()

def CT005():
    with webdriver.Chrome() as driver:
        print("Verificar se a opção de criar um perfil para crianças está funcionando corretamente")
        
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
        
        # Inserir conta acesso kids
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "add-kids-option"))
        ).click()
        time.sleep(5)
        
        # Criar conta
        click_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span[class='profile-button preferred-action preferred-active']"))
        )
        click_button.click()
        time.sleep(5)
        
        assert "Perfil infantil criado com sucesso" in driver.page_source  
        return None
     
CT005()