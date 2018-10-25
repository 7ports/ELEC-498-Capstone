from selenium import webdriver
import time
driver = webdriver.Chrome("C:/Users/kiera/OneDrive/Documents/GitHub/ELEC-498-Capstone/data/drivers/chromedriver.exe")

driver.set_page_load_timeout(10)
driver.get('http://climate.weather.gc.ca/climate_data/daily_data_e.html?timeframe=2&Year=2018&Month=10&Day=24&hlyRange=1994-02-28%7C2018-10-24&dlyRange=1980-05-01%7C2018-10-23&mlyRange=1980-01-01%7C2007-02-01&StationID=96&Prov=BC&urlExtension=_e.html&searchType=stnProx&optLimit=specDate&StartYear=1840&EndYear=2018&selRowPerPage=25&Line=12&txtRadius=50&optProxType=city&selCity=48%7C25%7C123%7C22%7CVictoria&selPark=')

for year in range(28,38):
	driver.find_element_by_xpath("//select[@id='Year1']/option[" + str(year) + "]").click()
	for month in range(1,13):
		driver.find_element_by_xpath('//select[@id="Month1"]/option[' + str(month) +']').click()
		driver.find_element_by_xpath('//input[@value= "Go"]').click()
		driver.find_element_by_xpath('//input[@value= "Download Data"]').click()


#driver.back()
time.sleep(4)
#driver.quit()