import requests
from bs4 import BeautifulSoup


headers = {}
headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 ' \
                        '(KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
print(type(headers))
x = ['spot', 'perpetual', 'futures']
for i in x:
    url = f'https://coinmarketcap.com/exchanges/binance/?type={i}'

    response = requests.get(url=url, headers=headers)
    if not response.ok:
        print(response.status_code, response.text)
        exit()

    data = BeautifulSoup(response.content, "html.parser")
    results = data.find('table')
    results = results.find_all('tr')
    for i in results:
        for j in i:
            print(j.text)
        print('\n'*2)

    print('\n' * 30)