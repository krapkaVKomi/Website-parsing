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


url = 'https://www.championat.com/olympic/_olympismog/tournament/588/standing/'

response = requests.get(url=url, headers=headers)
if not response.ok:
    print(response.status_code, response.text)
    exit()

data = BeautifulSoup(response.content, "html.parser")
row = data.find('option')

list = []
while True:
    if row.get('value'):
        list.append(row.get('value'))
    row = row.findNext('option')
    if row is None:
        break


for i in list:
    print(i)        # видалити
    url = 'https://www.championat.com' + i
    if not response.ok:
        print(response.status_code, response.text)
        exit()

    data = BeautifulSoup(response.content, "html.parser")
    results = data.find('tbody')
    row = results.find('tr')

    while True:

        col = row.find_all('td')
        medal = Medal(col[0].text.strip(), col[1].text.strip(), col[2].text.strip(), col[3].text.strip(), col[4].text.strip())
        print(medal.__str__())     # print(medal)
        row = row.findNext('tr')

        if row is None:
            break
    url = 'https://www.championat.com'
