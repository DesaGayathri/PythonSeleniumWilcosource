from time import sleep

from selenium import webdriver
# selenium command to open a blank  chrome window
driver = webdriver.Chrome(executable_path="C:\\Users\\gayathri desa\\Downloads\\chromedriver_win32\\chromedriver.exe")

# load url to open chrome

driver.get("https://makemytrip.com")

# maximize the window

driver.maximize_window()
sleep(5)
driver.close()
driver.quit()
