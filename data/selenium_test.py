from selenium import webdriver
import time
driver = webdriver.Chrome("C:/Users/Evan\ Bonneau/Documents/ELEC498/ELEC-498-Capstone/data/drivers/chromedriver.exe")


driver.set_page_load_timeout(10)
driver.get('http://climate.weather.gc.ca/radar/index_e.html')
driver.find_element_by_xpath('//select[@name="site"]/optgroup[2]/option[12]').click()
driver.find_element_by_xpath('//select[@name="year"]/option[1]').click()
driver.find_element_by_id("Submit2").click()
driver.back()
time.sleep(4)
driver.quit()
