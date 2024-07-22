from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest


link1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"



class TestMainPage1():
    def test_add_to_basket(self, browser):
        browser.get(link1)
        time.sleep(5)
        button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
        print(button,'button')
        #button.click()
        assert len(button)>0,"'Add to Basket' button not found"


