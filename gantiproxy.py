from selenium import webdriver
import time
PROXY = "190.61.88.147:8080" # IP:PORT or HOST:PORT

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)

chrome = webdriver.Chrome(options=chrome_options)
chrome.get("http://whatismyipaddress.com")
time.sleep(10)
chrome.get("http://google.com")
time.sleep(100)
