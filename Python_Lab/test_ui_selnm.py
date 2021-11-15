import time
import unittest
import os
#import cc_setup
from cc_setup import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Contracts(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def test_title(self):
        print(os.environ)
        #self.driver.get(cc_setup.MGMT_URL) #'https://173.36.208.191')
        self.driver.get(MGMT_URL) #'https://173.36.208.191')
        try:
            uelement = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
            self.assertEqual( self.driver.title, 'User Login')
            print('Verified User Login page')
            #uelement.send_keys(cc_setup.TEST_USERMAIL)
            uelement.send_keys(TEST_USERMAIL)
            #self.assertEqual( uelement.text, 'admin@cliqrtech.com')
            print('Verified username')
            pelement = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
            pelement.send_keys(TEST_USERPASS)
            #pelement.send_keys(cc_setup.TEST_USERPASS)
            #self.assertEqual( pelement.text, 'C1sco12345')
            print('Verified password')
            btnsubmit = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'btnSubmit')))
            btnsubmit.click
            print('Clicked on submit button')
            #title = WebDriverWait(self.driver, 30).until(EC.title_contains('CloudCenter Home'))
            #self.assertEqual( self.driver.title, 'CloudCenter Home')
        finally:
            self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


