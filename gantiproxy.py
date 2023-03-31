from selenium import webdriver
import time
from getdata import ip


def nganu(ip):
    print(ip)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % ip)

chrome = webdriver.Chrome(options=chrome_options)
chrome.get("https://www.youtube.com/watch?v=acfjeBZxdig")
time.sleep(10)
chrome.get("https://www.youtube.com/watch?v=w7Gz5djWV4Y")
time.sleep(400)