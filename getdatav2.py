from selenium import webdriver
#from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

urlpancingan = "https://whoer.net/"
#urlpancingan = "https://www.youtube.com/watch?v=acfjeBZxdig"
urltarget = "https://www.youtube.com/watch?v=w7Gz5djWV4Y"

def nganu(ip):
    
    if(cekipdulu(urlpancingan) == True):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % ip)
        chrome = webdriver.Chrome(options=chrome_options)
        chrome.get(urlpancingan)
        time.sleep(30)

def cekip():
    url = 'https://free-proxy-list.net/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    datas = []
    table = soup.find('table', attrs={'class':'table'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        datas.append([ele for ele in cols if ele]) # Get rid of empty values
    ips = []
    for data in datas:
        if(data[6] == "yes"):
            ip = data[0]+":"+data[1]
            ips.append(ip)
    return ips

def cekipdulu(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    table = soup.find('div', attrs={'class':'error-code'})
    return(pd.isnull(table))


#mulai eksekusi
ips = cekip()
ips5 = ips[0:5]
for ip in ips5:    
    #cekipdulu(urlpancingan)
    nganu(ip)

