from selenium.webdriver.common.by import By

from browser import Browser


'''Pagina inicial'''


class LiveloHomePage(Browser):


    def acess_page(self, url):
        # acessa url passada
        self.driver.get(url)


    def coockies(self):
        self.find_until_element((By.XPATH, ('//*[@id="btn-authorizeCoookies"]'))).click()

