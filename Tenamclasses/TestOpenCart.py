from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def testvalidatephonenumber():
    driver = webdriver.Chrome(
        executable_path="C:\\Users\\gayathri desa\\Downloads\\chromedriver_win32\\chromedriver.exe")
    # enter url
    driver.get("https://demo.opencart.com/")
    driver.maximize_window()
    expectednumber = "123456789"
    sleep(5)
    actualnumber = driver.find_element(by=By.XPATH,value= "//*[@id='top-links']/ul/li[1]/span").text
    assert actualnumber == expectednumber
    driver.find_element(by=By.XPATH, value="//*[@id='top-links']/ul/li[1]/a/i").click()
    driver.close()
    driver.quit()

def testvalidatelaptopsitems():
    print("")
    driver = webdriver.Chrome(executable_path="C:\\Users\\gayathri desa\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://demo.opencart.com/")
    driver.maximize_window()
    expectedresult = "Laptops & Notebooks"
    sleep(5)
    actualresult = driver.find_element(by=By.XPATH,value="//*[@id='menu']/div[2]/ul/li[2]/a").text
    assert expectedresult == actualresult
    driver.find_element(by=By.XPATH, value="//*[@id='menu']/div[2]/ul/li[2]/a").click()
    actualsecondmenuitem = driver.find_element(by=By.XPATH,value="//*[@id='menu']/div[2]/ul/li[2]/div/div/ul/li[2]/a").text
    expectedsecondmenuitem = "Windows (0)"
    assert actualsecondmenuitem == expectedsecondmenuitem
    driver.find_element(by=By.XPATH, value="//*[@id='menu']/div[2]/ul/li[2]/div/div/ul/li[2]/a").click()
    sleep(5)
    driver.close()
    driver.quit()









