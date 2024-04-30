from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://www.webull.com/quote/crypto'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

stock_data = soup.findAll('div', attrs={'class':'table-cell'})


counter = 1
for x in range(5):
    name = stock_data[counter].text.rstrip('USD')[1:-3]
    symbol = stock_data[counter].text.rstrip('USD')[-3:]
    if stock_data[counter].text.rstrip('USD')[-4:].isupper() == True:
        symbol = stock_data[counter].text.rstrip('USD')[-4:]
        name = stock_data[counter].text.rstrip('USD')[1:-4]
    change = float(stock_data[counter+2].text.strip('+').strip('-').strip('%'))
    last_price = float(stock_data[counter+1].text.replace(",",""))
    prev_price = round(last_price / (1 + (change/100)), 2)

    print()
    print()
    print(f'Crypto Name: {name}')
    print(f'Crypto Symbol: {symbol}')
    print(f'Change: {change}%')
    print(f'Price: ${last_price:,}')
    print(f'Previous Price: ${prev_price:,}')

    counter+=10

