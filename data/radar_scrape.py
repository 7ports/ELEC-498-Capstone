from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time
import urllib.request
import os

driver = webdriver.Chrome("C:/Users/rajes/OneDrive/Documents/ELEC498/ELEC-498-Capstone/data/drivers/chromedriver.exe")
#no images flag
flag = 0
sitename = 'Victoria'

driver.set_page_load_timeout(10)
driver.get('http://climate.weather.gc.ca/radar/index_e.html')
#iterate over years
for j in range(3,5):
    #Select the correct year for the iteration
    driver.find_element_by_xpath('//select[@name="year"]/option['+ str(j) + ']').click()
    year = driver.find_element_by_xpath('//select[@name="year"]/option['+ str(j) + ']').text
    #iterate over months
    for z in range(1,12):
        #Select the correct month for the iteration
        driver.find_element_by_xpath('//select[@name="month"]/option[' + str(z) +']').click()
        month = driver.find_element_by_xpath('//select[@name="month"]/option[' + str(z) +']').text
        numdays = len(driver.find_element_by_xpath('//select[@name="day"]').text.split('\n'))
        #iterate over days
        for x in range(1,numdays):
            #Select the same starting hour for each iteration (always 00:00)
            driver.find_element_by_xpath('//select[@name="hour"]/option[1]').click()
            driver.find_element_by_xpath('//select[@name="minute"]/option[1]').click()
            #Select the same site for each iteration
            driver.find_element_by_xpath('//select[@name="site"]/optgroup[2]/option[4]').click()
            site = driver.find_element_by_xpath('//select[@name="site"]/optgroup[2]/option[4]').text
            #select the correct day for the iteration
            driver.find_element_by_xpath('//select[@name="day"]/option[' + str(x) +']').click()
            day = driver.find_element_by_xpath('//select[@name="day"]/option[' + str(x) +']').text
            #select the 12 hour duration pictures
            driver.find_element_by_xpath('//select[@name = "duration"]/option[3]').click()

            #select the same image type for each iteration (RAIN 14 colours)
            options = driver.find_element_by_xpath('//select[@name = "image_type"]').text
            #split the list up
            options = options.split('\n')
            #check each option in the list to see if it is Rain 14 colours and make note of the option location
            for t in range(len(options)):
                if options[t] == "No images available":
                    flag = 1
                    break
                if '14' in options[t] and 'Rain' in options[t]:
                    best = t + 1
            driver.find_element_by_xpath('//select[@name ="image_type"]/option[' + str(best) + ']').click()
            #click the submit button
            driver.find_element_by_id("Submit2").click()

            sc = 0
            #iterate over hours
            for i in range(0,12):
                #click through the photos in the animation to increment by hours (only on the second iteration of the loop onwards)
                if sc == 1:
                    try:   
                        driver.find_element_by_id("nextimage").click()
                    except WebDriverException:
                        break
                #get the source element of the image object
                img = driver.find_element_by_xpath("//img[@id = 'radar']")
                src = img.get_attribute('src')
                print(src)
                #open a file with the name information from the form
                imagefile = open(sitename + '-' + year + '-' + day + '-' + month + '-' + str(i) + '.gif', 'wb')
                #write the image value to the file
                imagefile.write(urllib.request.urlopen(src).read())
                imagefile.close()
                sc = 1
                
            
            #go back to do the last hours of the day
            driver.back()

            #repeat all the same form options as above except with an increased time

            #Select the same starting hour for each iteration (always 13:00)
            driver.find_element_by_xpath('//select[@name="hour"]/option[14]').click()
            driver.find_element_by_xpath('//select[@name="minute"]/option[1]').click()
            #Select the same site for each iteration
            driver.find_element_by_xpath('//select[@name="site"]/optgroup[2]/option[4]').click()
            site = driver.find_element_by_xpath('//select[@name="site"]/optgroup[2]/option[4]').text
            #select the correct day for the iteration
            driver.find_element_by_xpath('//select[@name="day"]/option[' + str(x) + ']').click()
            day = driver.find_element_by_xpath('//select[@name="day"]/option[' + str(x) + ']').text
            #select the 12 hour duration pictures
            driver.find_element_by_xpath('//select[@name = "duration"]/option[3]').click()
            #select the same image type for each iteration (RAIN 14 colours)
            options = driver.find_element_by_xpath('//select[@name = "image_type"]').text
            #split the list up
            options = options.split('\n')
            #check each option in the list to see if it is Rain 14 colours and make note of the option location
            for t in range(len(options)):
                if options[t] == "No images available":
                    flag = 1
                    break
                if '14' in options[t] and 'Rain' in options[t]:
                    best = t + 1
            driver.find_element_by_xpath('//select[@name ="image_type"]/option[' + str(best) + ']').click()
            #click the submit button
            driver.find_element_by_id("Submit2").click()

            sc = 0
            for i in range(13,24):
                #click through the photos in the animation to increment by hours (only from the second iteration of the loop onwards)
                if sc == 1:
                    try:   
                        driver.find_element_by_id("nextimage").click()
                    except WebDriverException:
                        break
                #get the source element of the image object
                img = driver.find_element_by_xpath("//img[@id = 'radar']")
                src = img.get_attribute('src')
                print(src)
                #open a file with the name information from the form
                imagefile = open(sitename + '-' + year + '-' + day + '-' + month + '-' + str(i) + '.gif', 'wb')
                #write the image value to the file
                imagefile.write(urllib.request.urlopen(src).read())
                imagefile.close()
                sc = 1
            #go back to reset the form page
            driver.back()
        if flag == 1:
            flag = 0
            break
time.sleep(10)
driver.quit()
