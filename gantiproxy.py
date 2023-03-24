from selenium import webdriver
import time
PROXY = "61.28.233.217:3128" # IP:PORT or HOST:PORT

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)

chrome = webdriver.Chrome(options=chrome_options)
chrome.get("http://whatismyipaddress.com")
time.sleep(10)
