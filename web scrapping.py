from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import time

driver = webdriver.Chrome('/home/akshay/Downloads/chromedriver')

# ---------------------using keys--------------------------------------------------------
# driver.get('https://www.wikipedia.org/')
# find = driver.find_element_by_id('searchInput')
# find.clear()
# find.send_keys("python")
# find.send_keys(Keys.RETURN)
# py = driver.find_element_by_link_text('Python (programming language)')
# py.send_keys(Keys.RETURN)
# driver.quit()

# ----------image extraction-------------------------------------------------------------
# img = driver.find_element_by_class_name('thumbimage')
# src = img.get_attribute('src')
# urllib.request.urlretrieve(src, 'image.png')
# ---------------------video extraction--------------------------------------------------

driver.get('https://wikipedia.org')