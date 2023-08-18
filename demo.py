import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

#initalizing driver settings
options = uc.ChromeOptions()
# chrome://version/
profile = "C:\\Users\\thelo\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2" # CHANGE TO CHROME PROFILE PATH
options.add_argument(f"user-data-dir={profile}")
driver = uc.Chrome(options=options,use_subprocess=True)

method_dict = {
    "xpath": By.XPATH,
    "cssselector": By.CSS_SELECTOR,
    "id": By.ID
}

def click_element(mode,id,duration=999):
    mode = method_dict[mode]
    WebDriverWait(driver, duration).until(EC.presence_of_element_located((mode, id)))
    driver.find_element(mode,id).click()
    time.sleep(3)

''' # deprecated
driver.get("https://apps.euw2.pure.cloud/directory/#/admin/wfm/intradayMonitoring")
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class,'top-level-menu-item-label')][normalize-space()='Performance']")))
driver.find_element(By.XPATH,"//span[contains(@class,'top-level-menu-item-label')][normalize-space()='Performance']").click()
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Workspace']")))
driver.find_element(By.XPATH,"//span[normalize-space()='Workspace']").click()
'''

driver.get("https://apps.euw2.pure.cloud/directory/#/analytics/")
time.sleep(25)
frame = driver.find_element(By.XPATH, "(//iframe[@title='Analytics UI'])[1]")
driver.switch_to.frame(frame)
WebDriverWait(driver, 999).until(EC.presence_of_element_located((By.XPATH, "(//button[@title='Create New Tab'])[1]")))
time.sleep(2)
driver.find_element(By.XPATH,"(//button[@title='Create New Tab'])[1]").click()
WebDriverWait(driver, 999).until(EC.presence_of_element_located((By.LINK_TEXT,"Harender Singh ASD")))
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Harender Singh ASD").click()
time.sleep(3)
click_element("xpath", '//button[@title="Previous date"]')
click_element("xpath","(//button[@title='Toggle export panel'])[1]")
click_element("xpath", '//button[normalize-space()="Export"]')
driver.switch_to.default_content()
time.sleep(1)
WebDriverWait(driver, 999).until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[4]/div[1]/nav[1]/div[1]/div[2]/nav[1]/ul[1]/li[6]/a[1]"))).click()
WebDriverWait(driver, 999).until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[4]/div[1]/main[1]/section[4]/div[1]/div[1]/div[2]/button[10]"))).click()
time.sleep(30)
time.sleep(2)
click_element("cssselector", "body > div:nth-child(12) > div:nth-child(1) > main:nth-child(4) > section:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(10) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > button:nth-child(1)")

input('continue: ')

time.sleep(10)
frame = driver.find_element(By.XPATH, "//iframe[@title='Analytics UI']")
driver.switch_to.frame(frame)
WebDriverWait(driver, 999).until(EC.presence_of_element_located((By.XPATH, "(//button[@title='Create New Tab'])[1]")))
driver.find_element(By.XPATH,"(//button[@title='Create New Tab'])[1]").click()
time.sleep(3)
click_element('xpath',"(//a[normalize-space()='Queue Performance'])[1]")
time.sleep(5)
click_element('xpath','//i[@class="pc pc-plus"]')
click_element('xpath','//label[contains(@class,"column-label error")]')
click_element('xpath','//span[@class="column-label-text abandonNoShort"]')

print("Finish")
time.sleep(9999)
