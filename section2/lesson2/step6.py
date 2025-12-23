import math
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_el = browser.find_element(By.ID, "input_value")
    x = x_el.text
    print(x)

    y = calc(x)
    input_el = browser.find_element(By.ID, "answer")
    input_el.send_keys(y)

    browser.execute_script("window.scrollBy(0, 100);")

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()


finally:
    sleep(5)
    browser.quit()