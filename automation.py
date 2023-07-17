from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
driver.get('D:/project/public/home.html')
time.sleep(3)
driver.find_element(By.ID, "login").click()
driver.find_element(By.ID, "email").send_keys('pujitha@gmail.com')
time.sleep(1)
driver.find_element(By.ID, "password").send_keys('123')
time.sleep(1)
driver.find_element(By.ID, "submit").click()
time.sleep(1)
alert = Alert(driver)
alert.accept()
origin_input = driver.find_element(By.ID, "origin")
origin_input.send_keys('Bapatla Engineering College')
time.sleep(2)

# Wait for autocomplete suggestions and select option
origin_suggestion = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class='pac-item']"))
)
origin_suggestion.click()

destination_input = driver.find_element(By.ID, "destination")
destination_input.send_keys('Hyderabad')
time.sleep(2)

# Wait for autocomplete suggestions and select option
destination_suggestion = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class='pac-item']"))
)
destination_suggestion.click()

# Scroll to the button
button = driver.find_element(By.ID, "w")
driver.execute_script("arguments[0].scrollIntoView();", button)

# Wait for the button to be clickable
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.ID, "w")))

button.click()
time.sleep(5)
driver.find_element(By.ID, "home").click()
time.sleep(1)

driver.quit()
