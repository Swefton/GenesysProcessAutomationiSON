import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
from datetime import date
from datetime import timedelta

#initalizing driver settings
options = uc.ChromeOptions()
# chrome://version/
profile = "C:\\Users\\thelo\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2" # CHANGE TO CHROME PROFILE PATH
options.add_argument(f"user-data-dir={profile}")
driver = uc.Chrome(options=options,use_subprocess=True)

# dictionary that contains information on browser download behaviour
params = {
    "behavior": "allow",
    "downloadPath": r'C:\Users\thelo\OneDrive\Desktop\Internship\Scraper\downloads' # CHANGE TO DOWNLOAD PATH
}

# dictionary, keys are strings, values are method under the 'By' object
method_dict = {
    "xpath": By.XPATH,
    "cssselector": By.CSS_SELECTOR,
    "id": By.ID,
    "classname": By.CLASS_NAME
}

def open_webpage(url='https://apps.euw2.pure.cloud/directory/#/admin/welcomeV2',wait=15):
    '''
    opens webpage on chrome, accounts for slight delay to allow webpage to load
    url = direct link to webpage, defaults to admin page of genesys for initialization
    '''
    time.sleep(2)
    driver.get(url)
    time.sleep(wait)

def click_element(selector,selector_value,duration=999):
    '''
    finds element on webpage and clicks on it
    selector = selector/strategy to select web element (str)
    selector_value = selector value as shown by selectorshub (str)
    duration = how long the script will wait to try and find the element (int)
    returns element = returns found web element (selenium object)
    '''
    selector = method_dict[selector]
    WebDriverWait(driver, duration).until(EC.presence_of_element_located((selector, selector_value)))
    time.sleep(1.5)
    element = driver.find_element(selector,selector_value)
    driver.find_element(selector,selector_value).click()
    time.sleep(3)
    return element

def type_element(selector, selector_value, message):
    '''
    after an element is found and clicked, types message into it
    selector = selector/strategy to select web element (str)
    selector_value = selector value as shown by selectorshub (str)
    message = input in text field, could also be object of keys such as Keys.ENTER (str or obj)
    '''
    selector = method_dict[selector]
    time.sleep(1.5)
    element = driver.find_element(selector,selector_value)
    element.send_keys(message)
    time.sleep(1)

def frame_switch(framevalue, selector='xpath'):
    frame = driver.find_element(method_dict[selector], framevalue)
    driver.switch_to.frame(frame)
    return

def rename_newest_file(directory):
    # List all files in the directory along with their timestamps
    files = [(file, os.path.getmtime(os.path.join(directory, file))) for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
        
    if not files:
        return None
    
    # Find the file with the latest timestamp
    newest_file = max(files, key=lambda item: item[1])[0]
    os.rename(directory + '\\' + newest_file,directory + '\\' + '(1) ' + newest_file)


open_webpage()
input()
click_element()
