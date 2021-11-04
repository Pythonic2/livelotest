from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from browser import Browser
from selenium.webdriver.common.keys import Keys


'''Header da Página'''


class LiveloHeaderLocator(object):
    # Seletor do elementos utilizados na página
    # está com um elemento engessado mas apenas para teste
    INPUT_SEARCH = 'input-search'


class LiveloHeaderPage(Browser):


    def search_for_product(self):
        # pesquisa pelo termo berço
        search = self.wait.until(ec.element_to_be_clickable((By.ID,(LiveloHeaderLocator.INPUT_SEARCH))))
        search.click()
        search.send_keys('berço para bebe') # o Keys.ENTER poderia ser nessa linha mas n ia aparecer pesquisando,(muito rapido)
        search.send_keys(Keys.ENTER)

