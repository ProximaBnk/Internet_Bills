"""This is a program to automate internet payments from zain"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://zain.app/ar/home")
########
lang = driver.find_element(
    By.XPATH, value='//*[@id="formOnboarding"]/ul/li[1]/div/label'
)
submit_lang = driver.find_element(By.XPATH, value='//*[@id="formOnboarding"]/button[1]')
lang.click()
time.sleep(1)
submit_lang.click()
proceed = driver.find_element(By.CSS_SELECTOR, value=".onboarding__block a")
proceed.click()
time.sleep(3)
data_input = driver.find_element(By.ID, "lineTypeData")
driver.execute_script("arguments[0].click();", data_input)
########
data_info = driver.find_element(By.ID, "txtSubscriber")
data_info.send_keys("831035443038")
data_info.send_keys(Keys.ENTER)
########
time.sleep(2)
paying_button = driver.find_element(By.ID, value="btnPayBillSubmit")
print(paying_button)
paying_button.click()
########
time.sleep(2)
card_number = driver.find_element(By.ID, value="card-number")
# card_number.send_keys("234234423423")
expiry_date = driver.find_element(By.ID, value="exp-date")
# expiry_date.send_keys("02/26")
cvv = driver.find_element(By.ID, value="cvv")
# cvv.send_keys("232")
time.sleep(1000)
driver.quit()
