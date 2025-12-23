from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

link = "https://suninjuly.github.io/selects1.html"

def calc(x, y):
    return x + y

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_el = browser.find_element(By.ID, "num1")
    x = int(x_el.text)

    y_el = browser.find_element(By.ID, "num2")
    y = int(y_el.text)

    answer = calc(x, y)
    print(answer)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(answer))

    option1 = browser.find_element(By.CSS_SELECTOR, ".btn")
    option1.click()

finally:
    sleep(3)
    browser.quit()