import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://free-proxy-list.net/'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')
soup