from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

driver.get("https://www.google.com")
wait = WebDriverWait(driver,10)

# Close the browser
driver.quit()
