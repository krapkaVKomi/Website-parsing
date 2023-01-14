import requests
from bs4 import BeautifulSoup


class Chart:
    def __init__(self, avtor: str, song: str):
        self.avtor = avtor
        self.song = song

    def __str__(self):
        res = f'Автор: {self.avtor} Пісня: {self.song}'
        return res

headers = {}
headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 ' \
                        '(KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'


url = 'https://muzati.net/top100month'          # cortm

response = requests.get(url=url, headers=headers)
if not response.ok:
    print(response.status_code, response.text)
    exit()

data = BeautifulSoup(response.content, "html.parser")
x = []

x.append('/top100month')
urls = data.find('div', class_='cortm')
sub_url = urls.find('a', class_='catSortLink')
while True:
    line = sub_url.get('href')
    x.append(line)
    sub_url = sub_url.findNext('a', class_='catSortLink')
    if sub_url is None:
        break


for i in x:
    url = f'https://muzati.net{i}'

    response = requests.get(url=url, headers=headers)
    if not response.ok:
        print(response.status_code, response.text)
        exit()

    data = BeautifulSoup(response.content, "html.parser")
    results = data.find('div', class_='col-md-8')

    name = results.find('div', class_='track-play js-ctrl js-play')
    count = 0
    while True:
        count += 1
        print(count)
        line = name.get('title')
        avtor = line.split('-')

        item = Chart(avtor=avtor[0], song=avtor[1].strip())
        print(item)
        name = name.findNext('div', class_='track-play js-ctrl js-play')
        if name is None:
            break






