from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://onkeydev.pragmaproducts.com/contoso/testautomation/")
# time.sleep(2)
# development_azure_account = driver.find_element(By.NAME,'development_azure_account').click()
# time.sleep(2)

# Wait for the presence of element
wait = WebDriverWait(driver,30)
development_azure_account = wait.until(expected_conditions.presence_of_element_located((By.ID,"8eba098d-9432-4d0e-add4-c75b378bd596")))
development_azure_account.click()
time.sleep(3)


