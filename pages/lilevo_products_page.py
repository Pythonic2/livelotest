from selenium.webdriver.common.by import By
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
        # Navega para a pagina do produto
        element = self.find_until_element((By.XPATH, (LiveloProductsLocator.PRODUTO)))
        self.driver.get(element.get_attribute('href'))

    def add_to_cart(self):
        # clica no botao adicionar produto ao carrinho
        self.find_until_element((By.XPATH, (LiveloProductsLocator.BOTAO_ADD_TO_CART))).click()

    def dont_want_discount(self):
        # fecha poupup de disconto
        self.find_until_element((By.ID, (LiveloProductsLocator.BOTAO_NAO_QUERO_DESCONTO))).click()
