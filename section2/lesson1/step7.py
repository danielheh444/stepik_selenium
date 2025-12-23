import math
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    print(x)

    y = calc(x)
    print(y)
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    sleep(4)
    browser.quit()