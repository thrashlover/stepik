# -*- coding: utf-8 -*

import math

from selenium import webdriver

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element_by_id('treasure')
element = x_element.get_attribute("valuex")
x = element
y = calc(x)

browser.find_element_by_id('answer').send_keys(y)
browser.find_element_by_id('robotCheckbox').click()
browser.find_element_by_id('robotsRule').click()
browser.find_element_by_class_name(' btn-default').click()