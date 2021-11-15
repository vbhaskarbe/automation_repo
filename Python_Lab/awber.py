import unittest
from selenium import webdriver
 
class AweberTest(unittest.TestCase):
 
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
 
    def test_title(self):
        self.driver.get('https://www.aweber.com')
        self.assertEqual(
            self.driver.title,
            'AWeber Email Marketing Services & Software Solutions for Small Business')
 
    def test_pricing(self):
        self.driver.get('https://www.aweber.com')
        order_tab = self.driver.find_element_by_css_selector('#ordertab>a')
        order_tab.click()
        pricings = self.driver.find_elements_by_css_selector('#pricing-plans .price')
        pricing_texts = [price.text for price in pricings]
        self.assertIn('19', pricing_texts)
        self.assertIn('49', pricing_texts)
        self.assertIn('194', pricing_texts)
 
    def test_default_monthly(self):
        self.driver.get('https://www.aweber.com/order.htm')
        monthly_radio = self.driver.find_element_by_css_selector('#term_548')
        self.assertTrue(monthly_radio.is_selected())
 
    def test_search(self):
        self.driver.get('https://www.aweber.com/search.htm')
        search_input = self.driver.find_element_by_css_selector('#content input[type="text"]')
        search_input.send_keys('Meet the Team')
        search_submit = self.driver.find_element_by_css_selector('#content input[type="submit"]')
        search_submit.click()
        self.assertTrue(self.driver.find_element_by_css_selector('a[href="http://www.aweber.com/meet-the-team.htm"]'))
 
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        
        

