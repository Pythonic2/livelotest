from selenium import webdriver


class Browser(object):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])



    # Inicia o browser chrome, mas pode ser feito com outros como Firefox, Safari e IE
    driver = webdriver.Chrome(options=options)
    # Define o tempo máximo para carregamento da página
    driver.set_page_load_timeout(30)
    # Maximiza a janela do browser ao ser iniciado
    driver.maximize_window()

    # Fecha o browser
    def browser_quit(self):
        self.driver.quit()

    # Limpa o browser
    def browser_clear(self):

        self.driver.execute_script('window.localStorage.clear()')
        self.driver.execute_script('window.sessionStorage.clear()')
        self.driver.refresh()

