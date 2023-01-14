import requests
from bs4 import BeautifulSoup


class Hotel:
    def __init__(self, name: str, rating: str):
        self.name = name
        self.rating = rating

    def __str__(self):
        res = f' Готель: {self.name}, {self.rating} '
        return res

headers = {}
headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 ' \
                        '(KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'

url = 'https://www.turpravda.ua/ua/kiev/hotels.html?p=1'

response = requests.get(url=url, headers=headers)
if not response.ok:
    print(response.status_code, response.text)
    exit()

data = BeautifulSoup(response.content, "html.parser")
x = []


urls = data.find('div', class_='Pager NumberedPager')
sub_url = urls.find('a')

while True:
    try:
        item = int(sub_url.text)
        x.append(item)
    except:
        break
    sub_url = sub_url.findNext('a')


for store in range(max(x)):
    url = f'https://www.turpravda.ua/ua/kiev/hotels.html?p={store+1}'
    store +=1

    response = requests.get(url=url, headers=headers)
    if not response.ok:
        print(response.status_code, response.text)
        exit()

    data = BeautifulSoup(response.content, "html.parser")
    results = data.find('div', class_='wrapper_tab')

    name = results.find('a', class_='hotel-name-title')
    rating = results.find('div', class_='fluid-item hotel-desc-rating')

    while True:
        our_rating = rating.text
        hotel = name.text.strip()[:30]
        arr = our_rating.split('\n')
        line = ''
        for i in arr:
            if i != '':
                line += i
                line += '   '

        item = Hotel(name=hotel, rating=line)

        name = name.findNext('a', class_='hotel-name-title')
        rating = rating.findNext('div', class_='fluid-item hotel-desc-rating')

        print(item)
        if name is None:
            break

