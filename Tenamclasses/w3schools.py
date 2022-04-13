import sys
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def testvalidatetrybutton():
    driver = webdriver.Chrome(
        executable_path="C:\\Users\\gayathri desa\\Downloads\\chromedriver_win32\\chromedriver.exe")
    # enter url
    driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
    driver.maximize_window()
    driver.switch_to.frame("iframeResult")
    driver.find_element(by=By.XPATH,value="/html/body/button").click()
    sleep(5)
    myAlert = driver.switch_to.alert.text
    print("this is my new alert text" +myAlert)
    driver.switch_to.alert.accept()





