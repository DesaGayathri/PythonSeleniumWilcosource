
from selenium import webdriver



def testlogincancel():
    print("cancelling order")

def testloginorder():
    print("login and ordering")

def testsearchlogin():
    assert 5==5

def testvalidatewebpageopens():





 # selenium command to open a blank  chrome window
  driver = webdriver.Chrome(executable_path="C:\\Users\\gayathri desa\\Downloads\\chromedriver_win32\\chromedriver.exe")

  # load url to open chrome

  driver.get("https://makemytrip.com")
  expectedtitle = "MakeMyTrip - #1 Travel Website 50% OFF on Hotels, Flights & Holiday"

  # maximize the window

  driver.maximize_window()

  actualtitle = driver.title
  assert actualtitle == expectedtitle
  driver.close()
  driver.quit()