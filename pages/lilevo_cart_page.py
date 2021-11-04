from selenium.webdriver.common.by import By
from browser import Browser

'''Pagina do carrinho'''


class LiveloCartLocator(object):
    # Seletor do elementos utilizados na página

    TEXT_CART = 'CC-cart-list'


class LilevoCartPage(Browser):


    def get_text_cart(self):
        self.driver.implicitly_wait(5)
        textoElement = self.driver.find_element(By.ID,('CC-cart-list'))
        ver = bool(textoElement)
        return ver
