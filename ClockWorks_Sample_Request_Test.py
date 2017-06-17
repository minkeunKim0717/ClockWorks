# -*- coding:utf-8 -*-
import time
from mySystemLogin import SystemLogin
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
import platform

if platform.system() == 'Darwin':
	driver = webdriver.Chrome('./chromedriver')
elif platform.system() == 'Windows':
	driver = webdriver.Chrome('chromedriver.exe')

syslogin = SystemLogin()
print 'github test'

try:
	# Get the information about a sample
	print '\n\n'
	print '-'*70
	partNumber = raw_input('Enter the sample part number: ')
	noOfSample = raw_input('Enter the number of the sample: ')
	cusApp = raw_input('Enter the application information: ')
	endCompany = raw_input('Enter the end company: ')
	expectedVolume = raw_input('Enter the expected volume: ')
	mpDate = raw_input('Enter the production date(mm/dd/yyyy): ')
	print '-'*70

	print '\n\n'
	print '-'*70
	print 'Information of the samples'
	print '-'*70
	print 'Part Number: ' + partNumber
	print 'Application: ' + cusApp
	print 'End Company: ' + endCompany
	print 'Expected Volume: ' + expectedVolume
	print 'Production Date: ' + mpDate
	print '-'*70
	print 'The automation process has started...'

	# Start
	driver.get('http://clockworks.microchip.com/Timing/')
	navi_list = driver.find_element_by_class_name('navigation').find_elements_by_xpath('./ul/li')
	navi_list[6].click()

	# Login
	time.sleep(2)
	jqTransformInputInner = driver.find_elements_by_class_name('jqTransformInputInner')
	userName = jqTransformInputInner[0].find_element_by_id('edit-name')
	userName.send_keys(syslogin.loginSet('ClockWorks', 'Name'))

	time.sleep(1)
	userPass = jqTransformInputInner[1].find_element_by_id('edit-pass')
	userPass.send_keys(syslogin.loginSet('ClockWorks', 'Pass'))
	time.sleep(2)
	userPass.send_keys(Keys.RETURN)

	# Go to the page that requests the samples of DSC10XX Series
	driver.get('http://clockworks.microchip.com/Timing/OsPartNumberGeneration?PF=DSC10')
	time.sleep(1)
	elem = driver.find_element_by_id('edit-partNumberEnter')
	elem.clear()
	elem.send_keys(partNumber)

	time.sleep(1)
	driver.find_element_by_id('osc_sample_request2').click()

	# "Submit Sample Request" page
	time.sleep(1)
	driver.find_element_by_id('edit-number-of-samples').send_keys(noOfSample)
	time.sleep(3)
	driver.find_element_by_class_name('jqTransformCheckbox').click()
	# checkbox = driver.find_element_by_class_name('jqTransformCheckbox')
	# actions = ActionChains(driver)
	# actions.click(checkbox)
	# actions.perform()

	time.sleep(3)
	driver.find_element_by_id('edit-end-company').send_keys(endCompany)
	time.sleep(3)
	driver.find_element_by_id('edit-ship-application').send_keys(cusApp)
	time.sleep(3)
	driver.find_element_by_id('edit-expected-volume').send_keys(expectedVolume)
	time.sleep(3)
	mpDateSet = driver.find_element_by_id('edit-mp-date-datepicker-popup-0')
	mpDateSet.clear()
	mpDateSet.send_keys(mpDate)
	time.sleep(3)
	driver.find_element_by_id('edit-sampleSubmit').click()

	print 'The Automation process has ended'


except Exception as e:
	print e

finally:
	driver.quit()
