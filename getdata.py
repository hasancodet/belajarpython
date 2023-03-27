import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://free-proxy-list.net/'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')
#print(soup)

datas = []
table = soup.find('table', attrs={'class':'table'})
table_body = table.find('tbody')

rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    datas.append([ele for ele in cols if ele]) # Get rid of empty values

for data in datas:
    if(data[6] == "no"):
        print("no")
    else:
        ip = data[0]+":"+data[1]
        print(ip)
        break
        #print("yes")