from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#open browser
driver = webdriver.Chrome()
time.sleep(3)

driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(2)


#Type username student into Username field
username_locator = driver.find_element(By.ID , "username")
username_locator.send_keys("student")

#Type password Password123 into Password field
password_locator = driver.find_element(By.NAME , "password")
password_locator.send_keys("Password123")

#Puch Submit button
submit_button_locator = driver.find_element(By.XPATH , "//button[@class='btn']")
submit_button_locator.click()

time.sleep(2)
#Verify new page URL contains practicetestautomation.com/logged-in-successfully/
actual_url = driver.current_url
assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

#Verify new page contains expected text ('Congratulations' or 'successfully logged in')
test_locator = driver.find_element(By.TAG_NAME , "h1")
actual_url = test_locator.text
assert  actual_url == "Logged In Successfully"

#Verify button Log out is displayed on the new page
log_out_locator = driver.find_element(By.LINK_TEXT , "Log out")
assert log_out_locator.is_displayed()
