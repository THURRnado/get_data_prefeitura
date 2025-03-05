from time import sleep
from metodos_selenium import write, click
from login_prefeitura import login_prefeitura

def process_prefeitura(im:str, mes:str, ano:str, numero_nota:str):

    try:

        driver = login_prefeitura()

        driver.get('https://sispmjp.joaopessoa.pb.gov.br:8080/sispmjp/paginas/ds/DS_GerenciarContribuinte.jsf')

        write('//*[@id="form:contribuintesVinculados:j_idt64:filter"]', im, driver)

        click('//*[@id="form:contribuintesVinculados:0:commandButton_representarContribuinte"]/span[1]', driver)

        sleep(0.2)

        driver.get('https://sispmjp.joaopessoa.pb.gov.br:8080/sispmjp/paginas/ds/DS_EntregarDeclaracaoTomador.jsf')

        write('//*[@id="formEntregarDeclaracaoTomador:mes"]', mes, driver)

        write('//*[@id="formEntregarDeclaracaoTomador:ano"]', ano, driver)

        click('//*[@id="formEntregarDeclaracaoTomador:confirmarButton"]/span[2]', driver)

        click('//*[@id="form_lista_notas_declaracoes:commandButton_incluirDocumento"]/span', driver)

        write('//*[@id="form_emitir_nfse_ne:input_num_nota"]', numero_nota, driver)

        click('//*[@id="form_emitir_nfse_ne:commandButton_continuar"]/span[2]', driver)

        sleep(5)

        driver.quit()

    except Exception as e:

        raise e