import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Contracts(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def test_title(self):
        self.driver.get('https://173.36.208.191')
        try:
            uelement = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
            self.assertEqual( self.driver.title, 'User Login')
            print('Verified User Login page')
            uelement.send_keys('admin@cliqrtech.com')
            self.assertEqual( uelement.text, 'admin@cliqrtech.com')
            print('Verified username')
            pelement = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
            pelement.send_keys('C1sco12345')
            self.assertEqual( pelement.text, 'C1sco12345')
            print('Verified password')
            btnSubmit = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'btnSubmit')))
            btnSubmit.click
            print('Clicked on submit button')
            self.assertEqual( self.driver.title, 'CloudCenter Home')
        finally:
            self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


