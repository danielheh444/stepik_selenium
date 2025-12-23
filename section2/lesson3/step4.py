import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By



link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    print(x)

    y = calc(x)
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()