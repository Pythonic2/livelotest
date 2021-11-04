from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from browser import Browser


from time import sleep
class LiveloCartLocator(object):
    # Seletor do elementos utilizados na página

    TEXT_CART = 'CC-cart-list'


class LilevoCartPage(Browser):

    def get_text_cart(self):
        self.driver.implicitly_wait(5)
        textoElement = self.driver.find_element(By.ID,('CC-cart-list'))
        ver = bool(textoElement)
        return ver




