import sys
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@pytest.mark.skip
def testvalidatemouse():
    driver = webdriver.Chrome(
        executable_path="C:\\Users\\gayathri desa\\Downloads\\chromedriver_win32\\chromedriver.exe")
    # enter url
    driver.get("https://flipkart.com/")
    driver.maximize_window()
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/button").click()
    fashionmemu = driver.find_element(by=By.XPATH,value="//*[@id='container']/div/div[2]/div/div/div[4]/a/div[2]/div[1]/div")
    sleep(2)
    myMouse = ActionChains(driver)
    myMouse.move_to_element(fashionmemu).perform()
    womenethinic = driver.find_element(by=By.LINK_TEXT, value="Women Ethnic")
    myMouse.move_to_element(womenethinic).perform()
    womensarees = driver.find_element(by=By.LINK_TEXT, value="Women Sarees").click()
    sleep(2)
    driver.close()


def testwindowswitch():
    driver = webdriver.Chrome(
        executable_path="C:\\Users\\gayathri desa\\Downloads\\chromedriver_win32\\chromedriver.exe")
    # enter url
    driver.get("https://flipkart.com/")
    driver.maximize_window()
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/button").click()
    driver.find_element(by=By.XPATH, value="//*[@id='container']/div/footer/div/div[3]/div[1]/div[1]/a[6]").click()
    sleep(2)
    previouswindow = driver.window_handles[0]
    currentwindowtitle = driver.title
    sys.stderr.write(currentwindowtitle) #in pytest this is used instead of print statement
    #driver now has two windows
    newwindow =  driver.window_handles[1]
    driver.switch_to.window(newwindow)
    presentwindowtitle = driver.title
    sys.stderr.write(presentwindowtitle)
    print(presentwindowtitle+"this is print by print function")
    driver.find_element(by=By.XPATH,value="//*[@id='gatsby-focus-wrapper']/header[1]/div/div/a[2]").click()
    sleep(5)
    driver.switch_to.frame(0)
    driver.find_element(by=By.XPATH, value="//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys("gayathri")
    driver.find_element(by=By.XPATH,value="//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys("grocery")
    driver.find_element(by=By.XPATH,value="//*[@id='i13']/div[3]/div").click()
    driver.find_element(by=By.XPATH,value="//*[@id='i23']/div[3]/div").click()
    driver.find_element(by=By.XPATH,value="//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys("9865775775")
    driver.find_element(by=By.XPATH,value="//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys("abc@gmail.com")
    driver.find_element(by=By.XPATH,value="//*[@id='i83']/div[3]/div").click()
    driver.find_element(by=By.XPATH,value="//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys("500092")
    driver.find_element(by=By.XPATH,value="//*[@id='i109']/div[3]/div").click()
    driver.find_element(by=By.XPATH, value="//*[@id='mG61Hd']/div[2]/div[1]/div[3]/div[1]/div[1]/div/span").click()
    sleep(5)








