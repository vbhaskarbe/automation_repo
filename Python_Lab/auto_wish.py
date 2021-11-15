Let's start with code

Pre-requisite

First you must install these:-

1) Python Bindings for Selenium ( Browser Automation software )

    pip install selenium

2) Chrome webdriver
Download Chrome driver from here: Chromedriver download page( choose your specific version )
Extract it in a known location , as we need the location later

3) Chromium Web Browser( Open source version of chrome browser )

    sudo apt-get install chromium-browser

That’s it! You are all set.

Lets dive in right away-

from selenium import webdriver 

from selenium.webdriver.support.ui import WebDriverWait 

from selenium.webdriver.support import expected_conditions as EC 

from selenium.webdriver.common.keys import Keys 

from selenium.webdriver.common.by import By 

import time 

# Replace below path with the absolute path 

# to chromedriver in your computer 

driver = webdriver.Chrome('/home/saket/Downloads/chromedriver') 

driver.get("https://web.whatsapp.com/") 

wait = WebDriverWait(driver, 600) 

# Replace 'Friend's Name' with the name of your friend  

# or the name of a group  

target = '"Friend\'s Name"'

# Replace the below string with your own message 

string = " happy birthday boi"

x_arg = '//span[contains(@title,' + target + ')]'

group_title = wait.until(EC.presence_of_element_located(( 

 By.XPATH, x_arg))) 

group_title.click() 

inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'

input_box = wait.until(EC.presence_of_element_located(( 

 By.XPATH, inp_xpath))) 

for i in range(100): 

 input_box.send_keys(string + Keys.ENTER) 

 time.sleep(1) 

Keep your mobile phone with you. Choose whatsapp web from the top bar in whatsapp(3 dots)

Then Run the script ( make sure that you have added the absolute path for chromedriver and have replaced target variable with your friends name ). Scan the QR code that appears on the screen and enjoy.

You can make it responsive as well like kik bots just let your script read the input message of recipient and write command for further response… but it will be little lengthy.

Pro tip: You may get blocked by watsapp if you make it responsive like bots …. Be safe!!!


