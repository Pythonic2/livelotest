from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from browser import Browser

'''Páginia relacionada a produtos '''


class LiveloProductsLocator(object):
    # Seletor do elementos utilizados na página
    # está com um elemento engessado mas apenas para teste
    PRODUTO = '//*[@id="CC-product-grid-title-LVL202887-04"]'
    BOTAO_ADD_TO_CART = '//*[@id="cc-prodDetails-addToCart"]'
    BOTAO_NAO_QUERO_DESCONTO = 'cc-prodDetails-refusePriceClubeDiscount' #id



class LiveloProductsPage(Browser):
    def choose_product(self):
        #espera até 20s
        wait = WebDriverWait(self.driver, 20)
        #retorna o elemento achado
        element = wait.until(ec.element_to_be_clickable((By.XPATH, (LiveloProductsLocator.PRODUTO))))

        #pega o link do produto
        self.driver.get(element.get_attribute('href'))


    def add_to_cart(self):
        # espera até 20s
        wait = WebDriverWait(self.driver, 20)
        # retorna o elemento achado
        element = wait.until(ec.element_to_be_clickable((By.XPATH, (LiveloProductsLocator.BOTAO_ADD_TO_CART))))
        #clica no elemento
        self.driver.find_element(By.XPATH, (LiveloProductsLocator.BOTAO_ADD_TO_CART)).click()


    def dont_want_discount(self):
        # espera até 20s
        wait = WebDriverWait(self.driver, 20)
        # retorna o elemento achado
        element = wait.until(ec.element_to_be_clickable((By.ID, (LiveloProductsLocator.BOTAO_NAO_QUERO_DESCONTO))))
        # clica no elemento
        self.driver.find_element(By.ID, (LiveloProductsLocator.BOTAO_NAO_QUERO_DESCONTO)).click()
