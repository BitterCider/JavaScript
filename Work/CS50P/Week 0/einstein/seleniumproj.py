import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += r"C:\Users\user\Desktop\geckodriver.exe"
driver = webdriver.Firefox()
driver.get("https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")
driver.implicitly_wait(3)
element1 = driver.find_element(By.ID, 'downloadButton')
element1.click()

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, 'progress-label'),
                'Complete!'                                     )
)