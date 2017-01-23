from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from data_dump import *
import lxml.html

driver = webdriver.PhantomJS()
#driver = webdriver.Chrome(executable_path="/Users/grant/Downloads/chromedriver")
driver.maximize_window()
driver.get('https://www.uscis.gov/e-verify/about-program/e-verify-employers-search-tool?topic_id=&federal_contractor=All&e_verify_employer_agent=1&&employer_zip_code=&employer_city=&items_per_page=50&page=1')
doc = lxml.html.fromstring(driver.page_source)
driver.find_element_by_xpath("//a[@title='Go to last page']").click()
doc = lxml.html.fromstring(driver.page_source)
total = doc.xpath('//li[@class="pager-current last"]/text()') 
int_total = int((total[0]))

for page in range(int_total + 1):
	if page == 0:
		page = 1
	driver.get('https://www.uscis.gov/e-verify/about-program/e-verify-employers-search-tool?topic_id=&federal_contractor=All&e_verify_employer_agent=1&&employer_zip_code=&employer_city=&items_per_page=50&page=%d'%page)
	doc = lxml.html.fromstring(driver.page_source)
	raw_data_1 = doc.xpath('//tr[@class="views-row-first odd"]/td/text()')
	raw_data_2 = doc.xpath('//tr[@class="even"]/td/text()')
	raw_data_3 = doc.xpath('//tr[@class="odd"]/td/text()')
	data_storage_1 = []
	data_storage_1.append(raw_data_1)
	save(data_storage_1)
	data_storage_1 = []
	data_storage_1.append(raw_data_2)
	save(data_storage_1)
	data_storage_1 = []
	data_storage_1.append(raw_data_3)
	save(data_storage_1)
	print page , "/" , total	
	driver.stop()
