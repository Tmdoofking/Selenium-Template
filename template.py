import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

# 開啟乾淨了瀏覽器
def open_chrome():
    options = webdriver.ChromeOptions()
    # 擴充程式
    # options.add_extension('something.crx')
    # 啟動 headless 模式
    # options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    return driver

# 簡化程式碼
def web(driver, timeout, locator_type, locator):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((locator_type, locator)))

# ActionChains 
def perform_actions(driver, keys):
    actions = ActionChains(driver)
    actions.send_keys(keys)
    time.sleep(2)
    actions.perform()

# 重製瀏覽器，而不是重新開啟一個新的
def resetsystem(driver):
    driver.get("https://google.com/")
    driver.execute_script("window.open('')")  # Create a separate tab than the main one
    driver.switch_to.window(driver.window_handles[-1])  # Switch window to the second tab
    driver.get('chrome://settings/clearBrowserData')  # Open your chrome settings.
    perform_actions(driver,
                    Keys.TAB + Keys.ENTER)  # Tab to the time select and key down to say "All Time" then go to the Confirm button and press Enter
    driver.close()  # Close that window
    driver.switch_to.window(driver.window_handles[1])  # Switch Selenium controls to the original tab to continue normal functionality.
    time.sleep(2)