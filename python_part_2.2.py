# -*- coding: utf-8 -*

from selenium.webdriver.support.ui import Select

from selenium import webdriver

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)




num1 = browser.find_element_by_id('num1').text
num2 = browser.find_element_by_id('num2').text
res = (int(num1) + int(num2))

select = Select(browser.find_element_by_id('dropdown'))
browser.find_element_by_id('dropdown').send_keys(res)



browser.find_element_by_class_name('btn-default').click()

