import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
    def tearDown(self):
        self.driver.quit()
    def testCase1(self):
        driver = self.driver
        driver.get("http://www.google.com")
        assert "Google" in driver.title
        elem = driver.find_element_by_name("q")
        elem.send_keys("testproject.io")
        elem.send_keys(Keys.RETURN)
        assert "Kuku" not in driver.page_source
    def testCase2(self):
        driver = self.driver
        driver.get("http://www.google.com")
        assert "Google" in driver.title
        elem = driver.find_element_by_name("q")
        elem.send_keys("testproject.io")
        elem.send_keys(Keys.RETURN)
        assert "Blog" not in driver.page_source



