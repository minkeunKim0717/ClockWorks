# -*- coding:utf-8 -*-
import time
from mySystemLogin import SystemLogin
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import platform

if platform.system() == 'Darwin':
	driver = webdriver.Chrome('./chromedriver')
elif platform.system() == 'Windows':
	driver = webdriver.Chrome('chromedriver.exe')

syslogin = SystemLogin()

try:
	driver.get('http://clockworks.microchip.com/Timing/')
	navigation = driver.find_element_by_class_name('navigation')
	navi_list = navigation.find_elements_by_xpath('./ul/li')
	navi_list[6].click()

	# Login
	time.sleep(2)
	jqTransformInputInner = driver.find_elements_by_class_name('jqTransformInputInner')
	userName = jqTransformInputInner[0].find_element_by_id('edit-name')
	userName.send_keys(syslogin.loginSet('ClockWorks', 'Name'))
	print 'here'

	time.sleep(1)
	userPass = jqTransformInputInner[1].find_element_by_id('edit-pass')
	print 'here'
	userPass.send_keys(syslogin.loginSet('ClockWorks', 'Pass'))
	time.sleep(2)
	userPass.send_keys(Keys.RETURN)

	# Go to the page that shows all samples
	time.sleep(2)
	driver.get('http://clockworks.microchip.com/Timing/design/listing/allSampleReqs')
	bodycontainer = driver.find_element_by_class_name('bodycontainer')
	tr_list = bodycontainer.find_elements_by_xpath('./table/tbody/tr')

	# Show the contents of a sample table
	count = 0
	for tr in tr_list:
		td = tr.find_elements_by_xpath('./td')

		# td[9]: Ship Date
		if td[9].text == '-':
			print '-'*100
			print 'Sample-ID: ' + td[0].find_element_by_tag_name('font').text + ', Client: ' + td[2].text + ', Part#: ' + td[4].text + ', Scheduled Ship Date: ' + td[8].text + ' --> Not Shipped Yet'
		else:
			continue

		count += 1

	print '-'*100

except Exception as e:
	print e

finally:
	driver.quit()
