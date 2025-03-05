'''PASSO A PASSO PREFEITURA

LOGIN 

CONFIRMAR MAIS TARDE

ADM -> UNICA OPCAO

COLOCAR O IM -> OPCAO DO MEIO

DECLARACAO -> TOMADOR -> ENTREGAR -> COLOCAR A COMPETENCIA

BOTAO INCLUIR DOCUMENTO 

PREENCHER DADOS'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
from metodos_selenium import write, click
from dotenv import load_dotenv
from time import sleep

def login_prefeitura():

    load_dotenv()

    user = os.getenv("ACESSO_PREFEITURA")
    password = os.getenv("PASSWORD_PREFEITURA")

    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    #chrome_options.add_argument("--disable-gpu")
    #chrome_options.add_argument("--window-size=1920,1080")
    #chrome_options.add_argument("--no-sandbox")
    #chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--ignore-certificate-errors")  # Ignorar erros SSL
    chrome_options.add_experimental_option("prefs", {
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "plugins.always_open_pdf_externally": True
    })

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    url = 'https://sispmjp.joaopessoa.pb.gov.br:8080/sispmjp/login.jsf'

    try:

        driver.get(url)

        write('//*[@id="j_username"]', user, driver)

        write('//*[@id="j_password"]', password, driver)

        click('//*[@id="commandButton_entrar"]', driver)

        click('//*[@id="formAtualizarContato:commandButton_confirmar_mais_tarde"]/span[2]', driver)

        sleep(0.2)

    except Exception as e:

        raise e

    return driver