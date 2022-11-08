import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


class Trains:
    def __init__(self, train_number: str, route: str, arrival: str):
        self.train_number = train_number
        self.route = route
        self.arrival = arrival

    def __str__(self):
        res = f'Потяг під номером: {self.train_number} \n Маршрут потягy: {self.route} Прибуває на станцію: {self.arrival}'
        return res


headers = {}
headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 ' \
                        '(KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'


date_now = datetime.today()
count = 1
while True:
    plus_days = date_now + timedelta(days=count)
    plus_days = plus_days.strftime('%d.%m.%Y')
    print(plus_days)
    url = f'https://poizdato.net/rozklad-po-stantsii/kyiv-pas/{plus_days}/'
    print(url)
    count += 1

    response = requests.get(url=url, headers=headers)
    if not response.ok:
        print(response.status_code, response.text)
        exit()

    data = BeautifulSoup(response.content, "html.parser")
    results = data.find('tbody')

    try:
        row = results.find('tr')
    except AttributeError:
        print('Данних більше немає')
        break

    while True:
        col = row.find_all('td')
        train = Trains(train_number=col[1].text, route=col[2].text, arrival=col[5].text)
        row = row.findNext('tr')
        print(train.__str__())

        if row is None:
            break





