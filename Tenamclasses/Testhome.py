from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def testvalidatehomepageloaded():
    # open a browser

    driver = webdriver.Chrome(
        executable_path="C:\\Users\\gayathri desa\\Downloads\\chromedriver_win32\\chromedriver.exe")
    # enter url
    driver.get("https://demo.opencart.com/")
    # verify the home page opens
    expectedtitle = "Your Store"
    actualtitle = driver.title
    assert actualtitle == expectedtitle
    driver.close()  # close the browser
    driver.quit()  # remove the driver instance from the memory


def testverifycurrencyfieldispresent():
    print("")
    driver = webdriver.Chrome(executable_path="C:\\Users\\gayathri desa\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://demo.opencart.com/")
    driver.maximize_window()
    expectedtext = "Currency"
    sleep(5) # hard sleep explicit wait
    elementactualtext = driver.find_element(by=By.XPATH,value="//*[@id='form-currency']/div/button/span").text
    assert elementactualtext == expectedtext
    driver.close()
    driver.quit()


def testvalidatedesktopsmenuitems():
    print("")
    driver = webdriver.Chrome(executable_path="C:\\Users\\gayathri desa\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://demo.opencart.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    expectedtext = "Desktops"
    elementactualtext = driver.find_element(by=By.XPATH,value="//*[@id='menu']/div[2]/ul/li[1]/a").text
    assert elementactualtext == expectedtext
    driver.find_element(by=By.XPATH, value="//*[@id='menu']/div[2]/ul/li[1]/a").click()
    sleep(5) #
    actualfirstmemuitem = driver.find_element(by=By.XPATH,value="//*[@id='menu']/div[2]/ul/li[1]/div/div/ul/li[1]/a").text
    expectedmenuitemone = "PC (0)"
    assert actualfirstmemuitem == expectedmenuitemone
    driver.find_element(by=By.XPATH,value="//*[@id='menu']/div[2]/ul/li[1]/div/div/ul/li[1]/a").click()
    driver.close()
    driver.quit()







