import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def openUrl():
    driver_Path = "/usr/local/chromedriver-linux64/chromedriver"
    brave_Path = "/snap/bin/brave"
    google_Path = "/usr/bin/google-chrome"
    options = webdriver.ChromeOptions()
#    options.binary_location = brave_Path
    options.binary_location = google_Path

    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--remote-debugging-port=9222')
    options.add_argument('--disable-extensions')

    driver = webdriver.Chrome(service=Service(driver_Path), options=options)
    
    url = "https://www.affiligue.org"
    driver.get(url)

    time.sleep(2)
    
    return driver


def connection(driver):
    userName = driver.find_element(By.ID, "MasterContent_content_txtUsername")
    userName.send_keys("username")

    prenom_input = driver.find_element(By.ID, "MasterContent_content_txtPassword")
    prenom_input.send_keys("password")

    login = driver.find_element(By.ID, "MasterContent_content_btnConnect")
    login.click()
    
    adh = driver.find_element(By.ID, "MasterContent_menu_menuLevel_menuLevel_0_link_4")
    adh.click()

    gere = driver.find_element(By.ID, "MasterContent_menu_menuLevel_menuLevel_0_menuLevel_4_link_0")
    gere.click()
