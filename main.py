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

def click_element(selector,selector_value,duration=60):
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
    time.sleep(2)
    WebDriverWait(driver, 999).until(EC.presence_of_element_located((selector, selector_value)))
    element = driver.find_element(selector,selector_value)
    element.send_keys(message)
    time.sleep(1)

def frame_switch(framevalue, selector='xpath'):
    '''
    switches to appropriate iframe to locate elements
    framevalue = same as selector value (str)
    selector = strategy to locale frame, defaults to xpath as selectors hub uses xpath (str) 
    '''
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

open_webpage() # initialize browser
driver.execute_cdp_cmd("Page.setDownloadBehavior", params) # sets browser download parameters
driver.maximize_window() # puts window in fullscreen

# Queue Report IntraDay Monitoring
group = ['SA_BPO3_PP', 'SA_BPO3_PO']
for report in range(len(group)): # loops through both pre and post
    open_webpage('https://apps.euw2.pure.cloud/directory/#/admin/wfm/intradayMonitoring') # open main page
    # enter appropriate name in textfield
    click_element('xpath','//div[@class="KoControls textHolder"]')
    type_element('xpath','//input[@placeholder="Search"]',group[report])
    type_element('xpath','//input[@placeholder="Search"]',Keys.ENTER)
    frame_switch("//iframe[@title='Workforce Management']") # switch to appropriate iframe
    click_element('xpath','//button[@class="wfmButton previous"]') # go to previous date
    # export all planning groups
    time.sleep(10)
    click_element('xpath','//div[@id="intradayExportButton"]')
    click_element('xpath','//button[normalize-space()="Export All Planning Groups"]')
    time.sleep(30)
    if report == 0:
        rename_newest_file(params["downloadPath"])
    if report == 0: # export current ONLY for prepaid
        click_element('xpath','//div[@id="intradayExportButton"]')
        click_element('xpath','//button[normalize-space()="Export Current"]')
        time.sleep(3)


# Agent Reports
agent_report = ['//a[normalize-space()="Postpaid Agent Activity Report Shubham"]',
                '//a[normalize-space()="Prepaid Agent Activity Report Shubham"]',
                '//a[normalize-space()="Postpaid_APR_shubham"]',
                '//a[normalize-space()="Prepaid_APR_Shubham"]']

for report in range(len(agent_report)):
    # opens reports page
    time.sleep(5)
    open_webpage("https://apps.euw2.pure.cloud/directory/#/engage/reports",30) 
    # switch to appropriate iframe
    frame_switch("//iframe[@id='engage-frame']")
    click_element('xpath',agent_report[report]) # click on report
    # set location under advanced tab
    click_element('xpath','//a[normalize-space()="Advanced"]') 
    click_element('xpath','//button[@class="btn btn-default btn-sm dropdown-toggle select-search-type"]')
    click_element('xpath', '//span[normalize-space()="Location"]')
    if report%2 == 0:
        type_element('xpath','/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/ul[1]/li[1]/input[1]','BPO3 - CT - PO')   
    elif report%2 != 0:
        type_element('xpath','/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/ul[1]/li[1]/input[1]','BPO3 - CT - PP')
    time.sleep(3)
    type_element('xpath','/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/ul[1]/li[1]/input[1]',Keys.ENTER)
    try: # attempt to save settings
        click_element('xpath','//button[@class="btn btn-primary save-advanced-user-select"]')
    except: # back out and cancel if settings button is greyed out (sometimes it is presaved)
        click_element('xpath','/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/button[3]')
    click_element('xpath','//input[@value="now"]') # queue report generation
    # enter date field to be yesterday
    yesterday = (date.today() - timedelta(days = 1)).strftime("%m/%d/%Y") # subtracts 24 hours from current date
    yesterday = yesterday+" - "+yesterday # formats date into string in the same way as website
    date_input_field = click_element('xpath','//input[@id="reportEditor-timePeriod-interval"]') # clicks on date/time menu bar
    date_input_field.clear() # clears the date written previously
    date_input_field.send_keys(yesterday) # types date in date field
    time.sleep(3)
    click_element('xpath','//button[normalize-space()="Apply"]') # apply settings
    click_element('cssselector','button[type="submit"]') # start report generation
    time.sleep(5) # wait for report to generate

#download 4 latest reports
time.sleep(5)
click_element('xpath',"(//a[@title='XLS'][normalize-space()='XLS'])[1]")
click_element('xpath',"(//a[@title='XLS'][normalize-space()='XLS'])[2]")
click_element('xpath',"(//a[@title='XLS'][normalize-space()='XLS'])[3]")
click_element('xpath',"(//a[@title='XLS'][normalize-space()='XLS'])[4]")

print('Finished!')
