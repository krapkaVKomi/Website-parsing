import requests
from bs4 import BeautifulSoup


class CryptoExchange:
    def __init__(self, name: str, volume: str, volume_btc: str, lnk: str):
        self.name = name
        self.volume = volume
        self.volume_btc = volume_btc
        self.get_link = lnk

    def __str__(self):
        return f'Біржа: {self.name}, Об\'єм(24) $: {self.volume}, Об\'єм(24) BTC: {self.volume_btc}'


rating = []

url = f'https://coinmarketcap.com/rankings/exchanges/'
responese = requests.get(url=url)

if not responese.ok:
    print('ERROR:\n', responese.status_code, responese.text)
    exit()

soup = BeautifulSoup(responese.content, 'html.parser')
CMC_table = soup.find('table', {'class': "h7vnx2-2 kDGuD cmc-table"}).find('tbody')
row = CMC_table.findNext('a', {'class': 'cmc-link'})

links = []
while True:
    if row is None:
        break
    get_link = row.get('href', None)
    if 'exchanges' not in get_link:
        break
    links.append(get_link)
    row = row.findNext('a', {'class': 'cmc-link'})

for get_link in links:
    url = f'https://coinmarketcap.com{get_link}'
    response = requests.get(url=url)

    if not response.ok:
        print("Error: \n", response.status_code, response.text)
        exit()

    soup = BeautifulSoup(response.content, 'html.parser')

    name = url.split('/')[-2]
    volume = soup.find('span', {'class', 'sc-14rfo7b-0 pUIyV priceText'})
    if volume is None:
        volume = '-'
    else:
        volume = volume.text.replace('$', '').replace(',', '')
    volume_btc = soup.find('p', {'class', "sc-14rfo7b-0 hnlNry"})
    if volume_btc is None:
        volume_btc = '-'
    else:
        volume_btc = volume_btc.text.replace('BTC', '')

    rate = CryptoExchange(name=name, volume=volume, volume_btc=volume_btc, lnk=get_link)
    rating.append(rate)

for rating_top in rating:
    print(rating_top)
