from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import chromedriver_binary
import time
import math


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')
book_button = browser.find_element_by_id('book')
price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$105'))
book_button.click()
input_value = browser.find_element_by_id("input_value")
input_value = input_value.text
answer = browser.find_element_by_id("answer")
result = math.log(abs(12*math.sin(int(input_value))))
answer.send_keys(str(result))
submit = browser.find_element_by_id("solve")
submit.click()
time.sleep(15)





browser.quit()