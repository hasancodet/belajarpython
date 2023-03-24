import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('/path/to/chromedriver')
service.start()
driver = webdriver.Remote(service.service_url)
driver.get('https://www.youtube.com/watch?v=w7Gz5djWV4Y');
time.sleep(400) # Let the user actually see something!
driver.quit()
