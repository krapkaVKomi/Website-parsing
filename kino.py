import requests
from bs4 import BeautifulSoup


class Medal:
    def __init__(self, id:str, country: str, gold: str, silver: str, bronze: str):
        self.id = id
        self.country = country
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    def __str__(self):
        res = f'{self.id} {self.country} gold:  {self.gold} silver:  {self.silver} bronze:  {self.bronze}'
        return res

headers = {}
headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 ' \
                        '(KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'


url = 'http://bus.com.ua/cgi-bin/tablo.pl?as=680900'

response = requests.get(url=url, headers=headers)
if not response.ok:
    print(response.status_code, response.text)
    exit()

data = BeautifulSoup(response.content, "html.parser")
results = data.find('table')
results = results.findNext('table')
for i in results:
    for j in i:
        print(j.text)





