"""
    # Copyright © 2022 By Nguyễn Phú Khương(K.Auto)
    # ZALO : 0363561629
    # Email : dev.phukhuong0709@hotmail.com
    # Github : npk-0709
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

import os
import random
import time


class WebDriver:
    def __init__(self):
        self.__setup()

    def __setup(self):
        self.options = Options()
        self.options.add_experimental_option(
            'excludeSwitches', ['enable-logging'])
        self.options.add_experimental_option(
            "prefs", {"profile.default_content_setting_values.notifications": 2})
    def startDriver(self):
        service = Service(executable_path="chromedriver.exe")
        self.driver = webdriver.Chrome(service=service, options=self.options)
        return self.driver
    

def setCookieToBrowser(driver:webdriver.Chrome, cookie_:str):
    driver.get(f"https://www.facebook.com")
    time.sleep(1)
    for cookie in cookie_.split(';'):
        name, value = cookie.strip().split('=', 1)
        driver.add_cookie({'name': name.strip(), 'value': value.strip()})
    driver.get(f"https://www.facebook.com")


# cookie list
cookies = ['']
folderVideo = 'videos'
captions = ['hi','abc']
delay_click = 3
delay_wait_susses_upload = 60
cookie = str(random.choice(cookies)).strip() # random ngẫu nhiên cookie
listVideos = [os.path.join(os.getcwd(),folderVideo,i)  for i in os.listdir(folderVideo)] # get danh sách video trong thư mục
driver = WebDriver().startDriver()
setCookieToBrowser(driver,cookie)
for video in listVideos:
    caption = str(random.choice(captions)).strip() # random ngẫu nhiên nội dung
    driver.get('https://www.facebook.com/reels/create/?surface=ADDL_PROFILE_PLUS')
    print("OK")
    time.sleep(delay_click)
    action_chains = ActionChains(driver)
    for i in driver.find_elements(By.TAG_NAME,'input') :
        if str(i.get_attribute('type'))=='file':
            action_chains.drag_and_drop(i, driver.find_element(By.CLASS_NAME,'x1u5z0ei')).perform()
            i.send_keys(video)
            break
    
    print("IMPORTED")
    time.sleep(delay_click)
    #[i.click() for i in driver.find_elements(By.TAG_NAME,'span') if str(i.text)=='Tiếp']
    #driver.find_elements(By.CLASS_NAME,'x1j85h84')[7].click()
    driver.execute_script("document.getElementsByClassName('x1j85h84')[7].click()")
    print("CONTINUE")
    time.sleep(delay_click)
    [i.send_keys(caption) for i in driver.find_elements(By.TAG_NAME,'div') if str(i.get_attribute('role'))=='textbox']
    print("CAPTION")
    time.sleep(delay_click)
    #[i.click() for i in driver.find_elements(By.TAG_NAME,'span') if str(i.text)=='Đăng']
    #driver.find_elements(By.CLASS_NAME,'x1j85h84')[9].click()
    driver.execute_script("document.getElementsByClassName('x1j85h84')[9].click()")
    print("SUBMIT")
    time.sleep(delay_wait_susses_upload)

        
