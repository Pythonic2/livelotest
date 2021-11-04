from selenium.webdriver.common.by import By
from browser import Browser

'''Pagina do carrinho'''


class LiveloCartLocator(object):
    # Seletor do elementos utilizados na página

    TEXT_CART = '//*[@id="CC-cart-list"]/div[1]/h1'


class LilevoCartPage(Browser):

    @property
    def get_text_cart(self):
        textoElement = self.find_until_element((By.XPATH,(LiveloCartLocator.TEXT_CART)))
        return textoElement.get_attribute('innerText').strip()
