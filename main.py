import urllib.request
import requests
from bs4 import BeautifulSoup

res = requests.get("https://bank.gov.ua/")

if res.status_code == 200:
    soup = BeautifulSoup(res.text, features="html.parser")
    soup_list = soup.find_all("a", {"href": "/ua/markets/exchangerates"})
    res = soup_list[2].find("small")
    print(res)