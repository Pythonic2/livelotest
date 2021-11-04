from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from browser import Browser

from time import sleep
class LiveloProductsLocator(object):
    # Seletor do elementos utilizados na página
    # está com um elemento engessado mas apenas para teste
    PRODUTO = '//*[@id="CC-product-grid-title-LVL202887-04"]'
    BOTAO_ADD_TO_CART = '//*[@id="cc-prodDetails-addToCart"]'
    BOTAO_NAO_QUERO_DESCONTO = 'cc-prodDetails-refusePriceClubeDiscount' #id

class LiveloProductsPage(Browser):
    def choose_product(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable((By.XPATH, (LiveloProductsLocator.PRODUTO))))
        prod = self.driver.find_element(By.XPATH, (LiveloProductsLocator.PRODUTO)).get_attribute('href')
        self.driver.get(prod)
    def add_to_cart(self):
        wait = WebDriverWait(self.driver, 15, poll_frequency=0.5)
        element = wait.until(ec.element_to_be_clickable((By.XPATH, (LiveloProductsLocator.BOTAO_ADD_TO_CART))))
        add = self.driver.find_element(By.XPATH, (LiveloProductsLocator.BOTAO_ADD_TO_CART))
        add.click()
        sleep(10)
    def dont_want_discount(self):
        wait = WebDriverWait(self.driver, 15, poll_frequency=0.5)
        element = wait.until(ec.element_to_be_clickable((By.ID, (LiveloProductsLocator.BOTAO_NAO_QUERO_DESCONTO))))
        disc = self.driver.find_element(By.ID, (LiveloProductsLocator.BOTAO_NAO_QUERO_DESCONTO))
        disc.click()

