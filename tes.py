from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

ip = '52.191.208.232:80'
def nganu(ip):
    print(ip)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % ip)

    chrome = webdriver.Chrome(options=chrome_options)
    chrome.get("https://www.youtube.com/watch?v=acfjeBZxdig")
    get_source = chrome.page_source
    search_text = "ERR_"
    
    if(search_text in get_source == True):
        print("stop")
        time.sleep(30)
    else:
        print("lanjut")
        time.sleep(30)
        quit()
        
    
    time.sleep(30)
    #chrome.get("https://www.youtube.com/watch?v=w7Gz5djWV4Y")
    #time.sleep(400)

def cekip():
    url = 'https://free-proxy-list.net/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    print(soup)
    

nganu("210.148.200.1:8080")