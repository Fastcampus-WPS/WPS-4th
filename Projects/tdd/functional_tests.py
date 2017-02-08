from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://localhost:8000')
assert 'Welcome to Django' in browser.title
browser.quit()
