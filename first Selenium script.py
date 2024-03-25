from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium
from selenium.webdriver.support import expected_conditions as EC

# Initialize a WebDriver instance (e.g., ChromeDriver)
driver = webdriver.Chrome()

# Navigate to a webpage
driver.get("https://onkeydev.pragmaproducts.com/contoso/testautomation/")
wait = WebDriverWait(driver, 10)

# driver.implicitly_wait(1000)
wait.until(EC.title_contains("development_azure_account"))

# Retrieve the title of the webpage
title = driver.title
# Print the title to the console
print("Title of the webpage:", title)
# Close the WebDriver instance
driver.quit()

# element = driver.find_element_by_xpath('//button[@id="8eba098d-9432-4d0e-add4-c75b378bd596"]')
# element.click()
# driver.implicitly_wait(1000)


