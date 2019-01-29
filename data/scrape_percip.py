from selenium import webdriver
import time
driver = webdriver.Chrome("C:/Users/kiera/OneDrive/Documents/GitHub/ELEC-498-Capstone/data/drivers/chromedriver.exe")

driver.set_page_load_timeout(10)
driver.get('http://climate.weather.gc.ca/climate_data/daily_data_e.html?hlyRange=2008-06-26%7C2018-11-26&dlyRange=2008-07-02%7C2018-11-26&mlyRange=%7C&StationID=47187&Prov=NS&urlExtension=_e.html&searchType=stnProx&optLimit=yearRange&Month=12&Day=27&StartYear=2007&EndYear=2018&Year=2008&selRowPerPage=100&Line=5&txtRadius=25&optProxType=city&selCity=44%7C40%7C63%7C36%7CHalifax&selPark=&txtCentralLatDeg=&txtCentralLatMin=0&txtCentralLatSec=0&txtCentralLongDeg=&txtCentralLongMin=0&txtCentralLongSec=0&timeframe=2')

for year in range(28,38):
	driver.find_element_by_xpath("//select[@id='Year1']/option[" + str(year) + "]").click()
	for month in range(1,13):
		driver.find_element_by_xpath('//select[@id="Month1"]/option[' + str(month) +']').click()
		driver.find_element_by_xpath('//input[@value= "Go"]').click()
		driver.find_element_by_xpath('//input[@value= "Download Data"]').click()


#driver.back()
time.sleep(4)
#driver.quit()