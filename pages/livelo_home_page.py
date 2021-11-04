from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from browser import Browser



class LiveloHomePage(Browser):
    def get_element(self, locator):
        # aguarda elemento estar visível na tela
        WebDriverWait(self.driver, 10, poll_frequency=0.5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        # retorna elemento
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def acess_page(self, url):
        # acessa url passada
        self.driver.get(url)

