from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#adding incognito option to the chrome session
option = webdriver.ChromeOptions()
option.add_argument(" - incognito")

#create instance of chrome
browser = webdriver.Chrome(executable_path='/Library/ApplicationSupport/Google/chromedriver', chrome_options=option)


