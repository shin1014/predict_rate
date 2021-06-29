#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
options = Options()
options.add_argument('--disable-gpu');
options.add_argument('--disable-extensions');
options.add_argument('--proxy-server="direct://"');
options.add_argument('--proxy-bypass-list=*');
options.add_argument('--start-maximized');
driver = webdriver.Chrome()

import time
import random
import datetime

def l_sleep():
    time.sleep(random.randint(30,70)/100)

def m_sleep():
    time.sleep(random.randint(10,50)/10)

def click_selector(selector):
    button = driver.find_element_by_css_selector(selector)
    button.click()
    l_sleep()

def click_xpath(xpath):
    button = driver.find_element_by_xpath(xpath)
    button.click()
    l_sleep()

def scrollByElemAndOffset(element, offset = 0):

    driver.execute_script("arguments[0].scrollIntoView();", element)
    if (offset != 0):
        script = "window.scrollTo(0, window.pageYOffset + " + str(offset) + ");"
        self.driver.execute_script(script)

def setup_demo():
    # Demo Tradeにアクセスする
    url = 'https://demotrade.highlow.com'
    driver.get(url)

    driver.maximize_window()

    l_sleep()

    #quick demo
    click_selector('#header > div > div > div > div > div > span > span > a.highlight.hidden-xs.outlineNone > i')
    time.sleep(random.randint(250,300)/100)
    #bonus
    click_selector('#account-balance > div.pull-left.staBlock.cashback-balance.onboarding-highlighted.hiddenArea > div > div.onboarding-tooltip-content.success.last-child > a')
   
    
    #onehour
#     click_selector('#assetsCategoryFilterZoneRegion > div > div:nth-child(3) > span > span')

    #day
#     click_selector('#assetsCategoryFilterZoneRegion > div > div:nth-child(4) > span > span')
    
    #hour
    click_selector('#assetsCategoryFilterZoneRegion > div > div:nth-child(3)')
    
    #One Click mode
    click_selector('#strikeAreaRegion > div > div.chartTimeArea.pull-right.last-child > a')
    
    #Scroll to click HIGH&LOW
    scrollByElemAndOffset(driver.find_element_by_xpath('//*[@id="ChangingStrike"]'), 0)
    
    l_sleep()

def select_money(moneyname):
    scrollByElemAndOffset(driver.find_element_by_xpath('//*[@id="ChangingStrike"]'), 0)
    if moneyname == 'USD_JPY':
        click_xpath('//*[@id="6425"]/div[1]')
        
    elif moneyname == 'EUR_USD':
        click_xpath('//*[@id="6395"]/div[1]')
    
    elif moneyname == 'EUR_JPY':
        click_xpath('//*[@id="6245"]/div[1]')
    
    elif moneyname == 'GBP_JPY':
        click_xpath('//*[@id="6263"]/div[1]')
    
    elif moneyname == 'AUD_JPY':
        click_xpath('//*[@id="6208"]/div[1]')
    
    else:
        print("invalid money!")

def high_entry():
    click_xpath('//*[@id="up_button"]')
    l_sleep()

def low_entry():
    click_xpath('//*[@id="down_button"]')
    l_sleep()

def get_screen_shot():
    w = driver.execute_script("return document.body.scrollWidth;")
    h = driver.execute_script("return document.body.scrollHeight;")

    # set window size
    driver.set_window_size(w,h)

    # Get Screen Shot
    driver.save_screenshot("image/"+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+".png")
    
# def main():
#     setup_quickdemo()
#     select_money('CAD_JPY')
#     low_entry()
#     select_money('AUD_JPY')
#     high_entry()
#     select_money('EUR_JPY')
#     high_entry()

# main()
    


# In[ ]:





# In[ ]:





