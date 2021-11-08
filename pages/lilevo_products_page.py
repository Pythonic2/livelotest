from selenium.webdriver.common.by import By
import time
from browser import Browser

'''Páginia relacionada a produtos '''


class LiveloProductsLocator(object):

    # Seletor do elementos utilizados na página

    # está com elementos engessado mas apenas para teste

    PRODUTO = 'CC-product-list-name-LVL202887-00' # ID

    BOTAO_ADD_TO_CART = 'cc-prodDetails-addToCart' # ID

    BOTAO_NAO_QUERO_DESCONTO = 'cc-prodDetails-refusePriceClubeDiscount' #ID


class LiveloProductsPage(Browser):


    def choose_product(self):
        # Navega para a pagina do produto
        self.find_until_element((By.ID, (LiveloProductsLocator.PRODUTO))).click()



    def add_to_cart(self):
        # clica no botao adicionar produto ao carrinho
        self.find_until_element((By.ID, (LiveloProductsLocator.BOTAO_ADD_TO_CART))).click()


    def dont_want_discount(self):
        # fecha poupup de disconto

        self.find_until_element((By.ID, (LiveloProductsLocator.BOTAO_NAO_QUERO_DESCONTO))).click()
