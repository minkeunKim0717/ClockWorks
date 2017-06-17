# -*- coding:utf-8 -*-
import time
import platform
from mySystemLogin import SystemLogin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

if platform.system() == 'Darwin':
    driver = webdriver.PhantomJS('./phantomjs')
elif platform.system() == 'Windows':
    driver = webdriver.PhantomJS('phantomjs.exe')
syslogin = SystemLogin()

try:
	driver.get('http://clockworks.microchip.com/Timing/')
        navi = driver.find_element_by_class_name('navigation')
        # login_link = navi.find_element_by_tag_name('a')
        login_link = navi.find_element_by_link_text('LOG IN')
        login_link.click()

        # Login
	time.sleep(1)
        jqTransformInputInner = driver.find_elements_by_class_name('jqTransformInputInner')
        userName = jqTransformInputInner[0].find_element_by_id('edit-name')
	userName.send_keys(syslogin.loginSet('ClockWorks', 'Name'))
	time.sleep(1)
        userPass = jqTransformInputInner[1].find_element_by_id('edit-pass')
	userPass.send_keys(syslogin.loginSet('ClockWorks', 'Pass'))
	time.sleep(1)
	userPass.send_keys(Keys.RETURN)

	# Go to the page that shows all samples
	time.sleep(1)
	driver.get('http://clockworks.microchip.com/Timing/design/listing/allSampleReqs')
	bodycontainer = driver.find_element_by_class_name('bodycontainer')
	tr_list = bodycontainer.find_elements_by_xpath('./table/tbody/tr')
	# Show the contents of a sample table
	count = 0
	for tr in tr_list:
            td = tr.find_elements_by_xpath('./td')

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
