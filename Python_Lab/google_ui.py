from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("http://www.google.com")
elem = driver.find_element_by_name("q")
elem.send_keys("testproject.io")
elem.send_keys(Keys.RETURN)
driver.close()


