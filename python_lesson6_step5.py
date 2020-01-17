# -*- coding: utf-8 -*

import math
from selenium import webdriver

link = "http://suninjuly.github.io/find_link_text"

browser = webdriver.Chrome()
browser.get(link)
a = str(math.ceil(math.pow(math.pi, math.e)*10000))
browser.find_element_by_partial_link_text(a).click()
