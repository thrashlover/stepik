import os

from selenium import webdriver


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)


current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')


browser.find_element_by_name('firstname').send_keys('Kek')
browser.find_element_by_name('lastname').send_keys('Shlek')
browser.find_element_by_name('email').send_keys('666@333.mail.ru')
browser.find_element_by_css_selector('#file').send_keys(file_path)
browser.find_element_by_class_name('btn-primary').click()




