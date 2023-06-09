import requests
from bs4 import BeautifulSoup
import pandas as pd

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
    
ips = cekip()
print(list.count(ips))