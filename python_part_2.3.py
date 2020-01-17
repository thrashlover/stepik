import math

from selenium import webdriver


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_css_selector('body > form > div > div > button').click()
alert = browser.switch_to.alert
alert.accept()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

browser.find_element_by_id('answer').send_keys(y)
browser.find_element_by_css_selector('.btn-primary').click()