from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\rishi\\Downloads\\chromedriver_win32\\chromedriver.exe")
# step 2: Enter the Url
driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
driver.maximize_window()
driver.switch_to.frame("iframeResult")
driver.find_element(by=By.XPATH, value="/html/body/button").click()
sleep(5)
# With javascript alert  operation 1) Accept 2) deney 3) Get the alert message 4) send some text

# code to switch alert
myAlertText =driver.switch_to.alert.text
print("Hey this is my alert text "+myAlertText)
driver.switch_to.alert.accept()