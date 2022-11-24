# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# https://www.sefaz.salvador.ba.gov.br/IPTU/certidaoDadosCadastrais - webform

# https://dti.sefaz.salvador.ba.gov.br/Modulos/DTI/ItivDeclaracaoFrm.aspx - cod. validação captcha
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd



def wait_for_window(self, timeout=2):
    time.sleep(round(timeout / 1000))
    wh_now = driver.window_handles
    wh_then = vars["window_handles"]
    if len(wh_now) > len(wh_then):
        return set(wh_now).difference(set(wh_then)).pop()

def test(url):
    # import time

    options = webdriver.FirefoxOptions()
    options.binary_location = r"C:/Users/fabio/AppData/Local/Mozilla Firefox/firefox.exe"
    driver = webdriver.Firefox(options=options)

    # ações
    selectInscricao(driver, url, inscr_im7)

    html_source = driver.page_source
    return html_source


def selectInscricao(driver, url, InscricaoImobiliaria7d):
    driver.get(url)
    time.sleep(2)
    # Clicka em caixa de escolha
    driver.get(
        "https://servicosweb.sefaz.salvador.ba.gov.br/WebsiteV2/Sistemas/CertidaoDadosCadastrais/Modulos/Principal/CertidaoDadosCadastraisFrm.aspx")
    # 2 | setWindowSize | 900x600 |
    driver.set_window_size(900, 600)
    # 3 | click | id=ctl00_ContentPlaceHolderPrincipal_txtCdInscricao |
    driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_txtCdInscricao").click()
    # 4 | type | id=ctl00_ContentPlaceHolderPrincipal_txtCdInscricao | 6451977
    driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_txtCdInscricao").send_keys(
        InscricaoImobiliaria7d)
    # 8 | click | id=ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbCdInscricaoImob |
    vars["win162"] = wait_for_window(2000)
    # 5 | click | id=ctl00_ContentPlaceHolderPrincipal_BtConsultar |
    driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_BtConsultar").click()
    # 6 | click | id=ctl00_ContentPlaceHolderPrincipal_BtConsultar |
    vars["window_handles"] = driver.window_handles
    # 7 | selectWindow | handle=${win162} |
    driver.find_element(By.ID, "ctl00_ContentPlaceHolderPrincipal_BtConsultar").click()
    # 8 | click | id=ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbCdInscricaoImob |
    vars["win162"] = wait_for_window(2000)
    # 9 | click | id=ctl00_ContentPlaceHolderPrincipal_UCCertidaoDadosCadastrais_LbnmContribuinte |
    driver.switch_to.window(vars["win162"])

    return


if __name__ == '__main__':
    df = pd.DataFrame()
    inscr_im7 = 6451977
    inscr_im6 = inscr_im7 / 10
    indcr_im6_dig = inscr_im7 % 10

    test(r'https://www.sefaz.salvador.ba.gov.br/IPTU/certidaoDadosCadastrais')

    test(r'https://dti.sefaz.salvador.ba.gov.br/Modulos/DTI/ItivDeclaracaoFrm.aspx')

    # 645197 - 7
    # r"https://servicosweb.sefaz.salvador.ba.gov.br/WebsiteV2/Sistemas/CertidaoDadosCadastrais/Modulos/Principal/CertidaoDadosCadastraisFrm.aspx"
