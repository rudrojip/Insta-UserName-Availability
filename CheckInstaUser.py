# !pip3 install virtualenv
# !pip3 install selenium
# !wget https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz
# !tar -xvzf geckodriver-v0.18.0-linux64.tar.gz
# !cp geckodriver /usr/bin/
# !apt-get update && apt-hget upgrade
# !apt-get install firefox
# !virtualenv --system-site-packages /usr/bin/bin/rudr
# /usr/bin/bin/python3

from selenium.webdriver.common import keys
# import sys
# sys.path.insert(0,'/usr/lib/')
# sys.path.insert(0,'/usr/bin/')
import os , subprocess , time
from selenium import webdriver
class InstagramUserAvailability:
    os.environ['MOZ_HEADLESS'] = '1'
    def __init__(self,Check_Username):
        self.Check_Username = Check_Username
        self.driver = webdriver.Firefox()
        self.proxy = webdriver.Proxy()
    def open_url(self):
        driver=self.driver
        driver.get('https://www.instagramavailability.com/')
        time.sleep(3)
        search_user = driver.find_element_by_xpath("//input[@id='emailInput']")
        search_user.clear()
        time.sleep(2)
        search_user.send_keys(self.Check_Username)
        time.sleep(5)
        Color_Check = driver.find_element_by_xpath("//div[@id='emailGroup']")
        time.sleep(2)
        if 'success' in Color_Check.get_attribute('class'):
            return False
        elif 'error' in Color_Check.get_attribute('class'):
            return True
    def close(self):
        self.driver.close()
User_Name=input('Enter UserName To Check : ')
Insta_User_avail = InstagramUserAvailability(User_Name)
Check_Avail = Insta_User_avail.open_url()
if(Check_Avail):
    print("UserName Exists Trying To attack it")
else:
    print("UserName Does Not Exist")
Insta_User_avail.close()