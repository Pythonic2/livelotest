from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class Browser(object):

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # Inicia o browser chrome
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    # Define o tempo máximo para carregamento da página
    driver.set_page_load_timeout(30)
    # Maximiza a janela do browser ao ser iniciado
    driver.maximize_window()


    # metodo para busca de elementos com wait aplicado
    def find_until_element(self, locator):
        return self.wait.until(ec.presence_of_element_located(locator))

    # Fecha o browser
    def browser_quit(self):
        self.driver.quit()

    # Limpa o browser
    def browser_clear(self):
        self.driver.execute_script('window.localStorage.clear()')
        self.driver.execute_script('window.sessionStorage.clear()')
        self.driver.refresh()
