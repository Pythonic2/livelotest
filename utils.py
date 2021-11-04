from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from nose.tools import assert_equal
# arquivo de teste


driver = webdriver.Chrome()
driver.get("https://www.livelo.com.br/cart")
driver.maximize_window()




