import os

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By



link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    find_name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    find_name.send_keys("F")
    find_lastname = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    find_lastname.send_keys("G")
    find_email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    find_email.send_keys("fG@mail.ru")


    find_file = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname('file.txt'))
    file_path = os.path.join(current_dir, 'file.txt')
    find_file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    sleep(10)
    browser.quit()