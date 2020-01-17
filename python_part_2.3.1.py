import math

from selenium import webdriver


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_css_selector('.btn-primary').click()


new_window = browser.window_handles[1]
# first_window = browser.window_handles[0]
browser.switch_to.window(new_window)



def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
y = calc(x)

browser.find_element_by_id('answer').send_keys(y)
browser.find_element_by_css_selector('.btn-primary').click()
