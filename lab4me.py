import requests
from bs4 import BeautifulSoup


class Item:
    def __init__(self, name: str, vin_rete: str, kda: str, popularity: str):
        self.name = name
        self.vin_rete = vin_rete
        self.popularity = popularity
        self.kda = kda

    def __str__(self):
        res = f'Персонаж: {self.name}, Відсоток перемог: {self.vin_rete}, ' \
              f'Відсоток популярності: {self.popularity}, Kills Deaths Assists: {self.kda}'
        return res


sub_url = 'https://uk.dotabuff.com/heroes/winning'
headers = {}
headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36(KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'

response = requests.get(url=sub_url, headers=headers)
if not response.ok:
    print(response.status_code, response.text)
    exit()

data = BeautifulSoup(response.content, "html.parser")
row = data.find('option')

list_patch = []
while True:
    if row.get('value') not in 'separator' \
            and row.get('value') not in 'separator_season' \
            and row.get('value') not in 'separator_patch':
        list_patch.append(row.get('value'))
    row = row.findNext('option')
    if row is None:
        break


url = 'https://uk.dotabuff.com/heroes/winning?date='
for i in list_patch:
    our_url = url + i
    response = requests.get(url=our_url, headers=headers)
    if not response.ok:
        print(response.status_code, response.text)
        exit()

    data = BeautifulSoup(response.content, "html.parser")
    results = data.find('tbody')
    cources = []
    row = results.find('tr')

    while True:
        col = row.find_all('td')
        name = col[1].text
        vin_rete = col[2].text
        popularity = col[3].text
        kda = col[4].text
        line = Item(name=name[5:], vin_rete=vin_rete, popularity=popularity, kda=kda)
        print(line)

        row = row.findNext('tr')
        if row is None:
            break




